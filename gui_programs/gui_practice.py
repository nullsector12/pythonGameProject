import tkinter
import tkinter.font


def click_btn():
    button["text"] = "클릭했습니다."


root = tkinter.Tk()
print(tkinter.font.families())
set_font = "Times New Roman"
root.title("첫 번째 라벨")
canvas = tkinter.Canvas(root, width=400, height=600, bg="skyblue")
canvas.pack()
set_image = tkinter.PhotoImage(file="../image/hyunju.png")
canvas.create_image(200, 300, image=set_image)
root.geometry("800x600")
button = tkinter.Button(root, text="버튼 문자열", font=(set_font, 24), command=click_btn)
button.place(x=400, y=200)
label = tkinter.Label(root, text="라벨 문자열", font=(set_font, 24))
label.place(x=200, y=100)
root.mainloop()