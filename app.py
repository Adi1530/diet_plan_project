from datetime import date

import streamlit as st

from plan import (
    GOALS,
    NAME,
    PLAN_TITLE,
    PROFILE,
    RULES,
    TAGLINE,
    WEEKDAYS,
    WEEKS,
    WORKOUTS,
    day_meals,
    day_totals,
    grocery_list,
    week_number,
)

st.set_page_config(
    page_title=f"{NAME}'s plan",
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
      .hero-copy { color: #C8C0B0; font-size: 1.05rem; max-width: 40rem; }
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
        margin-right: 0.35rem;
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

TODAY = date.today()
TODAY_NAME = TODAY.strftime("%A")
if TODAY_NAME not in WEEKDAYS:
    TODAY_NAME = "Monday"

WEEK = week_number(TODAY)


def init_state() -> None:
    if "checked" not in st.session_state:
        st.session_state.checked = {}


def check(key: str, label: str) -> bool:
    return st.checkbox(label, key=f"chk_{key}")


init_state()

st.markdown('<div class="eyebrow">Personal command sheet · no login · just you</div>', unsafe_allow_html=True)
st.markdown(f'<div class="hero-title">{NAME}\'s {PLAN_TITLE}</div>', unsafe_allow_html=True)
st.markdown(f'<p class="hero-copy">{TAGLINE} Week {WEEK} of {WEEKS}. Today is {TODAY_NAME}.</p>', unsafe_allow_html=True)

today_food = day_totals(TODAY_NAME)
today_wo = WORKOUTS[TODAY_NAME]

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Calories today", f"{today_food['kcal']}", f"target {PROFILE['calories']}")
c2.metric("Protein", f"{today_food['p']} g", f"target {PROFILE['protein_g']} g")
c3.metric("Carbs / fat", f"{today_food['c']} / {today_food['f']} g")
c4.metric("Workout", f"{today_wo['minutes']} min", today_wo["kind"])
c5.metric("Water / steps", f"{PROFILE['water_l']:.0f} L · {PROFILE['steps']:,}")

today_tab, diet_tab, train_tab, goals_tab, shop_tab = st.tabs(
    ["Today", "7-day diet", "Training", "Goals", "Grocery"]
)

with today_tab:
    left, right = st.columns((1.25, 1))
    with left:
        st.subheader("Eat this")
        st.caption(PROFILE["style"])
        for meal in day_meals(TODAY_NAME):
            st.markdown(
                f"""
                <div class="card" style="margin-bottom:0.7rem">
                  <span class="pill">{meal["slot"]}</span>
                  <span class="pill">{meal["minutes"]} min</span>
                  <span class="meal-kcal">{meal["kcal"]} kcal · {meal["p"]}p {meal["c"]}c {meal["f"]}f</span>
                  <h3>{meal["name"]}</h3>
                  <div class="muted">{meal["plate"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            check(f"meal_{TODAY_NAME}_{meal['id']}", f"Ate {meal['name']}")
    with right:
        st.subheader("Train this")
        st.markdown(
            f"""
            <div class="card">
              <span class="pill">{today_wo["kind"]}</span>
              <span class="pill">{today_wo["minutes"]} min</span>
              <span class="pill">{today_wo["place"]}</span>
              <h3>{today_wo["name"]}</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for line in today_wo["blocks"]:
            st.markdown(f"- {line}")
        check(f"wo_{TODAY_NAME}", f"Finished {today_wo['name']}")
        st.divider()
        st.subheader("Daily marks")
        check("water", f"Drank {PROFILE['water_l']:.0f} L water")
        check("steps", f"Hit {PROFILE['steps']:,} steps")
        check("sleep", f"Slept {PROFILE['sleep_h']:.0f} hours")
        check("protein", f"Hit {PROFILE['protein_g']} g protein")
        st.info(PROFILE["notes"])

with diet_tab:
    st.subheader("The week on a plate")
    st.caption(
        f"Built to land near {PROFILE['calories']} kcal and {PROFILE['protein_g']} g protein. "
        "Swap a meal only with another from the same slot."
    )
    pick = st.radio("Day", WEEKDAYS, horizontal=True, index=WEEKDAYS.index(TODAY_NAME))
    totals = day_totals(pick)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Calories", totals["kcal"])
    m2.metric("Protein", f"{totals['p']} g")
    m3.metric("Carbs", f"{totals['c']} g")
    m4.metric("Fat", f"{totals['f']} g")

    for meal in day_meals(pick):
        with st.expander(f"{meal['slot'].title()} — {meal['name']} · {meal['kcal']} kcal", expanded=meal["slot"] in ("breakfast", "lunch")):
            st.write(meal["plate"])
            st.caption(f"{meal['p']}g protein · {meal['c']}g carbs · {meal['f']}g fat · {meal['minutes']} min")
            st.write("**Shop**")
            for name, amount in meal["ingredients"]:
                st.write(f"- {amount} {name}")

    st.divider()
    rows = []
    for day in WEEKDAYS:
        t = day_totals(day)
        rows.append(
            {
                "Day": day,
                "Calories": t["kcal"],
                "Protein": t["p"],
                "Carbs": t["c"],
                "Fat": t["f"],
                "Cook min": t["minutes"],
            }
        )
    st.dataframe(rows, hide_index=True, width="stretch")

with train_tab:
    st.subheader("Weekly training")
    st.caption("Three lifts, two easy conditioning days, one real rest day. Times include setup.")
    total_min = sum(w["minutes"] for w in WORKOUTS.values())
    st.metric("Minutes this week", total_min)

    cols = st.columns(2)
    for i, day in enumerate(WEEKDAYS):
        w = WORKOUTS[day]
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="card" style="margin-bottom:0.75rem">
                  <span class="pill">{day}</span>
                  <span class="pill">{w["kind"]}</span>
                  <span class="pill">{w["minutes"]} min</span>
                  <h3>{w["name"]}</h3>
                  <div class="muted">{w["place"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            for line in w["blocks"]:
                st.markdown(f"- {line}")
            check(f"wo_week_{day}", f"Done · {day}")

with goals_tab:
    st.subheader("What winning this block looks like")
    st.write(PROFILE["goal"])
    for goal in GOALS:
        with st.container(border=True):
            top = st.columns((4, 1))
            top[0].markdown(f"**{goal['title']}**")
            top[1].markdown(f"`{goal['target']}`")
            st.caption(goal["detail"])
            check(f"goal_{goal['id']}", "On track today")

    st.divider()
    st.subheader("Rules of the house")
    for rule in RULES:
        st.markdown(f"- {rule}")

with shop_tab:
    st.subheader("Buy once, cook the week")
    st.caption("Quantities are per cooked meal. Add rice, dal, eggs, curd, and chicken first — those run out.")
    groc = grocery_list()
    query = st.text_input("Filter items", placeholder="paneer, whey, chicken…")
    shown = 0
    for item, uses in groc.items():
        if query and query.lower() not in item.lower():
            continue
        shown += 1
        with st.expander(f"{item} · used {len(uses)} times"):
            for use in uses:
                st.write(f"- {use}")
    if shown == 0:
        st.warning("Nothing matches that filter. Clear the search.")

st.markdown(
    '<p class="footer-note">Hardcoded for Aditya. Not medical advice. '
    "Change meals, times, or targets in plan.py — the dashboard has no database.</p>",
    unsafe_allow_html=True,
)
