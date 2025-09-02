# 1. Mall Customers Dataset EDA
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Mall_Customers.csv")
print(df.head())

print(df.info())
print(df.describe())

sns.countplot(x="Gender", data=df)
plt.title("Gender Distribution")
plt.show()

sns.histplot(df["Age"], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()

sns.scatterplot(x="Annual Income (k$)", y="Spending Score (1-100)", hue="Gender", data=df)
plt.title("Annual Income vs Spending Score")
plt.show()

sns.boxplot(x="Gender", y="Spending Score (1-100)", data=df)
plt.title("Spending Score by Gender")
plt.show()

sns.pairplot(df[["Age","Annual Income (k$)","Spending Score (1-100)"]])
plt.show()

'''2. Salary Data EDA'''

df = pd.read_csv("Salary_Data.csv")
print(df.head())

print(df.info())
print(df.describe())

sns.scatterplot(x="YearsExperience", y="Salary", data=df)
plt.title("Experience vs Salary")
plt.show()


sns.regplot(x="YearsExperience", y="Salary", data=df)
plt.title("Experience vs Salary with Regression")
plt.show()

'''3. Social Network Ads Dataset EDA'''

df = pd.read_csv("Social_Network_Ads.csv")
print(df.head())

print(df.info())
print(df.describe())

sns.countplot(x="Gender", data=df)
plt.title("Gender Distribution")
plt.show()

sns.histplot(df["Age"], bins=15, kde=True)
plt.title("Age Distribution")
plt.show()


sns.countplot(x="Purchased", hue="Gender", data=df)
plt.title("Purchase by Gender")
plt.show()


sns.scatterplot(x="Age", y="EstimatedSalary", hue="Purchased", data=df)
plt.title("Age vs Salary (with Purchase)")
plt.show()


sns.boxplot(x="Gender", y="EstimatedSalary", data=df)
plt.title("Salary Distribution by Gender")
plt.show()


