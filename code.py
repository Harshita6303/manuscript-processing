#LRModel
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

#Load the cleaned text files and assign labels based on the folder structure
def load_cleaned_texts_with_labels(folder_paths):
    texts = []
    labels = []
    
    # Loop over each folder path provided
    for folder_path in folder_paths:
        folder_name = os.path.basename(folder_path)  # Get the folder name (e.g., cleanedtext1616)
        label = folder_name[-4:]  # Extract the year from the folder name (e.g., 1616 -> 1600, etc.)
        
        # Load all text files in this folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            # Read the cleaned text from each file
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                texts.append(text)
                labels.append(label)
    
    return texts, labels

#Define the folder paths
cleaned_text_folders = [
    r'C:\Users\harsh\OneDrive\Pictures\manuscript\cleanedtext-2-1600',
    r'C:\Users\harsh\OneDrive\Pictures\manuscript\cleanedtext-2-1700',
    r'C:\Users\harsh\OneDrive\Pictures\manuscript\cleanedtext-2-1800',
    r'C:\Users\harsh\OneDrive\Pictures\manuscript\cleanedtext-2-1900'
]

#Load the cleaned text and labels
texts, labels = load_cleaned_texts_with_labels(cleaned_text_folders)

#Create a DataFrame for easier manipulation
data = pd.DataFrame({
    'text': texts,
    'label': labels
})

#Feature Extraction using TF-IDF
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000)  # Using bigrams for richer features
X = vectorizer.fit_transform(data['text'])
y = data['label']

#Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train the model (Logistic Regression used here)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

#Evaluate the model on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Classification Report:\n", classification_report(y_test, y_pred))

#Predicting on new data
def predict_period(text):
    # Clean and transform the input text
    vectorized_text = vectorizer.transform([text])
    predicted_label = model.predict(vectorized_text)
    return predicted_label

# Example usage:
new_text = "hast"
predicted_label = predict_period(new_text)
print(f"Predicted Period: {predicted_label[0]}")
