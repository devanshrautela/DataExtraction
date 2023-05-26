import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')

# Define cancer-related keywords
keywords = [
    'cancer', 'tumor', 'neoplasm', 'carcinoma', 'metastasis', 'oncology', 'chemotherapy',
    'radiation', 'immunotherapy', 'mutation', 'prognosis', 'stage', 'palliative', 'mammogram',
    'mastectomy', 'lumpectomy', 'her2/neu', 'triple-negative', 'breast', 'carcinoma', 'smoker',
    'bronchoscopy', 'thoracoscopy', 'adenocarcinoma', 'squamous', 'mesothelioma', 'gleason',
    'prostatectomy', 'brachytherapy', 'androgen', 'melanoma', 'basal', 'squamous', 'uv',
    'sunscreen', 'mohs', 'sentinel', 'whipple', 'pancreaticoduodenectomy', 'cholangiopancreatography',
    'neuroendocrine'
]

# Read the txt file
try:
    with open('impure_test_unstructured2.txt', 'r', encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError:
    print("Input file not found.")
    exit(1)

# Tokenize the text into sentences
sentences = nltk.sent_tokenize(text)

# Extract cancer-related sentences using POS tagging and NER
cancer_sentences = []
for sentence in sentences:
    # Tokenize the sentence into words
    words = nltk.word_tokenize(sentence)
    # Perform POS tagging
    tagged_words = nltk.pos_tag(words)
    # Perform NER
    named_entities = nltk.ne_chunk(tagged_words)

    # Check if the sentence contains any cancer-related keywords or named entities
    for keyword in keywords:
        if keyword.lower() in sentence.lower() or any(
            entity.label() == 'ORGANIZATION' and keyword.lower() in entity.leaves()[0][0].lower()
            for entity in named_entities if isinstance(entity, nltk.Tree)
        ):
            cancer_sentences.append(sentence)
            break

# Store the sentences in a new txt file
try:
    with open('output11.txt', 'w', encoding='utf-8') as f:
        for sentence in cancer_sentences:
            f.write(sentence + '\n\n')
except IOError:
    print("Error occurred while writing the output file.")
    exit(1)

print("Extraction completed. The cancer-related sentences have been saved in 'output11.txt'.")
