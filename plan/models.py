"""Named records. The screens never see raw seed rows."""

from dataclasses import dataclass
from datetime import date


def _grams(value: float) -> str:
    rounded = round(value, 1)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.1f}"


@dataclass(frozen=True)
class Food:
    name: str
    unit: str
    kcal: int
    protein_g: float
    fat_g: float


@dataclass(frozen=True)
class Serving:
    food: Food
    count: int

    @property
    def kcal(self) -> int:
        return self.food.kcal * self.count

    @property
    def protein_g(self) -> float:
        return self.food.protein_g * self.count

    @property
    def fat_g(self) -> float:
        return self.food.fat_g * self.count

    def label(self) -> str:
        count = self.count
        name = self.food.name.lower()
        unit = self.food.unit
        if unit == "spoon":
            word = "spoon" if count == 1 else "spoons"
            return f"{count} {word} {name}"
        if unit == "teaspoon":
            word = "teaspoon" if count == 1 else "teaspoons"
            return f"{count} {word} {name}"
        if unit == "tumbler":
            return f"{count} tumbler {name}"
        if self.food.name == "Egg":
            return "1 egg" if count == 1 else f"{count} eggs"
        if self.food.name == "Paneer":
            word = "piece" if count == 1 else "pieces"
            return f"{count} {word} paneer"
        return f"{count} {name}"


@dataclass(frozen=True)
class Meal:
    name: str
    servings: tuple[Serving, ...]
    note: str = ""

    @property
    def kcal(self) -> int:
        return sum(item.kcal for item in self.servings)

    @property
    def protein_g(self) -> float:
        return sum(item.protein_g for item in self.servings)


@dataclass(frozen=True)
class DayPlate:
    on: date
    weekday: str
    high_protein: bool
    meals: tuple[Meal, ...]

    @property
    def kcal(self) -> int:
        return sum(meal.kcal for meal in self.meals)

    @property
    def protein_g(self) -> float:
        return sum(meal.protein_g for meal in self.meals)

    @property
    def fat_g(self) -> float:
        return sum(item.fat_g for meal in self.meals for item in meal.servings)

    @property
    def carbs_g(self) -> float:
        leftover = self.kcal - (self.protein_g * 4) - (self.fat_g * 9)
        return max(0.0, leftover / 4)

    @property
    def rice_spoons(self) -> int:
        return sum(
            item.count
            for meal in self.meals
            for item in meal.servings
            if item.food.name == "Rice"
        )

    def protein_label(self) -> str:
        return _grams(self.protein_g)

    def carbs_label(self) -> str:
        return _grams(self.carbs_g)

    def fat_label(self) -> str:
        return _grams(self.fat_g)


@dataclass(frozen=True)
class WeekPlan:
    number: int
    starts: date
    ends: date
    lunch_rice_spoons: int
    dinner_rice_spoons: int
    oil_teaspoons: int

    def date_label(self) -> str:
        start = self.starts.strftime("%d %b").lstrip("0")
        end = self.ends.strftime("%d %b").lstrip("0")
        return f"{start} – {end}"


@dataclass(frozen=True)
class Session:
    weekday: str
    name: str
    kind: str
    minutes: int
    place: str
    exercises: tuple[str, ...]


@dataclass(frozen=True)
class Checkpoint:
    on: date
    low_kg: float
    high_kg: float

    def date_label(self) -> str:
        return self.on.strftime("%d %b %Y").lstrip("0")

    def range_label(self) -> str:
        if self.low_kg == self.high_kg:
            return f"{self.low_kg:g} kg"
        return f"{self.low_kg:g}–{self.high_kg:g} kg"


@dataclass(frozen=True)
class Body:
    height_cm: float
    weight_kg: float
    fat_kg: float
    skeletal_muscle_kg: float
    fat_free_kg: float
    body_water_kg: float
    bmr_kcal: int

    @property
    def bmi(self) -> float:
        metres = self.height_cm / 100
        return round(self.weight_kg / (metres * metres), 1)

    @property
    def body_fat_percent(self) -> float:
        return round(self.fat_kg / self.weight_kg * 100, 1)


@dataclass(frozen=True)
class GroceryLine:
    food: str
    amount: str
    detail: str
