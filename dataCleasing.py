import os
import pandas as pd

def clean_titanic_dataset(csv_path):
    df = pd.read_csv(csv_path)

    # Drop columns with too many missing values
    if 'Cabin' in df.columns:
        df.drop(columns=['Cabin'], inplace=True)

    # Fill missing 'Age' values with the median
    df['Age'].fillna(df['Age'].median(), inplace=True)

    # Fill missing 'Embarked' values with the mode
    if 'Embarked' in df.columns:
        df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    # Strip extra spaces from names
    if 'Name' in df.columns:
        df['Name'] = df['Name'].str.strip()

    # Standardize string columns to lowercase
    if 'Sex' in df.columns:
        df['Sex'] = df['Sex'].str.lower()
    if 'Embarked' in df.columns:
        df['Embarked'] = df['Embarked'].str.lower()

    # Show remaining null values
    print("Null values after cleaning:")
    print(df.isnull().sum())

    # Show first rows of cleaned dataset
    print("\nFirst cleaned rows:")
    print(df.head())

    # Save the cleaned dataset
    clean_csv_path = os.path.join(os.path.dirname(csv_path), 'Titanic-Dataset-Cleaned.csv')
    df.to_csv(clean_csv_path, index=False)
    print(f"\n✅ Cleaned dataset saved at: {clean_csv_path}")

    return clean_csv_path
