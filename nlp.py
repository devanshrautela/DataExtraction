import nltk

nltk.download('stopwords')

# Read in the text file
with open("cancer.txt", "r") as file:
    text = file.read()

# Preprocess the text data by removing stop words and punctuation
stop_words = set(nltk.corpus.stopwords.words("english"))
words = nltk.word_tokenize(text)
words = [word for word in words if word.lower() not in stop_words and word.isalpha()]

# Apply POS tagging
pos_tags = nltk.pos_tag(words)

# Apply NER
ne_tags = nltk.ne_chunk(pos_tags)

# Apply dependency parsing
dependency_parser = nltk.parse.dependency.DependencyGraph.from_sentence(text)
dependency_tree = dependency_parser.tree()

# Extract relevant text data
keywords = [word for (word, tag) in pos_tags if tag.startswith("N")]
phrases = nltk.bigrams(words)

# Postprocess the extracted text data
keywords = list(set(keywords))
phrases = list(set([" ".join(phrase) for phrase in phrases]))

# Print the output
print("Keywords:", keywords)
print("Phrases:", phrases)
