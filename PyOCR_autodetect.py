
from PIL import Image, ImageGrab
import pytesseract
import pyperclip
from langdetect import detect
# from langdetect import detect_langs
# from langdetect import DetectorFactory
# DetectorFactory.seed = 0

im = ImageGrab.grabclipboard()
langslib = ["chi_sim", "chi_tra", "eng", "ita", "jpn"]
detectlib = ["zh-cn", "zh-tw", "en", "it", "ja"]

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
    result = pytesseract.image_to_string(img, lang=langu)
    # print(f"result: {result}")
    return result

def lang_detect(ocrresult):
    try:
        detectedresult = detect(ocrresult)
        # possibility = detect_langs(ocrresult)
        # print(f"detected result: {possibility}")
        return detectedresult
    except:
        print("detection failed.")


if __name__ == "__main__":
    a = 0
    for a in range(0,5):
        # print(f"round {a+1}")
        ocrresult = ocr_core(im, langslib[a])
        detectedresult = lang_detect(ocrresult)
        if detectedresult == detectlib[a]:
            finalresult = str(ocrresult)
            print(f"final result: {finalresult}")
            pyperclip.copy(finalresult)
        else:
            pass
