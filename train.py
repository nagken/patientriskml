import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("data/patient_data.csv")

# Ensure 'readmitted' column exists
if "readmitted" not in df.columns:
    raise ValueError("❌ Column 'readmitted' not found in CSV!")

# Define Features & Target
X = df.drop(columns=["readmitted"])  # Features
y = df["readmitted"]  # Target

# ✅ Ensure 'previous_admissions' is included
expected_features = ['age', 'admission_type', 'diagnosis', 'medications', 'length_of_stay', 'previous_admissions']
for feature in expected_features:
    if feature not in X.columns:
        raise ValueError(f"❌ Feature '{feature}' not found in dataset!")

# Convert categorical variables
X = pd.get_dummies(X, columns=["admission_type", "diagnosis", "medications"])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print(f"✅ Model trained and saved. Features: {list(X.columns)}")
