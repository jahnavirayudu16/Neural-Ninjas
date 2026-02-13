import os
from dotenv import load_dotenv
load_dotenv('.env')
import google.generativeai as genai
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    print('NO_KEY')
    exit(1)
try:
    genai.configure(api_key=api_key)
    models = genai.list_models()
    # list_models may return a generator or iterable; iterate and print each model
    for m in models:
        try:
            print(m)
        except Exception:
            print(repr(m))
except Exception as e:
    print('ERROR', e)
