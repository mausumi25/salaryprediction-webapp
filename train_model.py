import pandas as pd

# Load dataset
df = pd.read_csv("data/survey_results_public.csv")

# Keep only required columns
df = df[
    [
        "Country",
        "EdLevel",
        "YearsCodePro",
        "Employment",
        "ConvertedComp"
    ]
]

print("Selected Columns")
print(df.head())

print("\nShape before cleaning:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())
# Remove rows with missing values
df = df.dropna()

print("\nShape after removing missing values:")
print(df.shape)
print("\nUnique Employment Values:\n")
print(df["Employment"].unique())
# Keep only full-time employees
df = df[df["Employment"] == "Employed full-time"]

print("\nShape after filtering full-time employees:")
print(df.shape)