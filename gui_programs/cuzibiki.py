import tkinter
import random

def click_btn():
    label["text"] = random.choice(["대길", "중길", "소길", "소흉", "중흉", "대흉"])
    label.update()

root = tkinter.Tk()
root.title("제비뽑기 프로그램")
root.resizable(False, False)
set_font = "Times New Roman"
canvas =tkinter.Canvas(root, width=800, height=600)
canvas.pack()
set_image = tkinter.PhotoImage(file="../image/miko.png")
canvas.create_image(400, 300, image=set_image)
label = tkinter.Label(root, text="??", font=(set_font, 120), bg="white")
label.place(x=380, y=60)
button = tkinter.Button(root, text="제비뽑기", font=(set_font, 36), command=click_btn ,fg="skyblue")
button.place(x=360, y=400)
root.mainloop()