
import re

# define the regular expressions for identifying cancer-related terms
cancer_regex = re.compile(r"(cancer|tumor|carcinoma|neoplasm|metastasis)")
breast_cancer_regex = re.compile(r"(breast cancer|breast carcinoma)")
lung_cancer_regex = re.compile(r"(lung cancer|lung carcinoma)")

# sample medical text
with open('cancer.txt','r') as f:
    text = "The patient was diagnosed with lung cancer, stage 3. Treatment included chemotherapy and radiation therapy."

# create a dictionary to store the extracted data
data = {}

# check for lung cancer
if lung_cancer_regex.search(text):
    data["cancer_type"] = "lung cancer"
    data["stage"] = 3
    data["treatments"] = ["chemotherapy", "radiation therapy"]
    
print(data)

#deepanshu's code
import re

# Define regular expression to match cancer-related terms
cancer_regex = re.compile(r'cancer|malignancy', re.IGNORECASE)

# Read in unstructured text data from file
with open('impure_test.txt', 'r',encoding='utf-8') as f:
    text = f.read()

# Apply rules to extract paragraphs containing cancer-related terms
cancer_paragraphs = [p for p in text.split('\n\n') if re.search(cancer_regex, p)]

# Print extracted paragraphs
with open('output.txt', 'w',encoding='utf-8') as f:
   for p in cancer_paragraphs:
        f.write(p + '\n\n')

