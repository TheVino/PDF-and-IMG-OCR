import easyocr, os
from pdf2image import convert_from_path

path = "C:\\Users\\vini_\\Desktop\\Script\\OCR\\img\\"
dirList = os.listdir(path)
pdfpath = "C:\\Users\\vini_\\Desktop\\Script\\OCR\\pdf\\"
pdfDirList = os.listdir(pdfpath)
n = 1

def printPath(dirList):
    print("Files and directories in '", path, "' :") # prints the directories
    print("These are the files found: " +  str(dirList)) # prints all files
    return

def isTextPresent(imagePath):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(imagePath)
    return len(result) > 0

def printTextPresent(imgPath):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(imgPath)
    for (bbox, text, prob) in result: # this is to remove the coordinates
        print(text)

def convertPDFtoIMG(pdfpath, pdfDirList):
    for pdfFile in pdfDirList:
        print(pdfpath + pdfFile)
        images = convert_from_path(pdfpath + pdfFile)

        for image in images:
            image.save(path + "%s-pagina-%d.jpg" %
                       (pdfFile, images.index(image)),"JPEG")
        
# printPath(dirList)
# print(isTextPresent('img\\noisy.jpg'))
# printTextPresent('img\\noisy.jpg')
convertPDFtoIMG(pdfpath, pdfDirList )