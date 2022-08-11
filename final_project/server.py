"""
This Server Module creates paths to multiple endpoints
"""
import json
from flask import Flask, render_template, request
from machinetranslation import translator as tr

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_2_french():
    """
    This module translates english to french
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = tr.english_to_french(text_to_translate)
    return "Translated text to French : " + translated_text

@app.route("/frenchToEnglish")
def french_2_english():
    """
    This module translates english to french
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = tr.french_to_english(text_to_translate)
    return "Translated text to English : " + translated_text

@app.route("/")
def render_index_page():
    """
    This module translates english to french
    """
    # Write the code to render template
    return render_template('templates/index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
