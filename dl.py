import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Input, Embedding, Bidirectional, LSTM, Dense
from tensorflow.keras.models import Model

# Load the data from an Excel file with two columns, 'label' and 'text'
data = pd.read_excel('train.xlsx')
data = data.dropna(subset=['text'])
data['text'] = data['text'].astype(str)
# Split the data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.1, random_state=42)
test_data['label'] = pd.to_numeric(test_data['label'], errors='coerce').fillna(-1).astype(int)
train_data['label'] = train_data['label'].astype(int)
test_data['label'] = test_data['label'].astype(int)
# Define the maximum length of the input sequences and the number of output classes
max_length = 100
num_classes = 1

# Create a tokenizer and fit it on the training data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_data['text'].values)

# Convert the text data to sequences of integers and pad them
train_sequences = tokenizer.texts_to_sequences(train_data['text'].values)
train_padded = pad_sequences(train_sequences, maxlen=max_length, padding='post')

test_sequences = tokenizer.texts_to_sequences(test_data['text'].values)
test_padded = pad_sequences(test_sequences, maxlen=max_length, padding='post')

# Define the deep learning model
inputs = Input(shape=(max_length,))
embedding_layer = Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=100, input_length=max_length)(inputs)
bi_lstm_layer = Bidirectional(LSTM(64, return_sequences=False))(embedding_layer)
output_layer = Dense(num_classes, activation='sigmoid')(bi_lstm_layer)
model = Model(inputs=inputs, outputs=output_layer)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_padded, train_data['label'].values, epochs=8, batch_size=32, validation_data=(test_padded, test_data['label'].values))

# Load the data from a text file
with open('impure_test_unstructured.txt', 'r',encoding='utf-8') as f:
    new_data = f.read().splitlines()

# Convert the text data to sequences of integers and pad them
new_sequences = tokenizer.texts_to_sequences(new_data)
new_padded = pad_sequences(new_sequences, maxlen=max_length, padding='post')

# Make predictions on the new data
predictions = model.predict(new_padded)

# Extract the predictions that are related to cancer and write them to a file
with open('output2.txt', 'w', encoding='utf-8') as f:
    for i in range(len(predictions)):
        if predictions[i] > 0.5:
            f.write(new_data[i] + '\n')
