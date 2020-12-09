from gtts import gTTS
import os    

speechstr = "Happy Halloween, Torrey"
tts = gTTS(text=speechstr, lang='en')
tts.save("pcvoice.mp3")
# to start the file from python
os.system("start pcvoice.mp3")


