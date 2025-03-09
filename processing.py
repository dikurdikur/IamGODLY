import cv2
import numpy as np
import pytesseract
import pandas as pd
import json
import speech_recognition as sr
from transformers import pipeline

nlp = pipeline("text-generation")

def process_data(filename, content, prompt):
    if filename.endswith(".csv"):
        df = pd.read_csv(content.decode())
        return {"type": "csv", "data": df.to_dict()}

    elif filename.endswith(".json"):
        return {"type": "json", "data": json.loads(content.decode())}

    elif filename.endswith((".png", ".jpg", ".jpeg")):
        img_array = np.frombuffer(content, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        text = pytesseract.image_to_string(img)
        return {"type": "image", "extracted_text": text}

    elif filename.endswith(".wav"):
        recognizer = sr.Recognizer()
        with sr.AudioFile(content) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
        return {"type": "audio", "transcribed_text": text}

    else:
        ai_response = nlp(prompt, max_length=100)
        return {"type": "text", "ai_response": ai_response[0]["generated_text"]}
