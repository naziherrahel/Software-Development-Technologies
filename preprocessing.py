import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
def load_data():
    iris = load_iris()
    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    data['target'] = iris.target  # target is already categorical (0, 1, 2)
    return data

# Preprocess the data
def preprocess_data(data):
    # Standardize features (exclude the 'target' column)
    scaler = StandardScaler()
    features = data.drop(columns=['target'])
    data[features.columns] = scaler.fit_transform(features)  # Apply scaling to features

    # Ensure that the target variable is of type integer (it's categorical)
    data['target'] = data['target'].astype(int)
    
    return data

if __name__ == "__main__":
    data = load_data()  # Load the Iris dataset
    data = preprocess_data(data)  # Preprocess the dataset (scaling)
    data.to_csv("cleaned_data.csv", index=False)
    print("Preprocessed data saved as 'cleaned_data.csv'.")

