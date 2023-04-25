
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