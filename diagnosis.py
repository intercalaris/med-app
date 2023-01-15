from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from transformers import TFBertForSequenceClassification, AdamW, BertConfig
from load_data import fetch_data, preprocess_data

# Load BERT model
model = TFBertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# set optimizer
optimizer = tf.keras.optimizers.Adam(learning_rate=2e-5)

data = fetch_data("query")
data = preprocess_data(data)

X_train, X_test, y_train, y_test = train_test_split(data['description'], data['diagnosis'], test_size=0.2, random_state=42)


# Create a neural network model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y)

# make predictions on the test set
y_pred = model.predict(X_test,batch_size=32)

# round predictions to the nearest class
y_pred = np.round(y_pred)

# evaluate the model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy: {:.2f}".format(acc))
print("Precision: {:.2f}".format(prec))
print("Recall: {:.2f}".format(rec))
print("F1-score: {:.2f}".format(f1))

