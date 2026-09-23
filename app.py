from datetime import date

import pandas as pd
import streamlit as st

from plan import PlanBook
from plan.measurements import Measurement, MeasurementLog

book = PlanBook()
TODAY = date.today()
TODAY_PLATE = book.plate_on(TODAY)
THIS_WEEK = book.week_on(TODAY)
WEEKDAYS = book.store.weekdays()
SEED = book.store.seed
LOG = MeasurementLog()
LOG.ensure_opening_reading(SEED)


def written_date(day: date) -> str:
    return f"{day.strftime('%A')}, {day.day} {day.strftime('%b %Y')}"


def short_date(day: date) -> str:
    return f"{day.day} {day.strftime('%b %Y')}"


DAYS_TO_GOAL = (SEED.goal_date - TODAY).days

st.set_page_config(
    page_title=f"{SEED.name}'s plan",
    page_icon="⬤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      .stApp { background: #12140F; }
      header[data-testid="stHeader"] { background: #12140F; }
      .block-container { padding-top: 1.4rem; max-width: 1180px; }
      h1, h2, h3 { font-family: "Iowan Old Style", "Palatino Linotype", Palatino, serif; letter-spacing: -0.02em; }
      .eyebrow { color: #D7A15A; font-size: 0.78rem; letter-spacing: 0.16em; text-transform: uppercase; font-weight: 600; }
      .hero-title { font-size: 2.4rem; line-height: 1.1; margin: 0.2rem 0 0.4rem; color: #F4EFE4; }
      .hero-copy { color: #C8C0B0; font-size: 1.05rem; max-width: 42rem; }
      .card {
        background: #1B1F18;
        border: 1px solid #2A3124;
        border-radius: 16px;
        padding: 1rem 1.1rem 1.05rem;
        height: 100%;
      }
      .card h3 { margin: 0 0 0.35rem; font-size: 1.2rem; }
      .muted { color: #A39B8C; font-size: 0.92rem; }
      .gold { color: #D7A15A; }
      .pill {
        display: inline-block;
        border: 1px solid #3A3324;
        background: #241F14;
        color: #E6C98A;
        border-radius: 999px;
        padding: 0.15rem 0.6rem;
        font-size: 0.75rem;
        margin: 0 0.35rem 0.35rem 0;
      }
      .meal-kcal { float: right; color: #D7A15A; font-variant-numeric: tabular-nums; }
      .stCheckbox { padding-top: 0.15rem; }
      div[data-testid="stMetric"] {
        background: #1B1F18;
        border: 1px solid #2A3124;
        border-radius: 14px;
        padding: 0.7rem 0.85rem;
      }
      .footer-note { color: #7D7668; font-size: 0.82rem; margin-top: 2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)


def check(key: str, label: str) -> bool:
    return st.checkbox(label, key=key)


def measurement_chart(dates: list[date], values: list[float], unit: str) -> str:
    width, height = 560, 230
    left, right, top, bottom = 52, 16, 16, 36
    plot_width = width - left - right
    plot_height = height - top - bottom
    low = min(values)
    high = max(values)
    if high == low:
        low -= 1
        high += 1

    def x_at(index: int) -> float:
        if len(values) == 1:
            return left + plot_width / 2
        return left + plot_width * index / (len(values) - 1)

    def y_at(value: float) -> float:
        return top + plot_height * (1 - (value - low) / (high - low))

    points = " ".join(f"{x_at(index):.1f},{y_at(value):.1f}" for index, value in enumerate(values))
    dots = "".join(
        f'<circle cx="{x_at(index):.1f}" cy="{y_at(value):.1f}" r="3.5" fill="#D7A15A"/>'
        for index, value in enumerate(values)
    )
    first = f"{dates[0].day} {dates[0].strftime('%b')}"
    last = f"{dates[-1].day} {dates[-1].strftime('%b')}"
    return f"""
    <svg viewBox="0 0 {width} {height}" width="100%" role="img">
      <rect width="{width}" height="{height}" fill="#1B1F18" rx="12"/>
      <line x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_height}" stroke="#2A3124"/>
      <line x1="{left}" y1="{top + plot_height}" x2="{left + plot_width}" y2="{top + plot_height}" stroke="#2A3124"/>
      <text x="{left - 8}" y="{top + 4}" fill="#A39B8C" font-size="12" text-anchor="end">{high:.1f}</text>
      <text x="{left - 8}" y="{top + plot_height}" fill="#A39B8C" font-size="12" text-anchor="end">{low:.1f}</text>
      <text x="{left}" y="{height - 10}" fill="#A39B8C" font-size="12">{first}</text>
      <text x="{left + plot_width}" y="{height - 10}" fill="#A39B8C" font-size="12" text-anchor="end">{last}</text>
      <polyline points="{points}" fill="none" stroke="#D7A15A" stroke-width="2"/>
      {dots}
      <text x="{left + plot_width}" y="14" fill="#7D7668" font-size="11" text-anchor="end">{unit}</text>
    </svg>
    """


def meal_card(meal) -> None:
    items = "".join(f"<div class='muted'>{item.label()}</div>" for item in meal.servings)
    note = f"<div class='muted' style='margin-top:0.35rem'>{meal.note}</div>" if meal.note else ""
    st.markdown(
        f"""
        <div class="card" style="margin-bottom:0.7rem">
          <span class="pill">{meal.name}</span>
          <span class="meal-kcal">{meal.kcal} kcal · {meal.protein_g:.0f} g protein</span>
          <div style="margin-top:0.7rem">{items}</div>
          {note}
        </div>
        """,
        unsafe_allow_html=True,
    )


protein_kind = "Higher-protein day" if TODAY_PLATE.high_protein else "Normal day"
if DAYS_TO_GOAL > 1:
    countdown_label = f"{DAYS_TO_GOAL} days left"
elif DAYS_TO_GOAL == 1:
    countdown_label = "1 day left"
elif DAYS_TO_GOAL == 0:
    countdown_label = "Goal day"
else:
    countdown_label = f"{abs(DAYS_TO_GOAL)} days past goal"

st.markdown(
    f'<div class="eyebrow">{written_date(TODAY)} · {countdown_label} until {short_date(SEED.goal_date)}</div>',
    unsafe_allow_html=True,
)
st.markdown(f'<div class="hero-title">{SEED.name}\'s {SEED.plan_title}</div>', unsafe_allow_html=True)
st.markdown(
    f'<p class="hero-copy">{SEED.tagline} Week {THIS_WEEK.number} of {SEED.week_count} '
    f"({THIS_WEEK.date_label()}). Today is {TODAY_PLATE.weekday}, a {protein_kind.lower()}.</p>",
    unsafe_allow_html=True,
)

when1, when2, when3 = st.columns(3)
when1.metric("Today", short_date(TODAY))
when2.metric("Countdown", countdown_label)
when3.metric("Goal", short_date(SEED.goal_date))

steps = f"{SEED.steps_low:,}–{SEED.steps_high // 1000}k"
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Calories today", f"{TODAY_PLATE.kcal}")
c2.metric("Protein", f"{TODAY_PLATE.protein_label()} g")
c3.metric("Rice", f"{TODAY_PLATE.rice_spoons} spoons")
c4.metric("Workout", book.store.session(TODAY_PLATE.weekday).name)
c5.metric("Steps", steps)

today_tab, diet_tab, train_tab, road_tab, shop_tab, charts_tab = st.tabs(
    ["Today", "Counted diet", "Training", "Roadmap", "Grocery", "Charts"]
)

with today_tab:
    left, right = st.columns((1.25, 1))
    with left:
        st.subheader("Eat this")
        st.caption(SEED.spoon_guide[0])
        for meal in TODAY_PLATE.meals:
            meal_card(meal)
            check(f"meal_{TODAY_PLATE.weekday}_{meal.name}", f"Ate {meal.name.lower()}")
    with right:
        session = book.store.session(TODAY_PLATE.weekday)
        st.subheader("Train this")
        st.markdown(
            f"""
            <div class="card">
              <span class="pill">{session.kind}</span>
              <span class="pill">{session.minutes} min</span>
              <span class="pill">{session.place}</span>
              <h3>{session.name}</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for line in session.exercises:
            st.markdown(f"- {line}")
        check(f"wo_{TODAY_PLATE.weekday}", f"Finished {session.name.lower()}")
        st.divider()
        st.subheader("Daily marks")
        check("steps", f"Steps {SEED.steps_low:,}–{SEED.steps_high:,}")
        check("sleep", f"Slept {SEED.sleep_low_hours}–{SEED.sleep_high_hours} hours")
        check("weigh", "Morning weight recorded")
        st.info(SEED.protein_note)

with diet_tab:
    st.subheader("The counted plate")
    st.caption(" ".join(SEED.spoon_guide))
    default_index = WEEKDAYS.index(TODAY_PLATE.weekday) if TODAY_PLATE.weekday in WEEKDAYS else 0
    picked_name = st.radio("Day", WEEKDAYS, horizontal=True, index=default_index)
    picked = next(day for day in book.store.dates_in(THIS_WEEK) if day.strftime("%A") == picked_name)
    plate = book.plate_on(picked)
    kind = "Higher-protein day" if plate.high_protein else "Normal day"
    high_lunch = THIS_WEEK.lunch_rice_spoons - SEED.high_day_fewer_rice_spoons
    st.caption(
        f"{kind}. Normal lunch is {THIS_WEEK.lunch_rice_spoons} rice spoons, "
        f"dinner is {THIS_WEEK.dinner_rice_spoons}. "
        f"Wednesday and Sunday lunch is {high_lunch}."
    )

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Calories", plate.kcal)
    m2.metric("Protein", f"{plate.protein_label()} g")
    m3.metric("Carbs, estimated", f"{plate.carbs_label()} g")
    m4.metric("Fat", f"{plate.fat_label()} g")

    for meal in plate.meals:
        with st.expander(f"{meal.name} · {meal.kcal} kcal", expanded=meal.name in ("Breakfast", "Lunch")):
            for item in meal.servings:
                st.write(f"- {item.label()}")
            if meal.note:
                st.caption(meal.note)

    st.divider()
    st.subheader("Rice comes down, then holds")
    rows = []
    for week, normal, high in book.ladder():
        rows.append(
            {
                "Week": week.number,
                "Dates": week.date_label(),
                "Lunch spoons": week.lunch_rice_spoons,
                "Dinner spoons": week.dinner_rice_spoons,
                "Oil tsp": week.oil_teaspoons,
                "Normal day": normal.kcal,
                "Wed / Sun": high.kcal,
            }
        )
    st.dataframe(rows, hide_index=True, width="stretch")

with train_tab:
    st.subheader("Four lifting days")
    st.caption("Monday and Thursday upper. Tuesday and Friday lower. Walk on Wednesday, Saturday, and Sunday.")
    sessions = book.store.sessions()
    st.metric("Minutes this week", sum(session.minutes for session in sessions))
    cols = st.columns(2)
    for index, session in enumerate(sessions):
        with cols[index % 2]:
            st.markdown(
                f"""
                <div class="card" style="margin-bottom:0.75rem">
                  <span class="pill">{session.weekday}</span>
                  <span class="pill">{session.kind}</span>
                  <span class="pill">{session.minutes} min</span>
                  <h3>{session.name}</h3>
                  <div class="muted">{session.place}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            for line in session.exercises:
                st.markdown(f"- {line}")
            check(f"wo_week_{session.weekday}", f"Done · {session.weekday}")

with road_tab:
    st.subheader("92–94 kg by 30 Dec")
    st.write(SEED.goal)
    body = book.store.body()
    b1, b2, b3, b4 = st.columns(4)
    b1.metric("Now", f"{body.weight_kg:g} kg")
    b2.metric("Body fat", f"{body.body_fat_percent:g}%")
    b3.metric("Skeletal muscle", f"{body.skeletal_muscle_kg:g} kg")
    b4.metric("BMR", f"{body.bmr_kcal:,} kcal")
    st.caption(
        f"Height {body.height_cm:g} cm · BMI {body.bmi:g} · "
        f"fat {body.fat_kg:g} kg · lean mass {body.fat_free_kg:g} kg. "
        "One scan is a rough reading. Follow the weekly average."
    )
    st.subheader("Checkpoints")
    checkpoint_rows = []
    for point in book.store.checkpoints():
        checkpoint_rows.append(
            {
                "Date": point.date_label(),
                "7-day average": point.range_label(),
            }
        )
    st.dataframe(checkpoint_rows, hide_index=True, width="stretch")
    st.divider()
    st.subheader("How to run the 14 weeks")
    for rule in SEED.rules:
        st.markdown(f"- {rule}")
    st.subheader("Leave these alone")
    for line in SEED.avoid:
        st.markdown(f"- {line}")

with shop_tab:
    st.subheader(f"Week {THIS_WEEK.number} shopping counts")
    st.caption(f"{THIS_WEEK.date_label()}. Counts are for the days in this week, already multiplied out.")
    query = st.text_input("Filter foods", placeholder="rice, egg, chicken…")
    shown = 0
    for line in book.grocery(THIS_WEEK):
        if query and query.lower() not in line.food.lower():
            continue
        shown += 1
        with st.expander(f"{line.food} · {line.amount}"):
            st.write(line.detail)
    if shown == 0:
        st.warning("Nothing matches that filter.")

with charts_tab:
    st.subheader("Weight and body composition")
    st.caption("Enter one reading per morning. Saving a date that already exists replaces that day.")
    latest = LOG.latest()
    with st.form("body_log"):
        measured_on = st.date_input("Date", value=TODAY, key="measure_date")
        weight = st.number_input(
            "Weight (kg)",
            min_value=30.0,
            max_value=250.0,
            value=float(latest.weight_kg if latest else SEED.weight_kg),
            step=0.1,
            key="measure_weight",
        )
        muscle = st.number_input(
            "Skeletal muscle (kg)",
            min_value=5.0,
            max_value=120.0,
            value=float(latest.skeletal_muscle_kg if latest else SEED.skeletal_muscle_kg),
            step=0.1,
            key="measure_muscle",
        )
        water = st.number_input(
            "Body water (kg)",
            min_value=5.0,
            max_value=120.0,
            value=float(latest.body_water_kg if latest else SEED.body_water_kg),
            step=0.1,
            key="measure_water",
        )
        fat = st.number_input(
            "Fat (kg)",
            min_value=1.0,
            max_value=120.0,
            value=float(latest.fat_kg if latest else SEED.fat_kg),
            step=0.1,
            key="measure_fat",
        )
        submitted = st.form_submit_button("Save measurement")
    if submitted:
        LOG.save(
            Measurement(
                on=measured_on,
                weight_kg=weight,
                skeletal_muscle_kg=muscle,
                body_water_kg=water,
                fat_kg=fat,
            )
        )
        st.session_state["measure_saved"] = short_date(measured_on)
        st.rerun()
    saved_label = st.session_state.pop("measure_saved", None)
    if saved_label:
        st.success(f"Saved {saved_label}.")

    readings = LOG.all()
    frame = pd.DataFrame(
        {
            "Date": [row.on for row in readings],
            "Weight (kg)": [row.weight_kg for row in readings],
            "Fat (kg)": [row.fat_kg for row in readings],
            "Skeletal muscle (kg)": [row.skeletal_muscle_kg for row in readings],
            "Body water (kg)": [row.body_water_kg for row in readings],
        }
    )
    chart_dates = [row.on for row in readings]
    left, right = st.columns(2)
    with left:
        st.markdown("**Weight**")
        st.markdown(measurement_chart(chart_dates, frame["Weight (kg)"].tolist(), "kg"), unsafe_allow_html=True)
        st.markdown("**Fat**")
        st.markdown(measurement_chart(chart_dates, frame["Fat (kg)"].tolist(), "kg"), unsafe_allow_html=True)
    with right:
        st.markdown("**Skeletal muscle**")
        st.markdown(
            measurement_chart(chart_dates, frame["Skeletal muscle (kg)"].tolist(), "kg"),
            unsafe_allow_html=True,
        )
        st.markdown("**Body water**")
        st.markdown(
            measurement_chart(chart_dates, frame["Body water (kg)"].tolist(), "kg"),
            unsafe_allow_html=True,
        )
    st.dataframe(frame, hide_index=True, width="stretch")

st.markdown(
    '<p class="footer-note">Numbers live in plan/seed_data.py. The screens read them through the plan book. '
    "Not medical advice.</p>",
    unsafe_allow_html=True,
)
