# Video-Speech-Recognition-and-Subtitle-Generation
#### Video 음성 인식 및 ChatGPT 번역
<hr>

## 웹페이지 UI
![캡처](https://github.com/chanheehi/Video-Speech-Recognition-and-Subtitle-Generation/assets/101696330/2c6cc75c-02dc-41e1-848b-b5af5f567ea8)


## 결과
#### -동영상 자막 생성 후(상단[원어[/하단[GPT 번역])
![bandicam_2023-06-29_17-53-10-152_AdobeExpress mp4_20230630_201342](https://github.com/chanheehi/Video-Speech-Recognition-and-Subtitle-Generation/assets/101696330/5afb3a35-b61f-4d3e-9be4-5b5de8799f86)
<img src="[[https://github.com/chanheehi/Video-Speech-Recognition-and-Subtitle-Generation/assets/101696330/b5b46d27-0aca-4968-b8b9-7bb1ecc424a5)https://github.com/chanheehi/Video-Speech-Recognition-and-Subtitle-Generation/assets/101696330/b5b46d27-0aca-4968-b8b9-7bb1ecc424a5](https://github.com/chanheehi/Video-Speech-Recognition-and-Subtitle-Generation/assets/101696330/b95b7b5d-5cec-4937-8268-389241c59971)https://github.com/chanheehi/Video-Speech-Recognition-and-Subtitle-Generation/assets/101696330/b95b7b5d-5cec-4937-8268-389241c59971](https://github.com/chanheehi/Video-Speech-Recognition-and-Subtitle-Generation/assets/101696330/5afb3a35-b61f-4d3e-9be4-5b5de8799f86)" width="480">


## 실행
```
python app.py
```
## 종속성 해결
이 requirements.txt파일은 본 코드가 의존하는 Python 라이브러리가 나열되어 있으며, 다음 같이 설치합니다.
```
pip install -r requirements.txt
```
본 코드의 실행은 [`ffmpeg`](https://ffmpeg.org/)가 설치되어있어야 합니다. 환경에 따라 환경변수 설정이 필요합니다.

## 기존의 Whisper 개선한 점
#### - 자막이 반복되는 현상 제거
동영상 길이가 길어질 때 Whisper의 특성상 단어가 반복되는 현상이 생기는데, 동영상을 30초단위의 .mp3로 자르는 과정을 거치며 이를 해결하였습니다.
#### - ChatGPT 번역 기능 추가
번역 기능은 파파고, 구글 번역보다 ChatGPT를 활용할 수 있도록 기능을 추가하였습니다. ChatGPT 번역은 기존보다 더 자연스러운 번역을 제공합니다.
