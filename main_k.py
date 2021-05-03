from flask import Flask, render_template, redirect, request
from werkzeug.utils import secure_filename
import os
from utils import audio_extract, audio_ident_lyr
app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/sing")
def sing():
	return render_template("sing.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/song_process", methods=['GET','POST'])
def song_process():
	if request.method == 'POST' or request.method=='GET':
		f = request.files['file']
		if request.files['file'].filename == '':
			return('No selected file')
		elif str(f.filename).endswith('.mp3'):
			name = str(f.filename).replace(" ","")
			name = name.replace(".mp3","")
			alphanumeric = [character for character in name if character.isalnum()]
			name = "".join(alphanumeric)
			name = name+".mp3"
			f.save(os.path.join(app.static_folder,secure_filename(name)))

			path = os.getcwd()
			names = audio_extract(name, path)
			folder_name = names[0]
			karoke_file = names[1]
			vocals_file = names[2]

			lyr = audio_ident_lyr(folder_name, path)
			if lyr is None:
				lyr = "Sorry could not find lyrics."

			return render_template("play_audio.html", karoke = folder_name+"/"+karoke_file, vocals = folder_name+"/"+vocals_file, lyrics = lyr)
		else:
			return("Please check file format")
			
if __name__ == "__main__":
	app.run(host = '0.0.0.0' , port = 8000, debug=True)
