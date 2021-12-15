from ImportEngine import Importer

# pip install -r requirements.txt

print(Importer.parse('./data/cats.docx'))
print(Importer.parse('./data/cats.csv'))
print(Importer.parse('./data/cats.pdf'))
