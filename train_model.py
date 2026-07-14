import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# -------------------------------------------------
# Function to clean YearsCodePro
# -------------------------------------------------
def clean_experience(x):
    if x == "Less than 1 year":
        return 0.5
    elif x == "More than 50 years":
        return 50
    else:
        return float(x)


# -------------------------------------------------
# Function to group countries
# -------------------------------------------------
def shorten_categories(categories, cutoff):
    category_map = {}

    for category, count in categories.items():
        if count >= cutoff:
            category_map[category] = category
        else:
            category_map[category] = "Other"

    return category_map


# -------------------------------------------------
# Function to clean education
# -------------------------------------------------
def clean_education(x):

    if "Bachelor" in x:
        return "Bachelor's degree"

    elif "Master" in x:
        return "Master's degree"

    elif "Professional degree" in x:
        return "Post Graduate"

    elif "Doctoral" in x:
        return "Post Graduate"

    else:
        return "Less than Bachelor's"


# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
print("Loading Dataset...\n")

df = pd.read_csv("data/survey_results_public.csv")

# -------------------------------------------------
# Select Required Columns
# -------------------------------------------------
df = df[
    [
        "Country",
        "EdLevel",
        "YearsCodePro",
        "Employment",
        "ConvertedComp"
    ]
]

print("Shape before cleaning:", df.shape)

# -------------------------------------------------
# Remove Missing Values
# -------------------------------------------------
df = df.dropna()

print("Shape after removing missing values:", df.shape)

# -------------------------------------------------
# Keep only full-time employees
# -------------------------------------------------
df = df[df["Employment"] == "Employed full-time"]

print("Shape after filtering full-time employees:", df.shape)

# -------------------------------------------------
# Clean YearsCodePro
# -------------------------------------------------
df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)

# -------------------------------------------------
# Clean Country
# -------------------------------------------------
country_map = shorten_categories(df["Country"].value_counts(), 400)

df["Country"] = df["Country"].map(country_map)

# -------------------------------------------------
# Clean Education
# -------------------------------------------------
df["EdLevel"] = df["EdLevel"].apply(clean_education)

# -------------------------------------------------
# Remove Employment Column
# -------------------------------------------------
df = df.drop("Employment", axis=1)

print("\nCleaned Dataset")
print(df.head())

print("\nDataset Shape:", df.shape)

# -------------------------------------------------
# Encode Categorical Columns
# -------------------------------------------------
country_encoder = LabelEncoder()
education_encoder = LabelEncoder()

df["Country"] = country_encoder.fit_transform(df["Country"])
df["EdLevel"] = education_encoder.fit_transform(df["EdLevel"])

print("\nEncoded Dataset")
print(df.head())

# -------------------------------------------------
# Features and Target
# -------------------------------------------------
X = df.drop("ConvertedComp", axis=1)

y = df["ConvertedComp"]

# -------------------------------------------------
# Split Dataset
# -------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples :", X_train.shape[0])
print("Testing Samples  :", X_test.shape[0])

# -------------------------------------------------
# Train Model
# -------------------------------------------------
model = DecisionTreeRegressor(random_state=42)

model.fit(X_train, y_train)

print("\nModel Training Completed")

# -------------------------------------------------
# Prediction
# -------------------------------------------------
predictions = model.predict(X_test)

print("\nFirst Five Predictions")
print(predictions[:5])

# -------------------------------------------------
# Evaluation
# -------------------------------------------------
mae = mean_absolute_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print("\nModel Evaluation")
print("-------------------------")
print("Mean Absolute Error :", mae)
print("R2 Score            :", r2)

# -------------------------------------------------
# Save Model
# -------------------------------------------------
data = {
    "model": model,
    "country_encoder": country_encoder,
    "education_encoder": education_encoder
}

joblib.dump(data, "model/saved_steps.pkl")

print("\nModel saved successfully inside model/saved_steps.pkl")