from tkinter import *

gui=Tk()

"""Config Windows"""
gui.geometry("800x600")
gui.title("BMI")
gui.resizable(0, 0)
gui.iconbitmap(r'icon.ico')

def index():
    # text="ข้อความ", foreground="สีตัวหนังสือ", font=("ชื่อฟอร์น", ขนาด), .pack() คือให้แสดงข้อความ
    Label(gui, text="BMI & REE", foreground="black", font='Helvetica 20 bold').place(x=325, y=10)

    Label(gui, text="ชาย / หญิง", foreground="black", font='Helvetica 10 bold').place(x=50, y=120)

    images = ['boy', 'girl']
    photos = [PhotoImage(file=f'{img}.png') for img in images]
    Button(gui, image=photos[0], borderwidth=0).place(x=160, y=80)
    Button(gui, image=photos[1], borderwidth=0).place(x=270, y=80)


    Label(gui, text="อายุ", foreground="black", font='Helvetica 10 bold').place(x=50, y=200)
    Entry(gui, width=20, font='Helvetica 15').place(x=140, y=200)

    Label(gui, text="น้ำหนัก", foreground="black", font='Helvetica 10 bold').place(x=50, y=240)
    Entry(gui, width=20, font='Helvetica 15').place(x=140, y=240)

    Label(gui, text="ส่วนสูง", foreground="black", font='Helvetica 10 bold').place(x=50, y=280)
    Entry(gui, width=20, font='Helvetica 15').place(x=140, y=280)

    Button(gui, text="ยืนยันข้อมูล", background="white", font=("Courier", 10)).place(x=50, y=320)

    gui.mainloop()

if __name__ == '__main__':
    index()
