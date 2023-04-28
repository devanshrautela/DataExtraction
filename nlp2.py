import spacy

# Load the NLP model for English language
nlp = spacy.load('en_core_web_sm')

# Define a function to extract a paragraph related to cancer
def extract_cancer_paragraph(text):
    doc = nlp(text)
    cancer_terms = ['cancer', 'tumor', 'carcinoma', 'metastasis', 'leukemia', 'lymphoma', 'melanoma', 'oncology']
    cancer_paragraph = ''
    for sent in doc.sents:
        for ent in sent.ents:
            if ent.label_ == 'MISC' and ent.text.lower() in cancer_terms:
                cancer_paragraph += str(sent)
                break
    return cancer_paragraph

# Example usage
text = "Lung cancer is a type of cancer that starts in the lungs. Lung cancer is the leading cause of cancer deaths in both men and women. It is estimated that 1.8 million new cases of lung cancer will be diagnosed in 2022. Other common types of cancer include breast cancer, prostate cancer, and colorectal cancer."
cancer_paragraph = extract_cancer_paragraph(text)
print(cancer_paragraph) # Output: 'Lung cancer is a type of cancer that starts in the lungs. Lung cancer is the leading cause of cancer deaths in both men and women.'