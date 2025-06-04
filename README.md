## User Analysis Platform
A comprehensive data analysis platform for telecommunications data, focusing on user engagement, experience metrics, and satisfaction analysis. This project provides tools for processing large-scale telecom data, performing advanced analytics, and generating actionable insights.

## 🎯 Project Overview
This platform analyzes three key aspects of telecom user data:

User Engagement: Session counts, duration, and data usage patterns
User Experience: Network performance metrics like TCP retransmission rates and RTT
User Satisfaction: Combined analysis of engagement and experience metrics
## 📁 Project Structure
project/
│
├── scripts/
│   ├── load_data.py           # Database connection and data loading utilities
│   ├── aggregiate_metrics.py  # User metrics aggregation
│   ├── application_analysis.py # Application-specific traffic analysis
│   └── satistfaction_anlysis.py # Satisfaction scoring and analysis
│
├── notebooks/
│   ├── engagement.ipynb       # User engagement analysis
│   ├── EDA.ipynb             # Exploratory Data Analysis
│   ├── experience_visualizations.ipynb # Experience metrics visualization
│   └── satisfaction_anlysis.ipynb     # Satisfaction analysis and clustering
│
├── requirements.txt
├── .env
└── README.md
## 🚀 Key Features
1. Data Loading and Processing
Secure database connection handling
Efficient data loading with PostgreSQL
Data validation and cleaning
Example usage:

from load_data import load_data, connect_to_db

# Connect to database
conn = connect_to_db()

# Load data with custom query
query = """
SELECT 
    "MSISDN/Number" as msisdn,
    COUNT(*) as session_count,
    SUM("Dur. (ms)") as total_duration
FROM xdr_data
GROUP BY "MSISDN/Number"
"""
df = load_data(query)
2. User Metrics Analysis
Session analysis
Traffic pattern identification
Application usage tracking
Example from aggregiate_metrics.py:

def aggregate_user_metrics():
    query = """
    SELECT 
        "MSISDN/Number" as msisdn,
        COUNT(*) as session_count,
        SUM("Dur. (ms)") as total_duration,
        SUM("Total DL (Bytes)") as total_dl,
        SUM("Total UL (Bytes)") as total_ul
    FROM xdr_data
    GROUP BY "MSISDN/Number"
    """
    return load_data(query)
3. Satisfaction Analysis
The SatisfactionAnalyzer class provides comprehensive user satisfaction analysis:

Engagement scoring
Experience evaluation
Cluster analysis
Example usage:

from satistfaction_anlysis import SatisfactionAnalyzer

analyzer = SatisfactionAnalyzer()
engagement_scores = analyzer.calculate_engagement_score(user_metrics)
experience_scores = analyzer.calculate_experience_score(experience_data)
satisfaction_scores = analyzer.calculate_satisfaction_score(
    engagement_scores, 
    experience_scores
)
## 📊 Visualization Examples
The project includes various visualization techniques:

Distribution plots for metrics
Cluster analysis visualizations
Performance comparisons
Example visualization code:

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=df,
    x='engagement_score',
    y='experience_score',
    hue='cluster',
    palette='deep'
)
plt.title('User Segmentation by Engagement and Experience')
plt.show()
🛠️ Setup and Installation
Clone the Repository
git clone https://github.com/alazartefera/fintech-cx.git
cd fintech-cx
Create Virtual Environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Configure Environment Variables Create a .env file with the following:
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=your_port
## 📈 Usage Examples
Basic Data Analysis
from load_data import load_data
from aggregiate_metrics import aggregate_user_metrics

# Get aggregated metrics
metrics_df = aggregate_user_metrics()

# Basic statistics
print(metrics_df.describe())
Satisfaction Analysis
from satistfaction_anlysis import SatisfactionAnalyzer

analyzer = SatisfactionAnalyzer()

# Calculate scores
engagement_scores = analyzer.calculate_engagement_score(metrics_df)
experience_scores = analyzer.calculate_experience_score(experience_df)

# Cluster users
clusters = analyzer.cluster_users(engagement_scores, experience_scores)
## 📝 Requirements
Python 3.10.11 or higher
PostgreSQL database
Required Python packages:
pandas
numpy
scikit-learn
matplotlib
seaborn
psycopg2
python-dotenv
## 🤝 Contributing
Fork the repository
Create your feature branch (git checkout -b feature/...)
Commit your changes (git commit -m 'Addedcommmit message ')
Push to the branch (git push origin feature/...)
Open a Pull Request