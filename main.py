from docx import Document
import pandas as pd

document = Document()  # fill filename(or file path) with '' brackets

ser = pd.Series(str)  # Creating empty series, classifying it as a string

# append each paragraph in text as a series
for paragraph in document.paragraphs:
    to_append = paragraph.text
    ser_length = len(ser)
    ser.loc[ser_length] = to_append

print(ser)
