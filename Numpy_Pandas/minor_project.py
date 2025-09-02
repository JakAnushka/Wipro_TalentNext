import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("datasetExample.csv")

print("First 5 rows:\n", df.head())
print("\nInfo:\n")
print(df.info())
print("\nStatistical Summary:\n", df.describe())

def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

for col in numeric_cols:
    outliers = detect_outliers_iqr(df, col)
    print(f"\nOutliers in column '{col}':")
    print(outliers)

    
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()
