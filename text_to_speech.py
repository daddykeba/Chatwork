import subprocess
import os
from mpyg321.mpyg321 import MPyg321Player
player = MPyg321Player

from gtts import gTTS

mytext = 'Bienvenue à ma propre innovation'

language = 'fr'

myobj = gTTS(text=mytext, lang=language)

myobj.save("welcome.mp3")


subprocess.call(['mpg123', "welcome.mp3", '--play-and-exit'])