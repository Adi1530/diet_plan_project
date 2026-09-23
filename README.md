# Aditya's cut through 30 Dec 2026

A Streamlit dashboard for one person. Meals are counts (2 idli, 10 spoons of rice), not gram recipes. Calories start near 2,370 and step down to about 2,000 by 4 Nov, then hold through 30 Dec.

## Run it

Windows PowerShell, from this folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt --index-url https://pypi.org/simple
python -m streamlit run app.py --server.port 8517
```

Open [http://127.0.0.1:8517](http://127.0.0.1:8517).

A virtual environment is optional. The app runs on system Python if Streamlit is already installed:

```powershell
python -m streamlit run app.py --server.port 8517
```

## Where the numbers live

`plan/seed_data.py` is the database. Edit that file to change a spoon count, a lift, or a checkpoint.

The rest of `plan/` only reads those rows:

- `models.py` — named records (a serving, a day plate, a week)
- `store.py` — lookups
- `services.py` — builds today's plate, the 14-week ladder, and the grocery counts

`app.py` draws the screen. It does not contain the diet.

## What's on the screen

- **Today** — this week's counted plate and today's session
- **Counted diet** — any weekday, plus the rice-spoon ladder
- **Training** — Monday/Thursday upper, Tuesday/Friday lower, walks on the other days
- **Roadmap** — 99.3 kg toward 92–94 kg by 30 Dec 2026
- **Grocery** — piece and spoon totals for the current week
- **Charts** — morning weight, fat, skeletal muscle, and body water, plotted by date

This is food and training, not medical advice.
