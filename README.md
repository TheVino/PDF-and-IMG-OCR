# PDF-and-IMG-OCR

Hi! This code can idenfity and read text from images to you and also convert PDF to JPEG to also read the *(just like an OCR).* 



# What libs do I need?
```
 pip install pdf2image
 pip install easyocr
 ```


## Main code has 4 functions

```
def  printPath(*): # to print the path you will be working with

def  isTextPresent(*): # to identify if the file has any text on it

def  printTextPresent(*): # to print the actual letters on the image

def  convertPDFtoIMG(*): # to convert the pdf to image
```

### Hard coded - where you need to inform the path
So just replace these directories with the one you will be using to Convert/ OCR.
```
path 	= "C:\\Users\\vini_\\Desktop\\Script\\OCR\\img\\"
pdfpath = "C:\\Users\\vini_\\Desktop\\Script\\OCR\\pdf\\"
```


> **Tip:** It is better to have **2** separate **folders**, one for images and one for PDF.


## Testing some images! 👨‍💻
```
def  printPath(dirList):
```
**Returns**: 
![printpath](https://i.imgur.com/3IQW4lc.png)
-------------
```
printTextPresent('img\\noisy.jpg')
```
![noisy.jpg](https://i.imgur.com/Zbe5YBZ.jpg)
**Returns**:
 ![noisy_returns](https://i.imgur.com/P1AbmeP.png)
