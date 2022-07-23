
from PIL import Image, ImageGrab
import pytesseract
import pyperclip

im = ImageGrab.grabclipboard()
langslib = ["chi_sim", "chi_tra", "eng", "ita", "jpn"]

# if isinstance(im, Image.Image):
#     print("Image: size : %s, mode : %s" % (im.size, im.mode))
#     im.save("./grab_clipboard.png")
# elif im:
#     for filename in im:    
#         print("filename : %s" % filename)
#         im = Image.open(filename)
# else:
#     print("clipboard is empty")

    
def ocr_core(img, langu):
    text = pytesseract.image_to_string(img, lang=langu)
    return text

    
if __name__ == "__main__":
    try:
        picknum = int(input("please select a language:1. 简中 2.繁中 3.English 4.italiano 5.日本語:  "))
        lang_picked = langslib[picknum-1]
        result = ocr_core(im, lang_picked)
        print(result)
        pyperclip.copy(result)
    except:
        result = ocr_core(im, langslib[0])
        print(result)
        pyperclip.copy(result)