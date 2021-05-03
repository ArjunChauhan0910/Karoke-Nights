
# Tandoori Nights

This was a hobby project I made to work on my deployment skills. This project is called 
Tandoori Nights in honor of our one true music lord, Himesh Reshamia.

Jokes apart, this project aims to generate the karoke (and vocal) track(s) along with 
its lyrics. Can be useful for a fun night in with the bois if that's your thing. 
I had fun developing this. If you have any feedback or any improvements that you might suggest, please create a pull request :'D


## Features

- Works with any audio file
- Identifies audio using ACRCloud fingerprint database
- Fetches and shows lyrics using LyricsGenius API

  
## Usage/Examples

1. Clone this repository
2. Run setup.sh (convert it into an executable first)
3. Get your API keys from [ACRCloud](https://console-v2.acrcloud.com/account#/register)
4. Get your API keys from [LyricsGenius](https://genius.com/signup_or_login)
5. Update your API details in ```utils.py```
6. Run ```main_k.py``` and open http://0.0.0.0:8000/ on your local browser
  
