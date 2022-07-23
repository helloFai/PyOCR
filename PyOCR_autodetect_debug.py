from pydoc import ErrorDuringImport
from PIL import ImageGrab
import pytesseract
import pyperclip
from langdetect import detect
from langdetect import detect_langs
# from langdetect import DetectorFactory
# DetectorFactory.seed = 0

langslib = ["chi_sim", "chi_tra", "eng", "ita", "jpn"]
detectlib = ["zh-cn", "zh-tw", "en", "it", "ja"]

def ocr_core(img, langu):
    result = pytesseract.image_to_string(img, lang=langu)
    print(f"result: {result}")
    return result

def lang_detect(ocrresult):
    try:
        detectedresult = detect(ocrresult)
        possibility = detect_langs(ocrresult)
        print(f"detected result: {possibility}")
        return detectedresult
    except:
        print("detection failed.")

def main():
    im = ImageGrab.grabclipboard()
    a = 0
    for a in range(0,5):
        try:
            print(f"round {a+1}")
            ocrresult = ocr_core(im, langslib[a])
            detectedresult = lang_detect(ocrresult)
            if detectedresult == detectlib[a]:
                finalresult = str(ocrresult)
                print(f"final result: {finalresult}")
                pyperclip.copy(finalresult)
            else:
                finalresult = f"{langslib[a]} OCR failed"
                print(finalresult)
        except:
            print(ErrorDuringImport)

if __name__ == "__main__":
    flag = True
    while flag:
        main()
        flag = input('Would you like to run the program again? [y/n]') == 'y'
