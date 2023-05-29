import re

# Define regular expression to match cancer-related terms
cancer_regex = re.compile(r'cancer|malignancy', re.IGNORECASE)

# Read in unstructured text data from file
with open('impure_test_unstructured3.txt', 'r',encoding='utf-8') as f:
    text = f.read()



# Apply rules to extract paragraphs containing cancer-related terms
cancer_paragraphs = [p for p in text.split('\n\n') if re.search(cancer_regex, p)]

# Print extracted paragraphs
with open('output.txt', 'w',encoding='utf-8') as f:
   for p in cancer_paragraphs:
        f.write(p + '\n\n')

