"""Builds the plate, the week, and the grocery list from the store."""

from datetime import date

from plan.models import DayPlate, GroceryLine, Meal, Serving, WeekPlan
from plan.store import PlanStore


class PlanBook:
    """What the screens ask. They do not read the seed themselves."""

    def __init__(self, store: PlanStore | None = None) -> None:
        self.store = store or PlanStore()

    def week_on(self, day: date) -> WeekPlan:
        return self.store.week_on(day)

    def plate_on(self, day: date) -> DayPlate:
        weekday = day.strftime("%A")
        week = self.store.week_on(day)
        high_protein = self.store.is_high_protein(weekday)
        meals = (
            self._breakfast(),
            self._lunch(week, high_protein),
            self._evening(),
            self._dinner(week),
        )
        return DayPlate(
            on=day,
            weekday=weekday,
            high_protein=high_protein,
            meals=meals,
        )

    def ladder(self) -> tuple[tuple[WeekPlan, DayPlate, DayPlate], ...]:
        """Each week, with a normal day and a Wednesday plate."""
        rows = []
        for week in self.store.weeks():
            normal_day = self._sample_day(week, "Monday")
            high_day = self._sample_day(week, "Wednesday")
            rows.append((week, self.plate_on(normal_day), self.plate_on(high_day)))
        return tuple(rows)

    def grocery(self, week: WeekPlan) -> tuple[GroceryLine, ...]:
        totals: dict[str, int] = {}
        details: dict[str, list[str]] = {}
        for day in self.store.dates_in(week):
            plate = self.plate_on(day)
            for meal in plate.meals:
                for item in meal.servings:
                    totals[item.food.name] = totals.get(item.food.name, 0) + item.count
                    details.setdefault(item.food.name, []).append(
                        f"{plate.weekday[:3]} {meal.name.lower()}: {item.label()}"
                    )
        lines = []
        for name, count in totals.items():
            food = self.store.food(name)
            sample = Serving(food, count)
            lines.append(
                GroceryLine(
                    food=name,
                    amount=sample.label(),
                    detail="; ".join(details[name]),
                )
            )
        lines.sort(key=lambda line: line.food)
        return tuple(lines)

    def _sample_day(self, week: WeekPlan, weekday: str) -> date:
        for day in self.store.dates_in(week):
            if day.strftime("%A") == weekday:
                return day
        return week.starts

    def _breakfast(self) -> Meal:
        return Meal(
            name="Breakfast",
            servings=self._servings(self.store.seed.breakfast),
            note=self.store.seed.breakfast_note,
        )

    def _lunch(self, week: WeekPlan, high_protein: bool) -> Meal:
        rice = week.lunch_rice_spoons
        if high_protein:
            rice -= self.store.seed.high_day_fewer_rice_spoons
        sides = self.store.seed.high_lunch if high_protein else self.store.seed.ordinary_lunch
        note = self.store.seed.high_lunch_note if high_protein else ""
        rows = (("Rice", rice),) + sides
        oil = self._oil(week, "lunch")
        if oil:
            rows = rows + (("Oil", oil),)
        return Meal(name="Lunch", servings=self._servings(rows), note=note)

    def _evening(self) -> Meal:
        return Meal(name="Evening", servings=self._servings(self.store.seed.evening))

    def _dinner(self, week: WeekPlan) -> Meal:
        rows = (("Rice", week.dinner_rice_spoons),) + self.store.seed.dinner
        oil = self._oil(week, "dinner")
        if oil:
            rows = rows + (("Oil", oil),)
        return Meal(name="Dinner", servings=self._servings(rows))

    def _oil(self, week: WeekPlan, meal: str) -> int:
        if meal == "lunch" and week.oil_teaspoons >= 1:
            return 1
        if meal == "dinner" and week.oil_teaspoons >= 2:
            return 1
        return 0

    def _servings(self, rows: tuple[tuple[str, int], ...]) -> tuple[Serving, ...]:
        return tuple(
            Serving(self.store.food(name), count)
            for name, count in rows
            if count > 0
        )
