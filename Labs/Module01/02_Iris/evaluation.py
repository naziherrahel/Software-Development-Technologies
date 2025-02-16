from sklearn.metrics import classification_report
from preprocessing import load_data, preprocess_data
from training import train_model

#evalution the model with more details
def evaluate_model(data, model):
  x = data.drop("target",axis=1)
  y = data["target"]

  predictions = model.predict(x)
  report = classification_report(y, predictions)
  print(report)

if _name_ == "_main_":
  data = load_data()
  data = preprocess_data(data)
  model = train_model(data)
  evaluate_model(data, model)