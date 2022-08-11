'''
This Module is used to translate text
'''

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version= '2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


#from ibm_watson import ApiException
#try:
    # Invoke a method
#except ApiException as ex:
#    print("Method failed with status code " + str(ex.code) + ": " + ex.message)

def english_to_french(english_text):
    '''
    This module translates English text to French text
    '''
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    #list = dict(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    '''
    This module translates French text to English text
    '''
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    return english_text['translations'][0]['translation']
