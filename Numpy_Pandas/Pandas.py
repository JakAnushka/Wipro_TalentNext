'''3.Pandas DataFrame
 Download the data set and rename to cars.csv Link: Dataset: https://www.keggle.com/uciml/autompg dataset/data/select-auto-mpg.csv or https://archive.ics.uci.edu/ml/datasets/Auto-MPG a. Import Pandas b. Import the Cars Dataset and store the Pandas DataFrame in the variable cars c. Inspect the first 10 Bows of the DataFrame cars d. Inspect the Dataframe cars by "printing" cars e. Inspect the last 5 Rows f. Get some meta information on our DataFrame.'''

import pandas as pd


cars = pd.read_csv("cars.csv")

print("First 10 rows:\n", cars.head(10))

print("\nFull DataFrame:\n", cars)

print("\nLast 5 rows:\n", cars.tail())

print("\nInfo:\n")
print(cars.info())

'''4. Download 50 startups dataset Link: https://www.kaggle.com/datasets/farhaned29/50-startups  a. Create DataFrame using Pandas b. Read the data from 50 startups.csv file and load the data into dataframe. c. Check the statistical summary. d. Check for corelation coefficient between dependent and independent variables.'''
import pandas as pd

startups = pd.read_csv("50_Startups.csv")

print("First 5 rows:\n", startups.head())

print("\nStatistical Summary:\n", startups.describe())

print("\nCorrelation Matrix:\n", startups.corr())
