import gradio as gr
from whisper_caption import Whisper_caption
from gpt_translate import Gpt_translate, Long2short_lang
import os

def greet(file_name, input_language, output_language, model_size, chatgpt_api_key, onoff, progress=gr.Progress()):
    file_path = os.path.dirname(file_name.name)
    file_name = os.path.basename(file_name.name)
    input_language, output_language = Long2short_lang(input_language, output_language)
    notepad_content = Whisper_caption(file_name, file_path, input_language, model_size, onoff, progress)
    if chatgpt_api_key == '':
        return notepad_content, ''
    gpt_content = Gpt_translate(chatgpt_api_key, file_name, input_language, output_language, notepad_content)
    return notepad_content, gpt_content

demo = gr.Interface(fn=greet,
                    inputs=[gr.File(label="file_upload(.mp4/.mp3 형식)[1GB 이상의 파일 업로드는 추천하지 않음/uploading이 download로 바뀌면 제출하기 누르기]"),
                        gr.Dropdown(["english", "japanese", "chinese", "korean", "spanish", "french"], label="input_language(입력 동영상의 언어)", value="english"),
                        gr.Dropdown(["english", "japanese", "chinese", "korean", "spanish", "french"], label="output_language(chatgpt_api_key를 채우지 않을 시 output_language는 input_language과 같음)", value="korean"),
                        gr.Dropdown(["medium", "large", "large-v1", "large-v2"], label="model_size(large-v2[느리지만 정확함])", value="large-v2"),
                        gr.Textbox(label="chatgpt_api_key(GPT를 활용해 한글로 번역하지 않을것이라면 비워놓아야함)", type="text"),
                        gr.Dropdown(["On", "Off"], label="error 발생 시 Off로 설정(Off 설정 시 동영상 마지막30초는 자막 생성X)", value="On")
                        ],
                    outputs=[
                        gr.Textbox(label='Contents of the input video', show_copy_button=True),
                        gr.Textbox(label='Contents of the GPT translation', show_copy_button=True)
                        ],
                    cache_examples=True,
                    title="Video 음성 인식 및 ChatGPT 번역(제출하기 한번만 눌러야함, 원래 눌러도 무반응처럼 보임)",
                    description="블로그(https://blog.naver.com/jc603/223139586897)에서 자세한 내용을 확인할 수 있음/이 페이지의 기능은 같은 시간 한명만 사용 가능함(그래픽카드 연산 문제)"
                    )
                                                    
if __name__ == "__main__":
    demo.queue().launch(share=True, enable_queue=True, debug=True, show_error=True)