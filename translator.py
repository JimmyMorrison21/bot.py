
import pytesseract


def message_taker(message, lang='eng'):
    return pytesseract.image_to_string(message, lang=lang)

