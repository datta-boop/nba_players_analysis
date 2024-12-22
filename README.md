# NBA Players Analysis - Info Architects

## Introduction
The project is an NBA Player Data Analysis Dashboard that uses Power BI, Python, and SQLAlchemy to deliver interactive insights into player performances, college contributions, team dynamics, and physical attributes. Designed with a user-friendly interface, the dashboard allows seamless exploration of data, enabling fans, analysts, and decision-makers to extract valuable insights.

## Project Type
PowerBi Dashboard, using Python and SQL for data transformation

## Deplolyed App
https://drive.google.com/file/d/1Kwj3U946KTisQzESwepIDgZRxjoTj8nI/view?usp=sharing

## Directory Structure
my-app/
├─ python_files/
│  ├─ charts.py
│  ├─ preprocessor.py
│  ├─ main.py
├─ jupyter_notebook_files/
│  ├─ Advanced Metric.ipynb
│  ├─ Cleaned DataSet.ipynb
│  ├─ College Analysis.ipynb
│  ├─ NBAPlayersv.ipynb
│  ├─ Performance Metrics.ipynb

## Video Walkthrough of the project
https://youtu.be/2ORSU-OzMPE

## Features
- Player Insights

Examines individual player statistics, such as career highlights of LeBron James with above-average points, assists, and rebound trends.
Offers a platform for users to analyze any NBA player's performance data comprehensively.

- College Insights

Highlights top-performing collegiate programs like Kentucky and Duke as pipelines for NBA talent.
Tracks the progression of college player statistics over time, aiding teams in identifying the best sources of NBA-ready players.

- Team Insights

Analyzes how individual brilliance contributes to team performance.
Presents metrics like net ratings and shot accuracy to measure team efficiency.

- Physical Insights

Evaluates attributes such as height, weight, and age to uncover performance correlations.
Reveals peak player performance age range (27–32 years), informing management strategies.

- Technical Stack and Approach

- - Python: Efficient data cleaning and preprocessing.
- - SQL & SQLAlchemy: Structured data storage and querying.
- - Power BI: Interactive and impactful visualizations.

- Data Validation and Scalability

- - Cross-checks with official NBA datasets for accuracy.
- - Employs database normalization for scalability and secure data storage.

- Collaborative Workflow

- - Utilized GitHub for version control and milestone-based task prioritization.
- - Addressed feedback effectively, like adding a dedicated page for college insights.
- - This project showcases how analytical tools and structured data approaches can provide a profound understanding of sports performance and dynamics.

## design decisions or assumptions
- Design Decisions
- - Modular Design: Python for preprocessing, SQL for structured storage, and Power BI for interactive dashboards.
  - - Key Insights Focus: Simplified, clear metrics like points, assists, and team ratings for actionable insights.
    - - User-Centric Navigation: Intuitive dashboards with filters for players, colleges, and teams.
      - - Scalability: Grouped ranges and normalized databases to handle data growth efficiently.
        - - Feedback-Driven Enhancements: Added features like college insights based on stakeholder input.
          - - Performance Optimization: Prioritized responsiveness over exhaustive details in visualizations.
                 
- Assumptions
- - Accurate Data: Relied on official NBA datasets for validation.
  - - Stakeholder Relevance: Metrics were selected for analysts, scouts, and managers.
    - - Consistent Trends: Assumed patterns like age-performance correlation hold across updates.
      - - Scalable Design: Built for future data expansions with minimal rework.
        - - User Familiarity: Assumed users understand interactive dashboards.
          - This approach ensured a functional, scalable, and user-focused analysis tool.

## Installation & Getting started
This project demonstrates an end-to-end data analysis workflow, including:

- Data Cleaning:

- - Utilized pandas to preprocess data by handling missing values, duplicates, and standardizing formats.
Data Visualization:

- - Used matplotlib and seaborn to create visualizations for trends and patterns.
SQL Database Integration:

- - Leveraged SQLAlchemy to connect to a MySQL database, ensuring smooth data management.

- Power BI Dashboard:

- - Connected Power BI to the SQL database to create an interactive and insightful dashboard.

- How to Use:

- Python Script:
- - Refer to the script for detailed steps on data cleaning, visualization, and database operations.

- Power BI Connection Instructions:
- - Ensure the SQL database with cleaned data is available.
- - Open Power BI, navigate to Home > Get Data, and select SQL Server.
- - Enter the server name and database details, then click Load to import data for analysis.
- - This streamlined approach integrates Python, SQL, and Power BI to deliver actionable insights effectively.

## Technology Stack
List and provide a brief overview of the technologies used in the project.

- python
- matplotlib.pyplot
- seaborne
- SQL
- SQLAlchemy
- PowerBi
