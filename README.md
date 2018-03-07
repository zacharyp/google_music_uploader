# google_music_uploader
These python scripts are for uploading songs into google play music

## Requirements
brew install ffmpeg

## python requirements:
virtualenv

## Setup:
Run these commands in order:
```
virtualenv --no-site-packages venv
source venv/bin/activate
pip install -r requirements.txt
```

Recently on OSX, I've had to do the following as well (after pip install requirements.txt):
```
pip uninstall protobuf
pip install --no-binary=protobuf protobuf
```

## Get Authorized
Before running either of the scripts, you need to authorize your computer to interact with Google Play Music.  Run the perform_auth script and go to the url given.  Copy the key back in the terminal.  This will save your oauth credential to a default location.
```python
python perform_oauth.py
```
Note: you can only have ten computers authorized at once with Google Play Music, and can only delete four per year!

## Uploading music files
Recursively upload all music files within a directory and all subdirectories.
```
python upload_songs.py -dir "/Users/zacharyp/Downloads"
```

