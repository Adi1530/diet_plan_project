# Aditya's cut-and-strength plan

A Streamlit dashboard with **my** meals, workout times, and weekly goals. No database, no login, no backend. Everything lives in `plan.py`.

## Run it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py --server.port 8517
```

Open [http://127.0.0.1:8517](http://127.0.0.1:8517).

## What's in here

- **Today** — today's plate, today's session, water / steps / sleep checks
- **7-day diet** — Indian-friendly high-protein meals around 2000 kcal and 165g protein
- **Training** — 3 lifts, 2 easy conditioning days, Sunday rest (about 295 minutes)
- **Goals** — the 8-week block
- **Grocery** — a list generated from the week's meals

## Change the plan

Edit `plan.py`. The app only reads that file. Swap a meal id in `WEEK_MENU`, change a workout duration, or rewrite a goal.

## Deploy

Push this repo to GitHub, then deploy on [Streamlit Community Cloud](https://share.streamlit.io):

1. New app → pick this repo
2. Main file: `app.py`
3. Python version: 3.12

This is food and training, not medical advice.
"# diet_plan_project" 
