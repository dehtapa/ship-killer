import pyttsx3
from pygame import mixer # Load the required library
import playsound
import tkinter as tk
# playsound.playsound('good.mp3', True)
playsound.playsound('Cannon+5.wav', True)

#mixer.init()
# mixer.music.load('/home/dehtapa/Dev/Codecool/projects/ship-killer/good.mp3')
#mixer.music.play()

engine = pyttsx3.init()
#engine.say('hahahahahahahahaahahaha')
engine.runAndWait()

root = tk.Tk()
photo = tk.PhotoImage(file = "giphy.gif")
label = tk.Label(image = photo)
label.pack()
root.mainloop()