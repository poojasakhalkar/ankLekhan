from NumToWordConvertor import NumberToWord
import sys
from docx import Document


def main():
    number = sys.argv [1]
    obj_NumberToWord = NumberToWord()
    value = obj_NumberToWord.getValue(number)
    document = Document()
    p = document.add_paragraph(value)
    document.save('Output.docx')
    return "success"

main()
