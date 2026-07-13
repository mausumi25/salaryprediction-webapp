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

print("\nShape before cleaning:", df.shape)

print("\nMissing Values")
print(df.isnull().sum())