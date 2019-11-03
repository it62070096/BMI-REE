from tkinter import *

gui=Tk()

"""Config Windows"""
gui.geometry("800x600")
gui.title("BMI")
gui.resizable(0, 0)
gui.iconbitmap(r'icon.ico')
bgpg = PhotoImage(file='bg.png')
label = Label(image=bgpg).pack()

def main():
    """Infomation"""
    # text="ข้อความ", foreground="สีตัวหนังสือ", font=("ชื่อฟอร์น", ขนาด), .pack() คือให้แสดงข้อความ
    Label(gui, text="BMI & REE", foreground="black", font='Helvetica 20 bold').place(x=325, y=10)

    Label(gui, text="ชาย / หญิง", foreground="black", font='Helvetica 10 bold').place(x=50, y=70)
    Entry(gui, width=20, font='Helvetica 15').place(x=130, y=70)

    Label(gui, text="อายุ", foreground="black", font='Helvetica 10 bold').place(x=50, y=110)
    Entry(gui, width=20, font='Helvetica 15').place(x=130, y=110)

    Label(gui, text="น้ำหนัก", foreground="black", font='Helvetica 10 bold').place(x=50, y=150)
    Entry(gui, width=20, font='Helvetica 15').place(x=130, y=150)

    Label(gui, text="ส่วนสูง", foreground="black", font='Helvetica 10 bold').place(x=50, y=190)
    Entry(gui, width=20, font='Helvetica 15').place(x=130, y=190)

    Button(gui, text="ยืนยันข้อมูล", background="white", font=("Courier", 10)).place(x=50, y=230)


main()
gui.mainloop()
