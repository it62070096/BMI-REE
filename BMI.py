from tkinter import *

gui=Tk()

"""Config Windows"""
gui.geometry("800x600")
gui.title("BMI")
gui.resizable(0, 0)
gui.iconbitmap(r'icon.ico')

def main():
    """Infomation"""
    # text="ข้อความ", foreground="สีตัวหนังสือ", font=("ชื่อฟอร์น", ขนาด), .pack() คือให้แสดงข้อความ
    labelinfo_1 = Label(text="BMI & REE", foreground="black", font='Helvetica 20 bold').place(x=350, y=10)
    labelsex = Label(text="ชาย / หญิง", foreground="black", font='Helvetica 10 bold').place(x=250, y=70)
    sexentry = Entry().place(x=375, y=70)
    cfinfo = Button(text="ยืนยันข้อมูล", background="white", font=("Courier", 10)).place(x=350, y=300)


main()
gui.mainloop()
