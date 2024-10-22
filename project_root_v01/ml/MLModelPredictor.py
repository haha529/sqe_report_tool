from transformers import pipeline

class MLModelPredictor:
    def __init__(self, model_name="distilbert-base-uncased"):
        self.model = pipeline("text-classification", model=model_name)

    def predict(self, text_data):
        return self.model(text_data)
