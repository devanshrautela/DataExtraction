import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')

# Add more cancer-related keywords
keywords = ['cancer',
'Tumor',
'Neoplasm',
'Carcinoma',
'Metastasis',
'Oncology',
'Chemotherapy',
'Radiation',
'Immunotherapy', 
'mutation',
'Prognosis',
'Stage',
'Palliative',
'Mammogram',
'Mastectomy',
'Lumpectomy',
'HER2/neu',
'Triple-negative'
'breast',
'carcinoma',
'Smoker',
'Bronchoscopy',
'Thoracoscopy',
'Adenocarcinoma',
'Squamous',
'Mesothelioma',
'Gleason',
'prostatectomy',
'Brachytherapy',
'Androgen', 
'Prostatectomy',
'Melanoma',
'Basal',
'Squamous',
'UV',
'Sunscreen',
'Mohs',
'Sentinel',
'Whipple',
'Pancreaticoduodenectomy',  
'cholangiopancreatography', 
'neuroendocrine']

# Read the txt file
with open('impure_test_unstructured3.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract sentences related to cancer
sentences = nltk.sent_tokenize(text)
cancer_sentences = []
for sentence in sentences:
    if any(keyword in sentence.lower() for keyword in keywords):
        cancer_sentences.append(sentence)

# Store the sentences in a new txt file
with open('output1.txt', 'w', encoding='utf-8') as f:
    for sentence in cancer_sentences:
            f.write(sentence + '\n\n')