import pandas as pd

# -----------------------------
# Function to clean YearsCodePro
# -----------------------------
def clean_experience(x):
    if x == "Less than 1 year":
        return 0.5
    if x == "More than 50 years":
        return 50
    return float(x)

# -----------------------------
# Function to group countries
# -----------------------------
def shorten_categories(categories, cutoff):
    category_map = {}

    for category, count in categories.items():
        if count >= cutoff:
            category_map[category] = category
        else:
            category_map[category] = "Other"

    return category_map

# -----------------------------
# Function to clean education
# -----------------------------
def clean_education(x):
    if "Bachelor" in x:
        return "Bachelor's degree"

    if "Master" in x:
        return "Master's degree"

    if "Professional degree" in x:
        return "Post Graduate"

    if "Other doctoral" in x or "Doctoral" in x:
        return "Post Graduate"

    return "Less than a Bachelor's"

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/survey_results_public.csv")

# -----------------------------
# Select Required Columns
# -----------------------------
df = df[
    [
        "Country",
        "EdLevel",
        "YearsCodePro",
        "Employment",
        "ConvertedComp"
    ]
]

# -----------------------------
# Remove Missing Values
# -----------------------------
df = df.dropna()

# -----------------------------
# Keep only full-time employees
# -----------------------------
df = df[df["Employment"] == "Employed full-time"]

# -----------------------------
# Clean YearsCodePro
# -----------------------------
df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)

# -----------------------------
# Clean Country
# -----------------------------
country_map = shorten_categories(df["Country"].value_counts(), 400)
df["Country"] = df["Country"].map(country_map)

# -----------------------------
# Clean Education
# -----------------------------
df["EdLevel"] = df["EdLevel"].apply(clean_education)

# -----------------------------
# Show cleaned data
# -----------------------------
print("\nFirst 5 Rows:\n")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nCountries:")
print(df["Country"].value_counts())

print("\nEducation Levels:")
print(df["EdLevel"].value_counts())