from PIL import Image, ImageFilter
import pytesseract
import os
from dotenv import load_dotenv
load_dotenv()
pathcreated = os.getenv('DIR_TRANCRIPTION')

def image2text(path):
    text =''
    text += pytesseract.image_to_string(path) # extract text

    replacements = (
            ("6", "ó"),
            ("ion", "ión"),
            ("é","ó"),
            ("dn", "ón"),
            ("ria", "ría"),
            ("cia", "cía"),
            ("ii", "ió"),
            ("io", "ió"),
            ("sin", "sión"),
            ("aue", "que"),
            ("ae", "que"),
            ("cue", "que"),
            ("óad", "dad "),
            ("ían", "ian"),
            ("50", "se"),
            ("eun", "es un"),
            ("ss", "as"),
            ("ías", "ias"),
            ("oracones", "oraciones"),
            ("Felaciónadque", "relacionadas"),
            ("ems", "ema"),
            ("elque", "ellas"),
            ("feapresa", "expresa"),
            ("ndaría", "ndaria"),
            ("‘ert", "ext"),
            ("‘ex", "ex"),
            ("eh ", "está "),
            ("yis", "yús"),
            ("Eun", "es un"),
            ("unió", "punto y"),
            (" ina ", "inicia"),
            (" sabr ", "sobr"),
            ("iniciacon", " inicia con "),
            ("ls", "las"),
            ("reprasuce", "reproduce"),
            ("oracor", "orador"),
            ("des", "de"),
            ("oraiónes", "oraciones"),
            ("si tenia", "sin tenerla"),
            ("cite", "cierta"),
            (" 0 ", " o "),
        )
    text_new =text
    for a, b in replacements:
        text_new = text_new.replace(a, b).replace(a.upper(), b.upper())
    return text_new
