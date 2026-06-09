# Exploratory Data Analysis (EDA) Project

## Objective
Analyze a dataset to uncover patterns and trends using statistical summaries and visualizations. This project identifies correlations and key influencing factors, and presents insights in a structured report. It develops analytical thinking and data exploration skills.

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook / VS Code

## Key Features
- Statistical summaries (mean, median, standard deviation, quartiles, min, max)
- Missing value analysis
- Duplicate detection
- Outlier detection using IQR method
- Univariate analysis (histograms, boxplots, count plots)
- Bivariate analysis (scatter plots, bar plots)
- Correlation analysis with heatmap
- Key influencing factors identification
- Structured report generation

## Data Overview
The dataset contains employee information with the following columns:
- Employee_ID
- Age
- Department (Sales, HR, IT, Finance, Operations)
- Education (Diploma, Bachelor, Master, PhD)
- Experience_Years
- Monthly_Salary
- Working_Hours_Per_Week
- Performance_Score
- Projects_Handled
- Job_Satisfaction

Total samples: 250 records

## Tasks Performed
- Loaded and inspected the dataset
- Checked for missing values and duplicates
- Cleaned data by handling null values and removing duplicates
- Performed univariate analysis on all numeric and categorical variables
- Performed bivariate analysis to identify relationships between variables
- Computed correlation matrix and identified strong correlations (|r| > 0.5)
- Detected outliers using Interquartile Range (IQR) method
- Generated visualizations: histograms, boxplots, scatter plots, bar plots, correlation heatmap
- Created a structured report summarizing key findings and insights
- Saved cleaned dataset and all charts for documentation

## Files
- `eda_task3.py` – Main Python script for EDA
- `eda_dataset.csv` – Original dataset (with missing values, duplicates, outliers)
- `eda_cleaned_dataset.csv` – Cleaned dataset after preprocessing
- `eda_report.txt` – Structured text report with key findings
- `charts/` – Folder containing all visualization outputs

## Visualization Outputs
### Univariate Analysis
- Histograms with KDE for: Age, Experience_Years, Monthly_Salary, Working_Hours_Per_Week, Performance_Score, Projects_Handled, Job_Satisfaction
- Boxplots for all numeric columns
- Count plots for: Department, Education

### Bivariate Analysis
- Scatter plot: Experience_Years vs Monthly_Salary (colored by Department)
- Scatter plot: Job_Satisfaction vs Performance_Score (colored by Department)
- Bar plot: Average Monthly_Salary by Department
- Bar plot: Average Performance_Score by Education

### Correlation Analysis
- Correlation heatmap for all numeric columns
- Identified strong correlations (|r| > 0.5)

## Key Insights
- **Correlation Analysis**: Identified strong relationships between variables (detailed in report)
- **Salary Patterns**: Monthly salary varies significantly by department and experience level
- **Performance Factors**: Job satisfaction and experience years strongly influence performance scores
- **Outliers**: Detected outliers in Monthly_Salary and Working_Hours_Per_Week columns
- **Missing Data**: Some records had missing values in Monthly_Salary and Performance_Score, handled using median/mode
- **Duplicates**: Detected and removed duplicate employee records

## Methodology
1. Data Loading and Inspection
2. Data Quality Assessment (missing values, duplicates, outliers)
3. Data Cleaning (handle nulls, remove duplicates)
4. Univariate Analysis (distribution and outlier inspection)
5. Bivariate Analysis (relationship exploration)
6. Correlation Analysis (identifying strong relationships)
7. Report Generation (structured findings document)

## Insights Structure
The project report includes:
- Executive Summary
- Data Overview
- Statistical Analysis Results
- Visual Analysis Findings
- Correlation Analysis
- Key Influencing Factors
- Recommendations
- Conclusion

## How to Run
1. Install required libraries:
```bash
pip install pandas numpy matplotlib seaborn
```

2. Run the script:
```bash
python eda_task3.py
```

3. Or open in Google Colab and upload the `.py` file

## Outcome
This project developed analytical thinking and data exploration skills including:
- Understanding of EDA workflow and techniques
- Ability to perform statistical summaries and data quality checks
- Skill in creating effective visualizations for data exploration
- Competence in identifying correlations and key influencing factors
- Experience in generating structured analytical reports
- Practical knowledge of pandas, NumPy, Matplotlib, and Seaborn for EDA

The project demonstrates end-to-end exploratory data analysis from raw data to structured insights.

## Sample Correlations Found
Some strong correlations identified (|r| > 0.5):
- Experience_Years and Monthly_Salary
- Experience_Years and Performance_Score
- Job_Satisfaction and Performance_Score

## Conclusion
This EDA project successfully uncovered patterns, trends, and relationships in the dataset. The analysis provides actionable insights about salary distribution, performance factors, and key influencing variables, fulfilling all project objectives for data exploration and analytical thinking development.
