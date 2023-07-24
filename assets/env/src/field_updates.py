with open('../../../assets/data/books_zotero.csv','r') as file:
    filedata = file.read()
    filedata = filedata.replace('Key','Id')
    filedata = filedata.replace('File Attachments','Cover')
    filedata = filedata.replace('Url','Download')
    filedata = filedata.replace('Library Catalog','Library')
with open('../../../assets/data/books_zotero.csv','w') as file:
    file.write(filedata)