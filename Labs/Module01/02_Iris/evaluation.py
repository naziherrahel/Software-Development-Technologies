from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import pandas as pd
import joblib
import seaborn as sns
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time

def evaluate_model(model, data):
    # Include the same features as in training (no need to drop 'target' again)
    X = data.drop("target", axis=1)
    y = data["target"]

    # Make predictions
    predictions = model.predict(X)

    # Evaluate performance
    acc = accuracy_score(y, predictions)
    f1 = f1_score(y, predictions, average='weighted')
    cm = confusion_matrix(y, predictions)

    # Save confusion matrix as an image file
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='d')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    # Generate a unique filename using the current timestamp
    filename = f'confusion_matrix_{int(time.time())}.png'
    plt.savefig(filename)  # Save the plot as an image
    plt.close()  # Close the plot to avoid unnecessary display

    return acc, f1

if __name__ == "__main__":
    data = pd.read_csv("cleaned_data.csv")  # Read the cleaned data
    model = joblib.load("iris_model.pkl")  # Load the trained model
    acc, f1 = evaluate_model(model, data)  # Evaluate the model on the data
    
    print(f"Accuracy: {acc:.2f}")
    print(f"F1-Score: {f1:.2f}")
