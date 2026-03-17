import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

text_data = [
    "free ticket win",
    "claim money online",
    "how are you",
    "claim your prize"
]

labels = [1, 1, 0, 1]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text_data)

model = LogisticRegression()
model.fit(X, labels)

new_message = "won a free ticket"
new_message_vectorized = vectorizer.transform([new_message])
prediction = model.predict(new_message_vectorized)[0]

if prediction == 1:
  print("Prediction: Spam Message")
else:
  print("Prediction: Normal Message")