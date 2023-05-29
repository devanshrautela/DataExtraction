import pandas as pd

# Read structured data from Excel file
df = pd.read_excel('impure_test_structured.xlsx')


# Extract text from second column as a single unstructured string
text = '\n\n'.join([str(row) for row in df.iloc[:,1]])

# Write unstructured text to file
with open('impure_test_unstructured.txt', 'w',encoding='utf-8') as file:
   file.write(text)
