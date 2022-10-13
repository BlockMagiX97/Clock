from datetime import datetime
import tkinter

def update(frame, label):
    now = datetime.now()
    label.config(text=now.strftime("%H:%M:%S"))
    frame.after(500, lambda: update(frame, label))

root = tkinter.Tk()

frame = tkinter.Frame(root)
frame.pack()
time = tkinter.Label(frame)
time.pack()
update(frame, time)

root.mainloop()
