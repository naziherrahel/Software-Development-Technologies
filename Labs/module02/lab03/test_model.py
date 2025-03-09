# src/test_model.py
import joblib
from sklearn.datasets import load_iris
 
def test_model_accuracy():
     # Load the previously saved model
     model = joblib.load("iris_model.pkl")
     iris = load_iris()
     # Calculate the accuracy on the full dataset
     accuracy = model.score(iris.data, iris.target)
     # Ensure that the accuracy is at least 90%
     assert accuracy >= 0.9, "Model accuracy is too low!"
 
if __name__ == "__main__":
     test_model_accuracy()
     print("Test passed!")