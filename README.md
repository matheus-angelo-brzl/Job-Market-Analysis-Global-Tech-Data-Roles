# Global Job Market Analysis – Tech & Data Roles

An end-to-end job market analysis project that collects, processes, and analyzes global tech and data job postings, extracting insights about locations, salaries, seniority levels, work models, and in-demand skills.

This project demonstrates practical skills in Python, data analysis, data cleaning, and exploratory analysis using real-world job market data.

---

## Project Overview

The objective of this project is to analyze the global tech and data job market and answer questions such as:

- Where are tech and data roles most concentrated worldwide?
- What is the salary distribution across the market?
- How does compensation vary by seniority level?
- How do different work models impact salary?
- Which skills are most in demand?

The project follows a realistic data workflow:

- Data collection from a public job API  
- Data filtering and normalization  
- Data analysis using Pandas  
- Statistical summaries and aggregations  
- Data visualization with Matplotlib  
- Exportable insights for further analysis  

---

## Project Structure
The project is organized as follows:
- `data/raw/`: Raw job data collected from the API  
- `plots/`: Generated charts and visualizations  
- `collect_jobs.py`: Job data ingestion and filtering  
- `analyze_jobs.py`: Data analysis and insights generation  


---

## Technologies and Libraries

- Python 3
- Pandas
- Matplotlib
- JSON
- Pathlib

---

## Key Analyses and Results

### Dataset Summary

- Total jobs analyzed: **83**

---

### Top 10 Job Locations

| Location        | Job Count |
|-----------------|-----------|
| Worldwide       | 15 |
| North America   | 11 |
| Paris           | 7 |
| New York        | 5 |
| London          | 4 |
| Madrid          | 4 |
| Europe          | 3 |
| Málaga          | 3 |
| San Francisco   | 3 |
| Tel Aviv        | 3 |

---

### Salary Distribution (USD per year)

| Metric | Value |
|------|------|
| Mean | 149,639 |
| Median | 135,000 |
| Minimum | 41,500 |
| Maximum | 332,500 |
| 75th Percentile | 200,375 |

---

### Seniority Level Distribution

| Seniority | Job Count |
|----------|-----------|
| Senior | 36 |
| Mid | 25 |
| Lead | 7 |
| Entry Level | 4 |
| Junior | 2 |
| Manager | 2 |
| Staff | 2 |
| Intern | 2 |
| Director | 1 |
| VP | 1 |
| Principal | 1 |

---

### Average Salary by Seniority

| Seniority | Average Salary (USD/year) |
|---------|---------------------------|
| VP | 332,500 |
| Staff | 212,000 |
| Lead | 140,125 |
| Senior | 137,900 |
| Mid | 135,417 |
| Entry Level | 86,500 |

---

### Most In-Demand Skills

| Skill | Job Count |
|------|-----------|
| Python | 21 |
| SQL | 17 |
| APIs | 13 |
| AI | 12 |
| Dashboards | 9 |
| FX | 8 |
| RPA | 7 |
| BI Tools | 7 |
| ERP | 7 |
| Process Mining | 6 |

---

## Visualizations

The project generates visualizations such as average salary by work model using Matplotlib, allowing comparison between remote, hybrid, and on-site roles.

---

## How to Run the Project

### Clone the repository
git clone https://github.com/matheus-angelo-brzl/Job-Market-Analysis-Global-Tech-Data-Roles.git
cd Job-Market-Analysis-Global-Tech-Data-Roles

Create and activate a virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Collect job data
python collect_jobs.py

Run the analysis
python analyze_jobs.py

Portfolio Value

This project demonstrates:

Real-world API data ingestion

Data cleaning and normalization

Exploratory data analysis

Statistical reasoning

Modular and readable Python code

Business-oriented insights

It is well suited for roles such as:

Data Analyst

Business Intelligence Analyst

Junior Data Scientist

Analytics Engineer

Future Improvements

Time-series analysis of job postings

Salary comparison by country or region

Currency normalization

Interactive dashboards (Streamlit, Power BI, or Tableau)

Automated data collection and scheduling

Author

Matheus Angelo
GitHub: https://github.com/matheus-angelo-brzl
