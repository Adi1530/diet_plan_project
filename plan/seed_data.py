"""The only place numbers live. Treat this as the database."""

from datetime import date


class SeedData:
    """Hardcoded rows for Aditya's cut through 30 Dec 2026."""

    name = "Aditya"
    plan_title = "Cut to 30 Dec"
    tagline = (
        "Count every food. Rice spoons come down each week, then the plate holds at 2,000 kcal."
    )
    goal = (
        "Land between 92 and 94 kg by 30 Dec 2026, and keep the main lifting loads while the weight comes down."
    )
    starts = date(2026, 9, 23)
    ends = date(2026, 12, 30)
    goal_date = date(2026, 12, 13)
    week_count = 14

    height_cm = 190.5
    weight_kg = 99.3
    fat_kg = 25.5
    skeletal_muscle_kg = 40.2
    fat_free_kg = 73.8
    body_water_kg = 54.0
    bmr_kcal = 1964

    steps_low = 8000
    steps_high = 10000
    sleep_low_hours = 7
    sleep_high_hours = 9
    fast_loss_kg_per_week = 0.8

    # Wednesday and Sunday lunch uses chicken and 2 fewer rice spoons.
    high_protein_days = ("Wednesday", "Sunday")
    high_day_fewer_rice_spoons = 2

    # name, unit, kcal, protein grams, fat grams
    foods = (
        ("Egg", "piece", 70, 6, 5),
        ("Idli", "piece", 60, 2, 0.5),
        ("Dosa", "piece", 120, 3, 3),
        ("Rice", "spoon", 65, 1, 0),
        ("Curd", "spoon", 25, 1.5, 1),
        ("Sambar", "spoon", 20, 1, 0.5),
        ("Vegetables", "spoon", 25, 0.5, 0.5),
        ("Dal", "spoon", 45, 3, 0.5),
        ("Chicken", "spoon", 65, 10, 1.5),
        ("Paneer", "piece", 55, 4, 4),
        ("Milk", "tumbler", 150, 8, 5),
        ("Banana", "piece", 90, 1, 0),
        ("Oil", "teaspoon", 40, 0, 4.5),
    )

    spoon_guide = (
        "One rice spoon is one heaped serving spoon of cooked rice, about 50 g.",
        "Idli and dosa are whole pieces. One dosa replaces two idli.",
        "Curd, sambar, dal, vegetables, and chicken use the same heaped serving spoon.",
        "One paneer piece is a small cube, about 20 g. One tumbler of milk is 250 ml.",
    )

    breakfast = (
        ("Egg", 3),
        ("Idli", 2),
        ("Sambar", 2),
        ("Curd", 3),
    )
    breakfast_note = "One plain dosa can replace the two idli."

    ordinary_lunch = (
        ("Dal", 2),
        ("Vegetables", 2),
        ("Sambar", 1),
    )
    high_lunch = (
        ("Chicken", 3),
        ("Vegetables", 2),
        ("Sambar", 1),
    )
    high_lunch_note = "Fish can replace the chicken, spoon for spoon."

    evening = (
        ("Milk", 1),
        ("Banana", 1),
    )
    dinner = (
        ("Vegetables", 2),
        ("Paneer", 2),
        ("Curd", 2),
    )

    # Week 1 starts at 10 lunch spoons and 9 dinner spoons.
    # One spoon comes off each week. From week 7 the plate holds, and oil drops to 1 teaspoon.
    weeks = (
        (10, 9, 2),
        (10, 8, 2),
        (9, 8, 2),
        (9, 7, 2),
        (8, 7, 2),
        (8, 6, 2),
        (8, 6, 1),
        (8, 6, 1),
        (8, 6, 1),
        (8, 6, 1),
        (8, 6, 1),
        (8, 6, 1),
        (8, 6, 1),
        (8, 6, 1),
    )

    # weekday, name, kind, minutes, place, exercises
    sessions = (
        (
            "Monday",
            "Upper body",
            "Lift",
            55,
            "Gym",
            (
                "Bench press — 3 × 6–10",
                "Lat pulldown or pull-ups — 3 × 8–12",
                "Incline dumbbell press — 3 × 8–12",
                "Seated cable row — 3 × 8–12",
                "Lateral raises — 3 × 12–15",
                "Biceps curl — 2 × 10–15",
                "Triceps pushdown — 2 × 10–15",
            ),
        ),
        (
            "Tuesday",
            "Lower body",
            "Lift",
            55,
            "Gym",
            (
                "Squat or leg press — 3 × 6–10",
                "Romanian deadlift — 3 × 8–10",
                "Leg curl — 3 × 10–15",
                "Leg extension — 2 × 10–15",
                "Calf raises — 3 × 10–15",
                "Abs — 3 sets",
            ),
        ),
        (
            "Wednesday",
            "Walk",
            "Easy cardio",
            30,
            "Outside",
            (
                "Rest from weights.",
                "Get the day's 8,000–10,000 steps in.",
                "Optional: 20–30 minutes easy walk if the steps are still short.",
            ),
        ),
        (
            "Thursday",
            "Upper body",
            "Lift",
            55,
            "Gym",
            (
                "Overhead press — 3 × 6–10",
                "Pull-ups or lat pulldown — 3 × 8–12",
                "Chest press — 3 × 8–12",
                "Cable row — 3 × 8–12",
                "Lateral raises — 3 × 12–15",
                "Biceps — 2–3 × 10–15",
                "Triceps — 2–3 × 10–15",
            ),
        ),
        (
            "Friday",
            "Lower body",
            "Lift",
            55,
            "Gym",
            (
                "Leg press or squat — 3 × 8–12",
                "Romanian deadlift — 3 × 8–12",
                "Bulgarian split squat — 2 × 8–12",
                "Leg curl — 3 × 10–15",
                "Calf raises — 3 × 10–15",
                "Abs — 3 sets",
            ),
        ),
        (
            "Saturday",
            "Easy cardio",
            "Easy cardio",
            30,
            "Outside",
            (
                "20–30 minutes easy walk or cycle.",
                "Keep it easy enough to talk.",
                "Still hit 8,000–10,000 steps.",
            ),
        ),
        (
            "Sunday",
            "Walk and recover",
            "Recovery",
            30,
            "Outside",
            (
                "Walk. No lifting.",
                "This is a higher-protein food day.",
                "Lay out Monday's breakfast the night before.",
            ),
        ),
    )

    # date, low kg, high kg. The start row is the scale weight, not a range.
    checkpoints = (
        (date(2026, 9, 23), 99.3, 99.3),
        (date(2026, 9, 30), 98.5, 99.0),
        (date(2026, 10, 15), 97.0, 98.0),
        (date(2026, 10, 31), 96.0, 97.0),
        (date(2026, 11, 15), 95.0, 96.0),
        (date(2026, 11, 30), 94.0, 95.0),
        (date(2026, 12, 15), 93.0, 94.0),
        (date(2026, 12, 30), 92.0, 94.0),
    )

    protein_note = (
        "A normal day lands near 75 g protein. Wednesday and Sunday land near 100 g. "
        "165 g is a later aim, not this plate."
    )

    rules = (
        "Count the plate. Do not guess portions in grams.",
        "Rice is the food that shrinks. Eggs, curd, dal, milk, paneer, and chicken stay put.",
        "From 4 Nov the plate holds: 8 lunch spoons, 6 dinner spoons, 1 teaspoon of oil.",
        "If the 7-day average falls faster than about 0.8 kg in a week, add one rice spoon back.",
        "A sweet replaces food. About 200 kcal of sweet means less rice that day, not food on top.",
        "Weigh every morning after the bathroom, before food or water. Judge the week average, not one morning.",
        "Measure the waist once a week, same spot, same time.",
        "If curls, raises, or leg extensions feel like too much, shorten those before eating less.",
        "This is food and training, not medical advice.",
    )

    avoid = (
        "Do not drop toward 1,600–1,700 kcal to make up for a low-protein day.",
        "Do not take rice off the plate entirely.",
        "Do not add long daily cardio on top of the steps and the four lifting days.",
        "Do not change the plan because three mornings on the scale looked flat.",
    )
