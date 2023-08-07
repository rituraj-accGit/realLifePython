#takes screenshot of the running screen and saves it into a target folder

import time
import pyautogui
import tkinter as tk

def screenshot():
    time.sleep(2)
    name = int(round(time.time()* 100))
    name= 'C:/DataMine/Projects/PythonProjects/projectsenv/screenshotRecords/{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()

frame= tk.Frame(root)
frame.pack()

scbutton= tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot)

scbutton.pack(side=tk.LEFT)


close= tk.Button(
    frame,
    text="QUIT",
    command=quit
    )
close.pack(side=tk.LEFT)

root.mainloop()