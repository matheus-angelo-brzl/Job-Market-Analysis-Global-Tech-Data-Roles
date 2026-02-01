# Job-Market-Analysis-Global-Tech-Data-Roles
This project analyzes real-world job postings data to extract insights about the global job market, with a focus on salary distribution, seniority levels, work models, locations, and in-demand skills.  The goal is to demonstrate data analysis, data cleaning, and exploratory data analysis (EDA) skills using Python and Pandas.
Data Overview

Total job postings analyzed: 83

Source: Public job board API

Data format: JSON

Scope: Global positions (remote, hybrid, and on-site)

 Technologies Used

Python

Pandas

Matplotlib

JSON

Pathlib

***Key Analyses & Insights***

  
 ***Top Job Locations***
 
Location	Job Count

Worldwide	15

North America	11

Paris	7

New York	5

London	4

Madrid	4

Europe	3

Málaga	3

San Francisco	3

Tel Aviv	3

 Insight:
Remote-friendly or globally scoped roles (“Worldwide”, “Europe”) represent a significant portion of job openings, reinforcing the growing trend of distributed teams.

 ***Salary Distribution (USD / year)***

Based on 18 postings with available salary ranges:

Metric	Value

Mean	$149,639

Median	$135,000

Min	$41,500

Max	$332,500

75th Percentile	$200,375

 Insight:
The salary distribution shows high variance, indicating a market with strong differentiation based on seniority, specialization, and possibly company size.

  ***Seniority Level Distribution***
  
 Seniority	Job Count
 
Senior	36

Mid	25

Lead	7

Entry level	4

Junior	2

Manager	2

Staff	2

Intern	2

Director	1

VP	1

Principal	1

 Insight:
The market is clearly senior-heavy, suggesting high demand for experienced professionals and a more competitive environment for entry-level candidates.

  ***Average Salary by Seniority***
  
 Seniority	Avg Salary (USD/year)
 
VP	$332,500

Staff	$212,000

Lead	$140,125

Senior	$137,900

Mid	$135,417

Entry level	$86,500

 Insight:
Salary growth accelerates significantly after senior levels, with executive and staff roles commanding a strong premium.

  ***Most In-Demand Skills***
  
 Skill	Job Count
 
Python	21

SQL	17

APIs	13

AI	12

Dashboards 9

FX	8

RPA	7

BI Tools	7

ERP	7

Process Mining	6

 Insight:
The data highlights Python and SQL as core skills, while AI, automation, and business intelligence tools are increasingly relevant across roles.

 ***Project Structure***
project/

├── collect_jobs.py        # Job data collection

├── analyze_jobs.py        # Data analysis and visualization

├── data/

│   ├── raw/               # Raw JSON data

│   └── salary_by_seniority.csv

├── plots/

│   └── salary_by_work_model.png

└── README.md

***How to Run the Project***
pip install pandas matplotlib
python collect_jobs.py
python analyze_jobs.py

***What This Project Demonstrates***

Data ingestion and preprocessing

Exploratory data analysis (EDA)

Aggregations and group-based statistics

Real-world salary analysis

Clean, modular, and readable Python code

Future Improvements

Increase dataset size for stronger statistical significance

Add confidence intervals for salary analysis

Time-based analysis (salary trends over time)

Advanced skill clustering and correlation analysis

Interactive dashboards (e.g., Plotly / Streamlit)

 ***Author***

Matheus Angelo
Aspiring Data Analyst / Statistician
Focused on data-driven insights and real-world problem solving
