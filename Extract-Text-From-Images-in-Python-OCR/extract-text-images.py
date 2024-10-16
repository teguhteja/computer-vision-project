# %% [markdown]
# Link source : 
# 1. https://github.com/tesseract-ocr/tesseract
# 2. https://tesseract-ocr.github.io/tessdoc/Installation.html

# %%
%pip install pytesseract

# %%
!tesseract --help-psm

# %%
!tesseract logo.png stdout -l eng --psm 11

# %%
!tesseract logo.png stdout -l eng --psm 6

# %%
!tesseract --help-oem

# %%
!tesseract logo.png stdout -l eng --psm 6 --oem 3

# %%
!tesseract instruction.png result.txt

# %%
import pytesseract
import PIL.Image
import cv2

# %%
myconfig = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("instruction.png"), config=myconfig)
print (text)


# %%
myconfig = r"--psm 11 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("sign.png"), config=myconfig)
print(text)


# %%
img = cv2.imread("instruction.png")
height, width, _ = img.shape


# %%
boxes = pytesseract.image_to_boxes(img, config=myconfig)
print (boxes)


# %%
import matplotlib.pyplot as plt

boxes = pytesseract.image_to_boxes(img, config=myconfig)
for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 1)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()


# %%
from pytesseract import Output

data = pytesseract.image_to_data(img, output_type=Output.DICT, config=myconfig)
print(data.keys())
print(data['text'])

# %%
amount_boxes = len(data['text'])
img = cv2.imread("instruction.png")
myconfig = r"--psm 11 --oem 3"
# myconfig = r"--psm 11 --oem 3"
boxes = pytesseract.image_to_boxes(img, config=myconfig)

for i in range(amount_boxes):
    # if len(data['conf']) > 80:
    (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
    img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 1)
    img = cv2.putText(img, data['text'][i], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()


# %%



