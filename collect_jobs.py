import requests
import json
from datetime import datetime
from pathlib import Path

# =========================
# Configurações
# =========================
API_URL = "https://empllo.com/api/v1"

DATA_KEYWORDS = [
    "developer", "engineer", "programmer", "architect",
    "analyst", "specialist", "consultant",
]
TECH_KEYWORDS= [
    "data", "analytics", "analysis", "statistic", "statistics",
    "machine learning", "ml", "ai", "artificial intelligence",
    "business intelligence", "bi",
]
STACK_KEYWORDS = [
    "software", "system", "platform", "backend", "frontend",
    "fullstack", "api", "cloud", "devops",
]
BUSINESS_KEYWORDS = [
    "software", "system", "platform", "backend", "frontend",
    "fullstack", "api", "cloud", "devops",
]
DESIGN_KEYWORDS = [
    "product", "growth", "marketing", "seo", "crm",
    "operations", "ops", "strategy", "performance",
    "ux", "ui", "designer", "design", "product design",
    "graphic", "visual", "interaction"
]

KEYWORDS = set(
    DATA_KEYWORDS
    + TECH_KEYWORDS
    + STACK_KEYWORDS
    + BUSINESS_KEYWORDS
    + DESIGN_KEYWORDS
)


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# =========================
# Funções
# =========================
def is_relevant(job):
    text = " ".join([
        job.get("title", ""),
        job.get("mainCategory", ""),
        " ".join(job.get("tags", []))
    ]).lower()

    return any(keyword in text for keyword in KEYWORDS)


def fetch_jobs():
    """Busca vagas da API Remotive"""
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()

def filter_jobs(data):
    jobs = data.get("jobs", [])
    filtered = []

    for job in jobs:
        if is_relevant(job):
            filtered.append({
                "title": job.get("title"),
                "company": job.get("companyName"),
                "location": job.get("locations"),
                "salary_min": job.get("minSalary"),
                "salary_max": job.get("maxSalary"),
                "currency": job.get("currency"),
                "seniority_level": job.get("seniorityLevel"),
                "job_type": job.get("jobType"),
                "work_model": job.get("workModel"),
                "tags": job.get("tags"),
                "publication_date": job.get("pubDate"),
                "url": job.get("applicationLink")
            })

    return filtered


            

def save_raw_data(jobs):
    """Salva os dados brutos em JSON"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = RAW_DATA_DIR / f"jobs_raw_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(jobs, f, ensure_ascii=False, indent=2)

    print(f"Data saved in: {file_path}")

# =========================
# Execução
# =========================
def main():
    print("Searching Jobs...")
    data = fetch_jobs()

    print("Filtering tech jobs...")
    filtered_jobs = filter_jobs(data)

    print(f"Total number of job openings collected: {len(filtered_jobs)}")

    save_raw_data(filtered_jobs)

if __name__ == "__main__":
    main()