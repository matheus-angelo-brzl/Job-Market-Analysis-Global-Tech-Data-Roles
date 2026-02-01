import json
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"


# =============================
# LOAD DATA
# =============================
def load_jobs():
    latest_file = sorted(RAW_DATA_DIR.glob("jobs_raw_*.json"))[-1]

    with open(latest_file, "r", encoding="utf-8") as f:
        jobs = json.load(f)

    print(f"Total jobs analyzed: {len(jobs)}\n")
    return jobs


# =============================
# DATAFRAME
# =============================
def create_dataframe(jobs):
    df = pd.DataFrame(jobs)

    df["avg_salary"] = df[["salary_min", "salary_max"]].mean(axis=1)

    return df


# =============================
# ANALYSES
# =============================

def analyze_locations(df):
    locations = df["location"].explode()

    result = (
        locations
        .dropna()
        .value_counts()
        .head(10)
        .to_frame("Job Count")
    )

    print("Top Locations:\n", result, "\n")



def analyze_salary(df):
    desc = (
        df["avg_salary"]
        .dropna()
        .describe()
        .round(0)
        .to_frame("Salary USD")
    )

    print("Salary Distribution:\n", desc, "\n")

def analyze_seniority(df):
    seniority = (
        df["seniority_level"]
        .dropna()
        .value_counts()
        .to_frame("Seniority")
    )

    print("Seniority Level:\n", seniority, "\n")

def salary_by_seniority(df):
    salary_by_level = (
        df.dropna(subset=["seniority_level", "avg_salary"])
        .groupby("seniority_level")["avg_salary"]
        .mean()
        .sort_values(ascending=False)
        .round(0)
        .to_frame("Average Salary (USD/year)")
    )

    salary_by_level.to_csv("data/salary_by_seniority.csv")
    print("Salary By Seniority:\n", salary_by_level, "\n")


def analyze_skills(df):
    df_tags = df.explode("tags").rename(columns={"tags": "skills"})

    highest_demand = (
        df_tags["skills"]
        .value_counts()
        .head(10)
        .rename_axis("Skill")
        .to_frame("Job Count")
    )

    print("Highest Demand Skills:\n", highest_demand, "\n")

    return df_tags


# =============================
# PLOT
# =============================

def plot_salary_by_model(df):
    salary_by_model = (
        df.dropna(subset=["avg_salary"])
        .groupby("work_model")["avg_salary"]
        .mean()
        .sort_values(ascending=False)
    )

    salary_by_model.plot(kind="bar")

    plt.title("Average Salary by Work Model")
    plt.ylabel("Salary (USD)")
    plt.show()


# =============================
# MAIN
# =============================

def main():

    jobs = load_jobs()

    df = create_dataframe(jobs)

    analyze_locations(df)
    analyze_salary(df)
    analyze_seniority(df)
    salary_by_seniority(df)
    df_tags = analyze_skills(df)

    plot_salary_by_model(df)


if __name__ == "__main__":
    main()
