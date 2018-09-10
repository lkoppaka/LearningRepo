import cv2, numpy as np
from matplotlib import pyplot as plt
import PIL, pytesseract

#trying out an online example for extracting text from the image of a receipt from a restaurant

dimage = lambda x: PIL.Image.fromarray(x)
image = cv2.imread(r'expense_receipt.jpg')
dimage(image)

def norm_img(image, n=10):
    #--- dilation on the green channel ---
    dilated_img = cv2.dilate(image[:,:,1], np.ones((n, n), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 7)
    #--- finding absolute difference to preserve edges ---
    diff_img = 255 - cv2.absdiff(image[:,:,1], bg_img)
    #--- normalizing between 0 to 255 ---
    normed_img = cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    # Return the normed gray dilated image
    return normed_img
    
import re
nstrip = lambda s: re.sub(r"""[^\w\/\'\-#\.]+""", ' ', s)

def get_text(img, n=20):
    text = pytesseract.image_to_string(dimage(norm_img(img, n)))
    return [nstrip(c).strip() for c in text.split()]

from collections import Counter
import itertools

scans = [get_text(image, n) for n in range(1, 40, 4)]
words = Counter(itertools.chain(*scans))
print([word for word in get_text(image, 10) if word in words and words[word] >= 3])
