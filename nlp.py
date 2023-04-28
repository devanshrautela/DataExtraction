import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Read cancer-related keywords from a file
with open('cancer_keywords.txt', 'r', encoding='utf-8') as f:
    keywords = f.read().splitlines()

# Read the txt file
with open('impure_test.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract sentences related to cancer
sentences = nltk.sent_tokenize(text)
cancer_sentences = []
for sentence in sentences:
    if any(keyword in sentence.lower() for keyword in keywords):
        cancer_sentences.append(sentence)

# Store the sentences in a new txt file
with open('cancer_sentences.txt', 'w', encoding='utf-8') as f:
    for sentence in cancer_sentences:
        f.write(sentence + '\n')