"""Saved scale readings. One row per date, stored as a local file."""

import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from plan.seed_data import SeedData


@dataclass(frozen=True)
class Measurement:
    on: date
    weight_kg: float
    skeletal_muscle_kg: float
    body_water_kg: float
    fat_kg: float


class MeasurementLog:
    def __init__(self, path: Path | None = None) -> None:
        self.path = path or Path(__file__).resolve().parents[1] / "data" / "measurements.json"

    def all(self) -> tuple[Measurement, ...]:
        if not self.path.exists():
            return ()
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        rows = [
            Measurement(
                on=date.fromisoformat(item["date"]),
                weight_kg=float(item["weight_kg"]),
                skeletal_muscle_kg=float(item["skeletal_muscle_kg"]),
                body_water_kg=float(item["body_water_kg"]),
                fat_kg=float(item["fat_kg"]),
            )
            for item in raw
        ]
        rows.sort(key=lambda row: row.on)
        return tuple(rows)

    def latest(self) -> Measurement | None:
        rows = self.all()
        if not rows:
            return None
        return rows[-1]

    def save(self, reading: Measurement) -> None:
        kept = [row for row in self.all() if row.on != reading.on]
        kept.append(reading)
        kept.sort(key=lambda row: row.on)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = [
            {
                "date": row.on.isoformat(),
                "weight_kg": row.weight_kg,
                "skeletal_muscle_kg": row.skeletal_muscle_kg,
                "body_water_kg": row.body_water_kg,
                "fat_kg": row.fat_kg,
            }
            for row in kept
        ]
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def ensure_opening_reading(self, seed: SeedData) -> None:
        if self.all():
            return
        self.save(
            Measurement(
                on=seed.starts,
                weight_kg=seed.weight_kg,
                skeletal_muscle_kg=seed.skeletal_muscle_kg,
                body_water_kg=seed.body_water_kg,
                fat_kg=seed.fat_kg,
            )
        )
