import pandas as pd
import matplotlib.pyplot as plt

#file_path='survey_data_with_duplicate.csv'

file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv"
df = pd.read_csv(file_path)

print(df.info())
print()
# checking missing value
print('Missing value in CodingActivities: ',df['CodingActivities'].isnull().sum())
# Filling missing value (forward value)
df['CodingActivities'] = df['CodingActivities'].ffill()
# verifying missing value after filling them
print('Missing value in CodingActivities: ',df['CodingActivities'].isnull().sum())
print()
# Compensation Value

# checking empty value in column
print('Missing value in ConvertedCompYearly: ',df['ConvertedCompYearly'].isnull().sum())

# filling empty compensation value with column median value

df['ConvertedCompYearly'] = df['ConvertedCompYearly'].fillna(
    df['ConvertedCompYearly'].median()
)

# verifying filling
print('Verify column value: ',df['ConvertedCompYearly'].isnull().sum())
print()

# Normalize ConvertedCompYearly using Min-Max Scaling.
min_val =  df['ConvertedCompYearly'].min()
max_val = df['ConvertedCompYearly'].max()
df['ConvertedCompYearly_MinMax'] = ((df['ConvertedCompYearly'] - min_val) /
                                    (max_val - min_val))

# Z-Score Normalization
mean_val = df['ConvertedCompYearly_MinMax'].mean()
std_val = df['ConvertedCompYearly_MinMax'].std()

df['ConvertedCompYearly_Zscore']=(
    (df['ConvertedCompYearly'] - mean_val) /
    std_val
)

# Visualization of Normalized Data

# Histogram – Original Salary
plt.figure()
plt.hist(df['ConvertedCompYearly'], bins=50)
plt.title("Original ConvertedCompYearly Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# Histogram – Min-Max Normalized
plt.figure()
plt.hist(df['ConvertedCompYearly_MinMax'], bins=50)
plt.title("Min-Max Normalized Distribution")
plt.xlabel("Min-Max Normalized Salary")
plt.ylabel("Frequency")
plt.show()

# Histogram – Z-Score Normalized
plt.figure()
plt.hist(df['ConvertedCompYearly_Zscore'], bins=50)
plt.title("Z-score Normalized Distribution")
plt.xlabel("Z-score")
plt.ylabel("Frequency")
plt.show()
