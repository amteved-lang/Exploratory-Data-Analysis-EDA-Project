import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")
sns.set(style="whitegrid")

# -----------------------------------
# 1. Create folders
# -----------------------------------
os.makedirs("charts", exist_ok=True)

# -----------------------------------
# 2. Create sample dataset automatically
# -----------------------------------
file_path = "eda_dataset.csv"

if not os.path.exists(file_path):
    np.random.seed(42)
    n = 250

    departments = ["Sales", "HR", "IT", "Finance", "Operations"]
    education_levels = ["Diploma", "Bachelor", "Master", "PhD"]

    df_sample = pd.DataFrame({
        "Employee_ID": range(1001, 1001 + n),
        "Age": np.random.randint(21, 60, n),
        "Department": np.random.choice(departments, n),
        "Education": np.random.choice(education_levels, n),
        "Experience_Years": np.random.randint(0, 25, n),
        "Monthly_Salary": np.random.randint(25000, 120000, n),
        "Working_Hours_Per_Week": np.random.randint(30, 65, n),
        "Performance_Score": np.random.randint(50, 100, n),
        "Projects_Handled": np.random.randint(1, 15, n),
        "Job_Satisfaction": np.random.randint(1, 11, n)
    })

    # Add some missing values
    df_sample.loc[np.random.choice(df_sample.index, 10, replace=False), "Monthly_Salary"] = np.nan
    df_sample.loc[np.random.choice(df_sample.index, 8, replace=False), "Performance_Score"] = np.nan

    # Add some duplicates
    df_sample = pd.concat([df_sample, df_sample.iloc[:5]], ignore_index=True)

    # Add outliers
    df_sample.loc[np.random.choice(df_sample.index, 2, replace=False), "Monthly_Salary"] = 500000
    df_sample.loc[np.random.choice(df_sample.index, 2, replace=False), "Working_Hours_Per_Week"] = 100

    df_sample.to_csv(file_path, index=False)
    print(f"Sample dataset created: {file_path}")

# -----------------------------------
# 3. Load dataset
# -----------------------------------
df = pd.read_csv(file_path)

print("\n========== EXPLORATORY DATA ANALYSIS PROJECT ==========")
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe(include="all"))

# -----------------------------------
# 4. Handle missing values and duplicates for clean analysis
# -----------------------------------
df = df.drop_duplicates().copy()

numeric_cols = df.select_dtypes(include=np.number).columns
categorical_cols = df.select_dtypes(include=["object", "category"]).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

for col in categorical_cols:
    if not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nAfter Cleaning:")
print("Remaining Missing Values:")
print(df.isnull().sum())
print("Remaining Duplicate Rows:", df.duplicated().sum())

# -----------------------------------
# 5. Save cleaned dataset
# -----------------------------------
df.to_csv("eda_cleaned_dataset.csv", index=False)

# -----------------------------------
# 6. Univariate Analysis
# -----------------------------------
print("\n========== UNIVARIATE ANALYSIS ==========")

for col in numeric_cols:
    plt.figure(figsize=(8, 5))
    sns.histplot(df[col], kde=True, bins=20, color="skyblue")
    plt.title(f"Distribution of {col}")
    plt.tight_layout()
    plt.savefig(f"charts/hist_{col}.png", dpi=300)
    plt.show()

for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col], color="orange")
    plt.title(f"Boxplot of {col}")
    plt.tight_layout()
    plt.savefig(f"charts/boxplot_{col}.png", dpi=300)
    plt.show()

for col in categorical_cols:
    plt.figure(figsize=(8, 5))
    sns.countplot(y=df[col], order=df[col].value_counts().index, palette="viridis")
    plt.title(f"Count Plot of {col}")
    plt.tight_layout()
    safe_name = col.replace(" ", "_")
    plt.savefig(f"charts/countplot_{safe_name}.png", dpi=300)
    plt.show()

# -----------------------------------
# 7. Bivariate Analysis
# -----------------------------------
print("\n========== BIVARIATE ANALYSIS ==========")

# Salary vs Experience
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Experience_Years", y="Monthly_Salary", hue="Department")
plt.title("Experience vs Monthly Salary")
plt.tight_layout()
plt.savefig("charts/scatter_experience_salary.png", dpi=300)
plt.show()

# Performance vs Satisfaction
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Job_Satisfaction", y="Performance_Score", hue="Department")
plt.title("Job Satisfaction vs Performance Score")
plt.tight_layout()
plt.savefig("charts/scatter_satisfaction_performance.png", dpi=300)
plt.show()

# Salary by Department
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Department", y="Monthly_Salary", estimator=np.mean, palette="coolwarm")
plt.title("Average Monthly Salary by Department")
plt.tight_layout()
plt.savefig("charts/bar_salary_department.png", dpi=300)
plt.show()

# Performance by Education
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Education", y="Performance_Score", estimator=np.mean, palette="magma")
plt.title("Average Performance Score by Education")
plt.tight_layout()
plt.savefig("charts/bar_performance_education.png", dpi=300)
plt.show()

# -----------------------------------
# 8. Correlation Analysis
# -----------------------------------
print("\n========== CORRELATION ANALYSIS ==========")

corr_matrix = df[numeric_cols].corr()
print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("charts/correlation_heatmap.png", dpi=300)
plt.show()

# Find strong correlations
strong_corr = []
for i in range(len(corr_matrix.columns)):
    for j in range(i + 1, len(corr_matrix.columns)):
        col1 = corr_matrix.columns[i]
        col2 = corr_matrix.columns[j]
        corr_value = corr_matrix.iloc[i, j]
        if abs(corr_value) > 0.5:
            strong_corr.append((col1, col2, corr_value))

print("\nStrong Correlations (|correlation| > 0.5):")
if strong_corr:
    for col1, col2, corr_value in strong_corr:
        print(f"{col1} and {col2}: {corr_value:.2f}")
else:
    print("No strong correlations found.")

# -----------------------------------
# 9. Outlier Detection using IQR
# -----------------------------------
print("\n========== OUTLIER ANALYSIS ==========")

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"{col}: {len(outliers)} outliers detected")

# -----------------------------------
# 10. Generate summary report file
# -----------------------------------
report_lines = []
report_lines.append("EXPLORATORY DATA ANALYSIS REPORT")
report_lines.append("=" * 50)
report_lines.append(f"Dataset Shape: {df.shape}")
report_lines.append(f"Columns: {df.columns.tolist()}")
report_lines.append("\nMissing Values After Cleaning:")
report_lines.append(str(df.isnull().sum()))
report_lines.append("\nDuplicate Rows After Cleaning:")
report_lines.append(str(df.duplicated().sum()))
report_lines.append("\nStatistical Summary:")
report_lines.append(str(df.describe(include='all')))
report_lines.append("\nStrong Correlations:")
if strong_corr:
    for col1, col2, corr_value in strong_corr:
        report_lines.append(f"{col1} and {col2}: {corr_value:.2f}")
else:
    report_lines.append("No strong correlations found.")

with open("eda_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print("\nEDA completed successfully.")
print("Files generated:")
print("- eda_dataset.csv")
print("- eda_cleaned_dataset.csv")
print("- eda_report.txt")
print("- charts/ folder with all graphs")