## AHAHAHAA
import os, pyaudio, wave
from PIL import Image


image = Image.open('cane.jpg')

chunk = 1024
wf = wave.open('bruh.wav', 'rb')
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(chunk)

for _ in range(10):
    image.show(title="BBBRUUUUUUUUUUHHHHH")
while data:
    stream.write(data)
    data = wf.readframes(chunk)

stream.stop_stream()
stream.close()
p.terminate()
exit(666)