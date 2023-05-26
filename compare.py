from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np

# Read the contents of both files
with open("pure_test_validate.txt",'r',encoding='utf-8') as f:
    text1 = f.read()
    
with open("cancer_sentence.txt",'r',encoding='utf-8') as f:
    text2 = f.read()

# Tokenize the strings into sentences or words
sents1 = sent_tokenize(text1.lower())
sents2 = sent_tokenize(text2.lower())

# Create a set of all the unique words in both texts
word_set = set(sents1 + sents2)

# Create dictionaries to represent the frequency of each word
dict1 = {word:0 for word in word_set}
dict2 = {word:0 for word in word_set}

for sent in sents1:
    dict1[sent] += 1
    
for sent in sents2:
    dict2[sent] += 1

# Convert each dictionary to a bag-of-words representation
bag1 = [dict1[word] for word in word_set]
bag2 = [dict2[word] for word in word_set]

# Calculate cosine similarity between the two bag-of-words representations
X = np.array([bag1, bag2], dtype=object)
cos_sim = cosine_similarity(X)

# Print the cosine similarity as a percentage
print(f"The similarity between the two files is {cos_sim[0][1]*100:.2f}%")
