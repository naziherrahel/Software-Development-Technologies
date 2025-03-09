import os  
import joblib
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib
matplotlib.use('Agg')
 
# Create the assets directory if it doesn't exist
os.makedirs("assets", exist_ok=True)
 # Load the Iris dataset
iris = load_iris()
 
 # Split the data into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=42)
 
# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
 
 # Save the trained model to a file
joblib.dump(model, "iris_model.pkl")
 
 # Make predictions
y_pred = model.predict(X_test)
 
 # Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
 
 # Plot confusion matrix
plt.figure(figsize=(8, 6))
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.savefig("assets/confusion_matrix.png")  # Save the plot as an image
plt.close()  # Close the plot to free up memory
 
 # Optionally, you can save other metrics like accuracy, precision, etc.
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")
 
 # You can also save the accuracy to a text file or log it in your report
with open("assets/metrics.txt", "w") as f:
     f.write(f"Model: Random Forest Classifier\n")
     f.write(f"Dataset: Iris\n")
     f.write(f"Accuracy: {accuracy:.2f}\n")