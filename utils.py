import os
from flask import Flask, render_template, redirect, request
from werkzeug.utils import secure_filename
from acrcloud.recognizer import ACRCloudRecognizer
import lyricsgenius
import json

def audio_extract(name, path):
    command = "spleeter separate -o "+ path+"/static/" + " " + path+"/static/"+name
    os.system(command)

    folder_name = name[:name.index(".")]
    karoke_file = name[:name.index(".")]+"_karoke.mp3"
    vocals_file = name[:name.index(".")]+"_vocals.mp3"

    audio_ident_seg_command = "ffmpeg -y -ss 0 -t 30 -i "+ path+"/static/"+name+" "+path+"/static/"+folder_name+"/ident.mp3"
    conversion_command_song = "ffmpeg -y -i static/" +folder_name+"/accompaniment.wav -vn -ar 44100 -ac 2 -b:a 192k static/"+folder_name+"/"+karoke_file
    conversion_command_vocals = "ffmpeg -y -i static/"+folder_name+"/vocals.wav -vn -ar 44100 -ac 2 -b:a 192k static/"+folder_name+"/"+vocals_file
    
    os.system(audio_ident_seg_command)
    os.system(conversion_command_song)
    os.system(conversion_command_vocals)

    del_files = "cd "+path+"/static/"+folder_name+" && rm *.wav && cd ../"
    os.system(del_files)
    
    print(command)
    print(audio_ident_seg_command)
    print(conversion_command_song)
    print(conversion_command_vocals)
    print(del_files)

    return (folder_name, karoke_file, vocals_file)

def audio_ident_lyr(folder_name, path):
    #identifies song and returns lyrics
    config = {
    'host': YOUR API KEY,
    'access_key': YOUR API KEY,
    'access_secret': YOUR API KEY,
    'debug': True,
    'timeout': 10
    }

    acrcloud = ACRCloudRecognizer(config)
    file_ident = path+"/static/" +folder_name+"/ident.mp3"
    r = (acrcloud.recognize_by_file(file_ident, 0))

    d = json.loads(r)
    try:
        artist = d['metadata']['music'][-1]['artists'][0]['name']
        song_name = d['metadata']['music'][-1]['title']
        print(song_name)
        print(artist)
        token = YOUR_TOKEN
        genius = lyricsgenius.Genius(token)
        lyr = genius.search_song(song_name, artist)
        if lyr is not None:
            return (lyr.lyrics)
        else:
            return(None)
    except KeyError:
        return(None)

    
