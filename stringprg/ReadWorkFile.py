import docx
doc = docx.opendocx('C:/Users/Admin/PycharmProjects/Test/Test_File.docx')
all_data = docx.getdocumenttext(doc)
print(all_data)

with open('C:/Users/Admin/PycharmProjects/Test/test.txt') as file:
    text = file.read()
    print(text)
