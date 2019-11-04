# -*- Coding: utf-8 -*-

from PIL import Image
import sys

import pyocr
import pyocr.builders

import cv2



'''
# checker
tools = pyocr.get_available_tools() #is there any OCR tools
if len(tools) == 0:
    print("NO OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name())) #what tool you gonna use

langs = tool.get_available_languages()
print("Available languages: %s" % ",".join(langs))

lang = langs[0]
print("Will use lang '%s'" % (lang))
'''



# to text
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("NO OCR tool found")
    sys.exit(1)

tool = tools[0]
#print("Will use tool '%s'" % (tool.get_name()))

res = tool.image_to_string(#specify options
    Image.open('impt.jpg'),
    #lang='jpn',
    lang='eng',
    #lang='snum',
    #builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    builder=pyocr.builders.WordBoxBuilder(tesseract_layout=6)
    #builder=pyocr.builders.LineBoxBuilder(tesseract_layout=6)
)

#print(res)

for d in res:
    print(d.content)
    #print(d.position)

# open cv
out = cv2.imread('impt.jpg')
for d in res:
    #print(d.content)
    #print(d.position)
    cv2.rectangle(out, d.position[0], d.position[1], (10, 0, 250), 2)

cv2.imshow('img',out)
#cv2.imwrite('otpt.png',out)
cv2.waitKey(0)
vc2.destroyAllWindows()
