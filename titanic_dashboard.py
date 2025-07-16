import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load cleaned dataset with caching
@st.cache_data
def load_data():
    df = pd.read_csv("Titanic-Dataset-Cleaned.csv")
    return df

df = load_data()

# Cache the model training so it happens only once
@st.cache_resource
def train_model(df):
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    df_ml = df[features + ['Survived']].dropna()
    df_ml = pd.get_dummies(df_ml, columns=['Sex', 'Embarked'], drop_first=True)

    X = df_ml.drop('Survived', axis=1)
    y = df_ml['Survived']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return model, accuracy, X_test, y_test, y_pred

model, accuracy, X_test, y_test, y_pred = train_model(df)

# App title
st.title("🚢 Titanic Data Dashboard")
st.markdown("""
This dashboard provides a quick overview of the Titanic passenger dataset, exploring trends related to survival, age, class, and more.
""")

# Survival pie chart
st.subheader("🔵 Survival Distribution")
survival_counts = df['Survived'].value_counts()
labels = ['Did not survive', 'Survived']
fig1, ax1 = plt.subplots()
ax1.pie(survival_counts, labels=labels, autopct='%1.1f%%', startangle=90,
        colors=['salmon', 'lightgreen'])
ax1.axis('equal')
st.pyplot(fig1)
st.markdown("""
Approximately **38%** of passengers survived the Titanic disaster.
""")

# Passenger class vs survival
st.subheader("🏷️ Survival by Passenger Class")
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x='Pclass', hue='Survived', palette='Set2', ax=ax2)
ax2.set_xlabel("Passenger Class")
ax2.set_ylabel("Count")
ax2.set_xticklabels(["1st", "2nd", "3rd"])
ax2.legend(title="Survived", labels=["No", "Yes"])
st.pyplot(fig2)
st.markdown("""
First-class passengers had a much higher chance of survival compared to second and third classes.
""")

# Age distribution
st.subheader("📊 Age Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(df['Age'], bins=30, kde=True, color='skyblue', ax=ax3)
ax3.set_title("Distribution of Passenger Ages")
ax3.set_xlabel("Age")
st.pyplot(fig3)
st.markdown("""
Most passengers were between **20 and 40 years old**.
""")

# Machine Learning Prediction Section
st.header("🤖 Survival Prediction with Machine Learning")

st.write(f"Model Accuracy on test data: **{accuracy:.2%}**")

# Show some predictions side by side
st.subheader("Sample Predictions")
sample_df = X_test.copy()
sample_df['Actual Survival'] = y_test.values
sample_df['Predicted Survival'] = y_pred

# Map 0/1 to text
sample_df['Actual Survival'] = sample_df['Actual Survival'].map({0: 'No', 1: 'Yes'})
sample_df['Predicted Survival'] = sample_df['Predicted Survival'].map({0: 'No', 1: 'Yes'})

st.dataframe(sample_df.head(10))

st.markdown("---")
st.markdown("""
[🔗 LinkedIn](https://www.linkedin.com/in/lucasg-romao/) | [🐙 GitHub](https://github.com/lucasromaodev)
""")
