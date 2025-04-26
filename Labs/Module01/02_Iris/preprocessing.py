import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
def load_data():
    iris = load_iris()
    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    data['target'] = iris.target
    return data

# Preprocess the data
def preprocess_data(data):
    # Add a new feature: the ratio of sepal to petal length
    data['sepal_petal_ratio'] = data['sepal length (cm)'] / data['petal length (cm)']

    # Standardize features (exclude the 'target' column and 'sepal_petal_ratio')
    scaler = StandardScaler()
    features = data.drop(columns=['target', 'sepal_petal_ratio'])  # Don't scale the ratio feature
    data[features.columns] = scaler.fit_transform(features)  # Apply scaling to only features

    # Ensure that the target variable is of type integer (it's categorical)
    data['target'] = data['target'].astype(int)
    return data

if __name__ == "__main__":
    data = load_data()  # Load the Iris data


    data.to_csv("cleaned_data.csv", index=False)  # This file will be ignored in Git
    print("Preprocessed data saved as 'cleaned_data.csv'.")

