document = docx.Document(filename)
docText = '\n\n'.join([
    paragraph.text.encode('utf-8') for paragraph in document.paragraphs
])
print docText