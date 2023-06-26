import datetime
import time
import os
from tempfile import TemporaryDirectory
from typing import *
    
def Create_srt(raw_text, file_name):
    # os_path = os.path.dirname(__file__)[:os.path.dirname(__file__).find('PC')+3]
    # os_path = os_path+'\\Downloads\\'
    # tmp/file_name.srt
    with TemporaryDirectory() as tmp_dir:
        path_to_save = os.path.join(tmp_dir, f"{file_name}.srt")
        # path_to_save = f'{os_path}\\{file_name}.srt'
        with open(path_to_save, 'w', encoding='utf-8') as f:
            for i, text in enumerate(raw_text):
                f.write(str(i+1)+'\n')
                f.write((lambda x: '0'+x if len(x) < 8 else x)(str(datetime.timedelta(seconds=(int(text['start'])))))+',')
                if len(str(text['start']).split('.')[1]) == 1:
                    f.write((lambda x: '00'+x if len(x) == 1 else x)(str(text['start']).split('.')[1])+' --> ')
                elif len(str(text['start']).split('.')[1]) == 2:
                    f.write((lambda x: '0'+x if len(x) == 2 else x)(str(text['start']).split('.')[1])+' --> ')
                elif len(str(text['start']).split('.')[1]) == 3:
                    f.write(str(text['start']).split('.')[1]+' --> ')
                else:
                    f.write("{0:.3f}".format(text['start']).split('.')[1]+' --> ')
                
                f.write((lambda x: '0'+x if len(x) < 8 else x)(str(datetime.timedelta(seconds=(int(text['end'])))))+',')
                if len(str(text['end']).split('.')[1]) == 1:
                    f.write((lambda x: '00'+x if len(x) == 1 else x)(str(text['end']).split('.')[1]))
                elif len(str(text['end']).split('.')[1]) == 2:
                    f.write((lambda x: '0'+x if len(x) == 2 else x)(str(text['end']).split('.')[1]))
                elif len(str(text['end']).split('.')[1]) == 3:
                    f.write(str(text['end']).split('.')[1])
                else:
                    f.write("{0:.3f}".format(text['end']).split('.')[1])
                
                if i+1 == len(raw_text):
                    f.write(f"\n{text['text'].strip().replace('.','')}")
                    break
                f.write(f"\n{text['text'].strip()}\n\n")
        with open(path_to_save, "r", encoding='utf-8') as f:
            notepad_content = f.read()

    return notepad_content
