from GptSrtTranslator import GptSrtTranslator
import time
from tempfile import TemporaryDirectory
import os


def Gpt_translate(chatgpt_api_key, input_file, input_language, output_language):
    GptSrtTranslator.API_KEY = chatgpt_api_key
    GptSrtTranslator.MODEL_ENGINE = "gpt-3.5-turbo-0301"

    with TemporaryDirectory() as temp_dir:
        input_file = input_file[:input_file.rfind('.')]+'.srt'
        input_path = os.path.join(temp_dir, input_file)
        output_path = os.path.join(temp_dir, f'{input_file.split(".")[0]}_gpt.srt')
        input_language, output_language = Short2long_lang(input_language, output_language)
        subtitle = GptSrtTranslator(
            input_file=input_path,
            output_file=output_path,
            input_language=input_language,
            output_language=output_language,
            # break after 40 characters
            subtitle_line_max_length=40,
        )
        subtitle.translate()
        with open(output_path, "r", encoding='utf-8') as f:
            gpt_content = f.read()
    return gpt_content

# 언어 치환
def Short2long_lang(input_language, output_language):
    if input_language == 'en':  input_language = 'english'
    elif input_language == 'ja':    input_language = 'japanese'
    elif input_language == 'ko':    input_language = 'korean'
    elif input_language == 'zh':    input_language = 'chinese'
    elif input_language == 'es':    input_language = 'spanish'
    elif input_language == 'fr':    input_language = 'french'
    
    if output_language == 'en': output_language = 'english'
    elif output_language == 'ja':   output_language = 'japanese'
    elif output_language == 'ko':   output_language = 'korean'
    elif output_language == 'zh':   output_language = 'chinese'
    elif output_language == 'es':   output_language = 'spanish'
    elif output_language == 'fr':   output_language = 'french'
    
    return input_language, output_language

def Long2short_lang(input_language, output_language):
    if input_language == 'english':  input_language = 'en'
    elif input_language == 'japanese':    input_language = 'ja'
    elif input_language == 'korean':    input_language = 'ko'
    elif input_language == 'chinese':    input_language = 'zh'
    elif input_language == 'spanish':    input_language = 'es'
    elif input_language == 'french':    input_language = 'fr'

    if output_language == 'english': output_language = 'en'
    elif output_language == 'japanese':   output_language = 'ja'
    elif output_language == 'korean':   output_language = 'ko'
    elif output_language == 'chinese':   output_language = 'zh'
    elif output_language == 'spanish':   output_language = 'es'
    elif output_language == 'french':   output_language = 'fr'

    return input_language, output_language