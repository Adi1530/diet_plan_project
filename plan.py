"""Aditya's personal plan. Edit this file — the dashboard reads only from here."""

from datetime import date

NAME = "Aditya"
PLAN_TITLE = "Cut & stay strong"
START_DATE = date(2026, 9, 22)
WEEKS = 8
TAGLINE = "High-protein meals you can cook. Lifts that fit a busy week. No fluff."

PROFILE = {
    "goal": "Drop fat while keeping muscle. Show up 5 days a week. Don't chase perfection.",
    "calories": 2000,
    "protein_g": 165,
    "carbs_g": 190,
    "fat_g": 60,
    "meals_per_day": 4,
    "water_l": 3.0,
    "steps": 8000,
    "sleep_h": 7.0,
    "style": "Indian-friendly, high protein, mostly home-cooked",
    "notes": (
        "Eat the listed meals or swap inside the same slot if calories stay within 150. "
        "If you skip a workout, walk 30 minutes. Don't stack two rest days."
    ),
}

GOALS = [
    {
        "id": "protein",
        "title": "Hit 165g protein",
        "detail": "Every day. If dinner is light, add 1 scoop whey or 200g curd.",
        "target": "7 / 7 days",
        "kind": "daily",
    },
    {
        "id": "training",
        "title": "5 training sessions",
        "detail": "3 lifts + 1 conditioning + 1 walk. Rest is Sunday.",
        "target": "5 / week",
        "kind": "weekly",
    },
    {
        "id": "calories",
        "title": "Land near 2000 kcal",
        "detail": "Window is 1850–2150. Don't go under 1700.",
        "target": "2000 ± 150",
        "kind": "daily",
    },
    {
        "id": "steps",
        "title": "8000 steps",
        "detail": "Walk after lunch or dinner if the watch is short.",
        "target": "8,000 / day",
        "kind": "daily",
    },
    {
        "id": "water",
        "title": "3 litres of water",
        "detail": "Bottle at the desk. Finish one before each meal.",
        "target": "3.0 L",
        "kind": "daily",
    },
    {
        "id": "sleep",
        "title": "In bed by 11:30",
        "detail": "7 hours. No late caffeine after 4pm.",
        "target": "7 hours",
        "kind": "daily",
    },
]

# Compatible with typical Indian kitchen + one or two supermarket items.
MEALS = {
    "breakfast": [
        {
            "id": "egg-roti",
            "name": "Masala omelette + 2 phulka",
            "kcal": 480,
            "p": 32,
            "c": 42,
            "f": 18,
            "minutes": 15,
            "plate": "3-egg omelette with onion, tomato, green chilli. 2 phulka. 1 cup black tea, no sugar.",
            "ingredients": [
                ("Eggs", "3"),
                ("Phulka / roti", "2"),
                ("Onion", "1 small"),
                ("Tomato", "1 small"),
                ("Green chilli", "1"),
                ("Oil", "1 tsp"),
            ],
        },
        {
            "id": "chilla",
            "name": "Moong dal chilla + curd",
            "kcal": 450,
            "p": 30,
            "c": 48,
            "f": 12,
            "minutes": 20,
            "plate": "2 moong dal chillas. 200g plain curd. Pinch of chaat masala. Tea optional.",
            "ingredients": [
                ("Moong dal batter", "1 cup"),
                ("Plain curd", "200 g"),
                ("Onion", "2 tbsp"),
                ("Coriander", "handful"),
                ("Oil", "1 tsp"),
            ],
        },
        {
            "id": "oats-whey",
            "name": "Oats, whey, banana",
            "kcal": 470,
            "p": 38,
            "c": 55,
            "f": 10,
            "minutes": 8,
            "plate": "50g oats cooked in water. 1 scoop whey stirred in off-heat. 1 banana. Cinnamon.",
            "ingredients": [
                ("Rolled oats", "50 g"),
                ("Whey protein", "1 scoop"),
                ("Banana", "1"),
                ("Cinnamon", "pinch"),
            ],
        },
        {
            "id": "poha-egg",
            "name": "Peanut poha + boiled eggs",
            "kcal": 490,
            "p": 28,
            "c": 58,
            "f": 16,
            "minutes": 15,
            "plate": "1.5 cups kanda poha with peanuts. 2 boiled eggs. Lemon.",
            "ingredients": [
                ("Thick poha", "60 g dry"),
                ("Peanuts", "15 g"),
                ("Eggs", "2"),
                ("Onion", "1 small"),
                ("Lemon", "1/2"),
            ],
        },
    ],
    "lunch": [
        {
            "id": "chicken-rice",
            "name": "Chicken curry + rice + salad",
            "kcal": 620,
            "p": 48,
            "c": 62,
            "f": 16,
            "minutes": 30,
            "plate": "150g chicken (cooked weight) in light gravy. 150g cooked rice. Cucumber-onion salad.",
            "ingredients": [
                ("Chicken", "180 g raw"),
                ("Rice", "50 g dry"),
                ("Onion", "1"),
                ("Tomato", "1"),
                ("Cucumber", "1"),
                ("Oil", "1 tsp"),
            ],
        },
        {
            "id": "dal-paneer",
            "name": "Dal tadka + paneer + 2 roti",
            "kcal": 640,
            "p": 38,
            "c": 60,
            "f": 24,
            "minutes": 25,
            "plate": "1.5 cups dal. 80g paneer bhurji. 2 roti. Kachumber.",
            "ingredients": [
                ("Toor / moong dal", "50 g dry"),
                ("Paneer", "80 g"),
                ("Roti", "2"),
                ("Onion", "1"),
                ("Tomato", "1"),
                ("Oil / ghee", "1 tsp"),
            ],
        },
        {
            "id": "fish-rice",
            "name": "Fish fry + rice + curd",
            "kcal": 600,
            "p": 45,
            "c": 58,
            "f": 16,
            "minutes": 25,
            "plate": "150g kingfish or tilapia shallow-fried. 150g rice. 100g curd. Lime.",
            "ingredients": [
                ("Fish fillet", "160 g"),
                ("Rice", "50 g dry"),
                ("Curd", "100 g"),
                ("Oil", "1 tsp"),
                ("Lime", "1"),
            ],
        },
        {
            "id": "egg-bhurji-rice",
            "name": "Egg bhurji + jeera rice",
            "kcal": 610,
            "p": 36,
            "c": 58,
            "f": 22,
            "minutes": 20,
            "plate": "3-egg bhurji. 150g jeera rice. Side salad. Green chutney.",
            "ingredients": [
                ("Eggs", "3"),
                ("Rice", "50 g dry"),
                ("Onion", "1"),
                ("Tomato", "1"),
                ("Cumin", "1/2 tsp"),
                ("Oil", "1 tsp"),
            ],
        },
    ],
    "dinner": [
        {
            "id": "grilled-chicken",
            "name": "Tandoori chicken + salad + curd",
            "kcal": 520,
            "p": 52,
            "c": 18,
            "f": 22,
            "minutes": 25,
            "plate": "180g tandoori / grilled chicken. Big salad. 150g curd. No roti tonight.",
            "ingredients": [
                ("Chicken", "200 g raw"),
                ("Hung curd marinade", "2 tbsp"),
                ("Mixed salad", "2 cups"),
                ("Plain curd", "150 g"),
            ],
        },
        {
            "id": "paneer-veg",
            "name": "Palak paneer + 1 roti + salad",
            "kcal": 540,
            "p": 32,
            "c": 28,
            "f": 32,
            "minutes": 25,
            "plate": "100g paneer in palak. 1 phulka. Salad bowl. Keep the gravy light.",
            "ingredients": [
                ("Paneer", "100 g"),
                ("Spinach", "2 cups"),
                ("Phulka", "1"),
                ("Garlic", "2 cloves"),
                ("Oil", "1 tsp"),
            ],
        },
        {
            "id": "egg-curry-veg",
            "name": "Egg curry + mixed veg",
            "kcal": 500,
            "p": 34,
            "c": 22,
            "f": 28,
            "minutes": 25,
            "plate": "3 eggs in thin masala. 1.5 cups lauki / beans / cabbage. No rice.",
            "ingredients": [
                ("Eggs", "3"),
                ("Mixed vegetables", "2 cups"),
                ("Onion", "1"),
                ("Tomato", "1"),
                ("Oil", "1 tsp"),
            ],
        },
        {
            "id": "sprouts-chicken",
            "name": "Chicken stir-fry + sprouts",
            "kcal": 510,
            "p": 50,
            "c": 24,
            "f": 18,
            "minutes": 20,
            "plate": "150g chicken strips. 1 cup boiled moong sprouts. Capsicum, onion, soya.",
            "ingredients": [
                ("Chicken", "170 g raw"),
                ("Moong sprouts", "1 cup"),
                ("Capsicum", "1"),
                ("Onion", "1"),
                ("Soya sauce", "1 tsp"),
            ],
        },
    ],
    "snack": [
        {
            "id": "curd-fruit",
            "name": "Curd + papaya",
            "kcal": 220,
            "p": 14,
            "c": 28,
            "f": 5,
            "minutes": 3,
            "plate": "200g curd. 1 cup papaya or guava. No sugar.",
            "ingredients": [
                ("Plain curd", "200 g"),
                ("Papaya or guava", "1 cup"),
            ],
        },
        {
            "id": "whey-nuts",
            "name": "Whey shake + 8 almonds",
            "kcal": 250,
            "p": 26,
            "c": 8,
            "f": 10,
            "minutes": 3,
            "plate": "1 scoop whey in water. 8 almonds. Drink after training if that's today.",
            "ingredients": [
                ("Whey protein", "1 scoop"),
                ("Almonds", "8"),
            ],
        },
        {
            "id": "buttermilk-sprouts",
            "name": "Chaas + sprouts chaat",
            "kcal": 210,
            "p": 16,
            "c": 26,
            "f": 4,
            "minutes": 8,
            "plate": "1 glass salted chaas. 1 cup sprouts with onion, tomato, lemon.",
            "ingredients": [
                ("Chaas / buttermilk", "300 ml"),
                ("Sprouts", "1 cup"),
                ("Onion", "2 tbsp"),
                ("Lemon", "1/2"),
            ],
        },
        {
            "id": "peanut-apple",
            "name": "Apple + peanut butter",
            "kcal": 230,
            "p": 6,
            "c": 28,
            "f": 12,
            "minutes": 2,
            "plate": "1 apple. 1 tbsp peanut butter. Only on heavier training days.",
            "ingredients": [
                ("Apple", "1"),
                ("Peanut butter", "1 tbsp"),
            ],
        },
    ],
}

# One meal from each slot per weekday. Rotates so the week isn't copy-paste.
WEEK_MENU = {
    "Monday": {
        "breakfast": "egg-roti",
        "lunch": "chicken-rice",
        "snack": "whey-nuts",
        "dinner": "grilled-chicken",
    },
    "Tuesday": {
        "breakfast": "chilla",
        "lunch": "dal-paneer",
        "snack": "curd-fruit",
        "dinner": "paneer-veg",
    },
    "Wednesday": {
        "breakfast": "oats-whey",
        "lunch": "fish-rice",
        "snack": "buttermilk-sprouts",
        "dinner": "egg-curry-veg",
    },
    "Thursday": {
        "breakfast": "poha-egg",
        "lunch": "egg-bhurji-rice",
        "snack": "whey-nuts",
        "dinner": "sprouts-chicken",
    },
    "Friday": {
        "breakfast": "egg-roti",
        "lunch": "chicken-rice",
        "snack": "curd-fruit",
        "dinner": "paneer-veg",
    },
    "Saturday": {
        "breakfast": "chilla",
        "lunch": "dal-paneer",
        "snack": "peanut-apple",
        "dinner": "grilled-chicken",
    },
    "Sunday": {
        "breakfast": "oats-whey",
        "lunch": "fish-rice",
        "snack": "buttermilk-sprouts",
        "dinner": "egg-curry-veg",
    },
}

WORKOUTS = {
    "Monday": {
        "name": "Push — chest, shoulders, triceps",
        "kind": "Lift",
        "minutes": 50,
        "place": "Gym",
        "blocks": [
            "Barbell bench — 4 x 6–8",
            "Dumbbell shoulder press — 3 x 8–10",
            "Incline dumbbell press — 3 x 10",
            "Lateral raises — 3 x 15",
            "Tricep pushdown — 3 x 12",
            "Optional: 5 min easy bike cooldown",
        ],
    },
    "Tuesday": {
        "name": "Pull — back and biceps",
        "kind": "Lift",
        "minutes": 50,
        "place": "Gym",
        "blocks": [
            "Lat pulldown or pull-ups — 4 x 8",
            "Chest-supported row — 4 x 8–10",
            "Seated cable row — 3 x 10",
            "Face pulls — 3 x 15",
            "EZ bar curl — 3 x 10",
            "Hammer curl — 2 x 12",
        ],
    },
    "Wednesday": {
        "name": "Zone-2 walk + core",
        "kind": "Conditioning",
        "minutes": 35,
        "place": "Outside / home",
        "blocks": [
            "Brisk walk 25 min — you can talk, but not sing",
            "Dead bug — 3 x 8/side",
            "Side plank — 3 x 30s/side",
            "Bird dog — 3 x 8/side",
        ],
    },
    "Thursday": {
        "name": "Legs",
        "kind": "Lift",
        "minutes": 55,
        "place": "Gym",
        "blocks": [
            "Goblet or back squat — 4 x 6–8",
            "Romanian deadlift — 4 x 8",
            "Walking lunges — 3 x 10/leg",
            "Leg curl — 3 x 12",
            "Calf raise — 3 x 15",
            "Easy walk 5 min after",
        ],
    },
    "Friday": {
        "name": "Upper pump + arms",
        "kind": "Lift",
        "minutes": 45,
        "place": "Gym",
        "blocks": [
            "Machine chest press — 3 x 10",
            "Seated row — 3 x 10",
            "Arnold press — 3 x 10",
            "Cable fly — 2 x 15",
            "Bicep curl + tricep overhead — 3 supersets of 12",
        ],
    },
    "Saturday": {
        "name": "Long easy walk or cycle",
        "kind": "Conditioning",
        "minutes": 40,
        "place": "Outside",
        "blocks": [
            "40 min zone-2. Keep heart rate conversational.",
            "If raining: incline treadmill 3.5–4.5 km/h, 6–8% grade.",
        ],
    },
    "Sunday": {
        "name": "Rest and mobility",
        "kind": "Rest",
        "minutes": 20,
        "place": "Home",
        "blocks": [
            "No lifting. 20 min stretch or yoga if you want.",
            "Prep dal / chicken for Monday.",
            "In bed by 11:00 tonight.",
        ],
    },
}

RULES = [
    "Cook lunch in the morning or pack leftovers. Don't decide food hungry at 2pm.",
    "Whey is a tool, not a meal. Food first.",
    "Oil is measured — 1 teaspoon per cook, not a free pour.",
    "Eating out: grilled protein + dal + roti. Skip the sweet and the fried starter.",
    "Missed a lift? Do Wednesday's walk. Don't double tomorrow.",
    "This is food and training, not medical advice. If something feels off, see a doctor.",
]

WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def meal_index():
    index = {}
    for slot, meals in MEALS.items():
        for meal in meals:
            index[meal["id"]] = {**meal, "slot": slot}
    return index


def day_meals(weekday: str):
    index = meal_index()
    picks = WEEK_MENU[weekday]
    ordered = []
    for slot in ("breakfast", "lunch", "snack", "dinner"):
        ordered.append(index[picks[slot]])
    return ordered


def day_totals(weekday: str):
    meals = day_meals(weekday)
    return {
        "kcal": sum(m["kcal"] for m in meals),
        "p": sum(m["p"] for m in meals),
        "c": sum(m["c"] for m in meals),
        "f": sum(m["f"] for m in meals),
        "minutes": sum(m["minutes"] for m in meals),
    }


def grocery_list():
    index = meal_index()
    qty = {}
    for weekday in WEEKDAYS:
        for slot, meal_id in WEEK_MENU[weekday].items():
            for name, amount in index[meal_id]["ingredients"]:
                key = name
                if key not in qty:
                    qty[key] = []
                qty[key].append(f"{weekday[:3]} {slot}: {amount}")
    return dict(sorted(qty.items()))


def week_number(today: date | None = None) -> int:
    today = today or date.today()
    delta = (today - START_DATE).days
    if delta < 0:
        return 1
    return min(WEEKS, delta // 7 + 1)
