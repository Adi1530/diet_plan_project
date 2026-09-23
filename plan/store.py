"""Reads the seed the way a screen would read a database."""

from datetime import date, timedelta

from plan.models import Body, Checkpoint, Food, Session, WeekPlan
from plan.seed_data import SeedData


class PlanStore:
    def __init__(self, seed: SeedData | None = None) -> None:
        self.seed = seed or SeedData()
        self._foods = {
            row[0]: Food(
                name=row[0],
                unit=row[1],
                kcal=row[2],
                protein_g=row[3],
                fat_g=row[4],
            )
            for row in self.seed.foods
        }

    def food(self, name: str) -> Food:
        return self._foods[name]

    def body(self) -> Body:
        seed = self.seed
        return Body(
            height_cm=seed.height_cm,
            weight_kg=seed.weight_kg,
            fat_kg=seed.fat_kg,
            skeletal_muscle_kg=seed.skeletal_muscle_kg,
            fat_free_kg=seed.fat_free_kg,
            body_water_kg=seed.body_water_kg,
            bmr_kcal=seed.bmr_kcal,
        )

    def weekdays(self) -> tuple[str, ...]:
        return tuple(row[0] for row in self.seed.sessions)

    def is_high_protein(self, weekday: str) -> bool:
        return weekday in self.seed.high_protein_days

    def weeks(self) -> tuple[WeekPlan, ...]:
        built = []
        for index, row in enumerate(self.seed.weeks):
            number = index + 1
            starts = self.seed.starts + timedelta(days=7 * index)
            ends = starts + timedelta(days=6)
            if number == self.seed.week_count:
                ends = self.seed.ends
            lunch, dinner, oil = row
            built.append(
                WeekPlan(
                    number=number,
                    starts=starts,
                    ends=ends,
                    lunch_rice_spoons=lunch,
                    dinner_rice_spoons=dinner,
                    oil_teaspoons=oil,
                )
            )
        return tuple(built)

    def week_on(self, day: date) -> WeekPlan:
        weeks = self.weeks()
        if day <= self.seed.starts:
            return weeks[0]
        if day >= self.seed.ends:
            return weeks[-1]
        for week in weeks:
            if week.starts <= day <= week.ends:
                return week
        return weeks[-1]

    def dates_in(self, week: WeekPlan) -> tuple[date, ...]:
        days = []
        cursor = week.starts
        while cursor <= week.ends:
            days.append(cursor)
            cursor += timedelta(days=1)
        return tuple(days)

    def session(self, weekday: str) -> Session:
        for row in self.seed.sessions:
            if row[0] == weekday:
                return Session(
                    weekday=row[0],
                    name=row[1],
                    kind=row[2],
                    minutes=row[3],
                    place=row[4],
                    exercises=row[5],
                )
        raise KeyError(weekday)

    def sessions(self) -> tuple[Session, ...]:
        return tuple(self.session(day) for day in self.weekdays())

    def checkpoints(self) -> tuple[Checkpoint, ...]:
        return tuple(
            Checkpoint(on=row[0], low_kg=row[1], high_kg=row[2])
            for row in self.seed.checkpoints
        )
