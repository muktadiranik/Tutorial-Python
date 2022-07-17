from gtts import gTTS
import os

a = open('test.txt', 'r+')
text = a.read().replace('\n', ' ')
o = gTTS(text=text, lang='en', slow=False)
o.save('test.mp3')
a.close()
os.system('start test.mp3')
