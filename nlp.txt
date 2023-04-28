import nltk

nltk.download('punkt')
nltk.download('dependency_treebank')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

from nltk.parse import CoreNLPParser
from nltk.parse.dependencygraph import DependencyGraph

# Read in the text file
with open("cancer.txt", "r", encoding='utf-8') as file:
    text = file.read()

# Split the text into sentences
sentences = nltk.sent_tokenize(text)

# Preprocess the text data by removing stop words and punctuation
stop_words = set(nltk.corpus.stopwords.words("english"))
all_words = []
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    words = [word for word in words if word.lower() not in stop_words and word.isalpha()]
    all_words.extend(words)

# Apply POS tagging to all words
pos_tags = nltk.pos_tag(all_words)

# Apply NER to all words
ne_tags = nltk.ne_chunk(pos_tags)

# Apply dependency parsing to each sentence
dependency_trees = []
for sentence in sentences:
    dependency_parser = CoreNLPParser(url='http://localhost:9000', tagtype='pos,parse,depparse')
    parse = next(dependency_parser.raw_parse(sentence))
    dependency_graph = DependencyGraph(parse.to_conll(10))
    dependency_trees.append(dependency_graph.tree())

# Extract relevant text data
keywords = [word for (word, tag) in pos_tags if tag.startswith("N")]
phrases = nltk.bigrams(all_words)

# Postprocess the extracted text data
keywords = list(set(keywords))
phrases = list(set([" ".join(phrase) for phrase in phrases]))

# Print the output
print("Keywords:", keywords)
print("Phrases:", phrases)
