@ECHO OFF
ECHO Running DadBot 2.0...
pip install playsound
pip install PyQt5
pip install speechRecognition
pip install pyttsx3
pip install dadjokes
pip install pyjokes
python -u "%~dp0\main.py %*"
PAUSE