import pandas as pd

# Load dataset
df = pd.read_csv("data/survey_results_public.csv")

# Select required columns
df = df[[
    "Country",
    "EdLevel",
    "YearsCodePro",
    "Employment",
    "ConvertedComp"
]]

print("Missing Values:\n")
print(df.isnull().sum())
# Remove rows containing missing values
df = df.dropna()

print("\nShape after removing missing values:")
print(df.shape)
df = df[df["Employment"] == "Employed full-time"]

print("\nShape after filtering full-time employees:")
print(df.shape)
print("\nCleaned Dataset:")
print(df.head())