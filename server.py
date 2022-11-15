from flask import Flask, render_template, request, jsonify
import time
from PitchIdentificationByRules import pitchidentification

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

audio_directory = "static/audios/"
pic_directory = "static/pic/"
audio_suffix = '.wav'
pic_suffix = '.jpg'
def get_file_path():
    filename = str(int(time.time()))
    return f"{audio_directory}{filename}{audio_suffix}", f"{pic_directory}{filename}{pic_suffix}"

@app.post('/identify')
def identify():
    try:
        file = request.files['file']
        audio_name, pic_name = get_file_path()
        file.save(audio_name)
        pitch=pitchidentification(audio_name,pic_name)
    except:
        k=int(request.values.get("k"))
        if type(k) != type(1) or k<1 or k>21:
            return jsonify({ 
            'message': "Please type in an integer within the range of the notes", 
        })
        _, pic_name = get_file_path()
        pitch=pitchidentification(f"static/data/{k}.wav",pic_name)
    return render_template("index.html", Pitch=f"The pitch of this note is {pitch}", img_dir=pic_name)

if __name__ == '__main__':
    app.run('127.0.0.1', 8000)
