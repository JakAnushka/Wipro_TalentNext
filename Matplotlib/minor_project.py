'''Use Case

Diabetes Prediction

Perform Exploratory Data Analysis for the Diabetes Dataset.

Dataset:

Diabetes.csv

The dataset can be downloaded from https://www.kaggle.com/datasets

Perform the following tasks

1. Load the data in the DataFrame

2. Data Pre-processing

3. Handle the Categorical Data

4. Perform Uni-variate Analysis

5. Perform Bi-variate Analysis'''


import pandas as pd


df = pd.read_csv("Diabetes.csv")


print(df.head())
print(df.info())
print(df.describe())
cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols_with_zero] = df[cols_with_zero].replace(0, pd.NA)

df.fillna(df.median(), inplace=True)

print("Duplicates:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

df['Outcome'] = df['Outcome'].astype('category')
import matplotlib.pyplot as plt
import seaborn as sns

df.hist(figsize=(12,10), bins=20, color='skyblue', edgecolor='black')
plt.suptitle("Histograms of Features", fontsize=16)
plt.show()


plt.figure(figsize=(12,8))
sns.boxplot(data=df, palette="Set2")
plt.title("Boxplot of Features")
plt.show()

plt.figure(figsize=(6,5))
sns.countplot(x='Outcome', data=df, palette="pastel")
plt.title("Count of Diabetic vs Non-Diabetic")
plt.show()
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

sns.pairplot(df, hue='Outcome', diag_kind='kde', palette='Set1')
plt.show()

features = ['Glucose', 'BMI', 'Age', 'BloodPressure', 'Insulin', 'SkinThickness']
plt.figure(figsize=(14,10))
for i, feature in enumerate(features, 1):
    plt.subplot(3, 2, i)
    sns.boxplot(x='Outcome', y=feature, data=df, palette="Set3")
    plt.title(f"{feature} vs Outcome")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7,5))
sns.scatterplot(x='Glucose', y='BMI', hue='Outcome', data=df, palette='Set1')
plt.title("Glucose vs BMI by Outcome")
plt.show()
