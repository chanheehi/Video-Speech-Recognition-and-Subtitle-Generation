import os, time
import whisper
from moviepy.video.VideoClip import ImageClip
from moviepy.editor import *
from create_srt import Create_srt
from tempfile import TemporaryDirectory

def Whisper_caption(file_full_name, file_path, language, model_size, onoff, progress):
    audio_clip = AudioFileClip(os.path.join(file_path, file_full_name))
    n = round(audio_clip.duration)
    audio_clip.close()
    counter = 0
    start = 0
    index = 30

    flag_to_exit = False
    print('Temp directory:', file_path)
    model = whisper.load_model(model_size)
    file_name, tmp= os.path.splitext(file_full_name)
    
    
    with TemporaryDirectory() as fp:
        while(True):
            audio_clip = AudioFileClip(os.path.join(file_path, file_full_name))
            if index >= n:
                if onoff == 'Off':
                    break
                flag_to_exit = True
                index = n

            temp = audio_clip.subclip(start, index)
            temp_saving_location = os.path.join(fp, f'{file_name}_{counter}.mp3')
            temp.write_audiofile(filename=temp_saving_location)
            temp.close()
            counter += 1
            start = index
            audio_clip.close()
            if flag_to_exit:
                break
            index += 30
            
        
        base_path_to_saved_files, file = os.path.split(temp_saving_location)
        list_of_files = os.listdir(base_path_to_saved_files)
        list_of_files = [file for file in list_of_files if file.startswith(file_name)]
        start = 0
        end = 0
        id_counter = 0
        final_list_of_text = []

        progress(0, desc='staring')
        time.sleep(0.5)
        for index in progress.tqdm(range(len(list_of_files)), desc='음성 인식 진행율(ChatGPT번역까지 할 시 100%가 된 후에도 기다려야함)'):
            path_to_saved_file = os.path.join(base_path_to_saved_files, f'{file_name}_{index}.mp3')
            audio_clip = AudioFileClip(path_to_saved_file)

            duration = 30
            # duration = audio_clip.duration
            audio_clip.close()
            
            # 언어 선택
            if language != '':
                out = model.transcribe(path_to_saved_file, language=language, word_timestamps=True)
            elif language == '':
                out = model.transcribe(path_to_saved_file)

            list_of_text = out['segments']
            for _, line in enumerate(list_of_text):
                
                line['start'] += start
                line['end'] += start
                line['id'] = id_counter
                id_counter += 1

                end = line['end']
                final_list_of_text.append(line)
            start += duration

        for index in range(len(final_list_of_text)):
            data = final_list_of_text[index]
            if index+1 >= len(final_list_of_text):
                break
            fur_data = final_list_of_text[index+1]
            data['end'] = fur_data['start']
            data[duration] = data['end'] - data['start']

        notepad_content = Create_srt(final_list_of_text, file_name)
    
    return notepad_content