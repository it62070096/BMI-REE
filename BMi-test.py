import pygal
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
Builder.load_string('''
<GridLayout>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
<Label>:
    font_size: 50
    color: 0,0,0,1
    font_name: "angsa.ttf"
<TextInput>:
    font_size: 30
    font_name: "angsa.ttf"
    size_hint_y: None
    size_hint_x: None
''')
class page1(GridLayout):
    def __init__(self):
        super().__init__()
        self.name = Label(text="BMI & REE", font_size=150, pos=(720,650), color=(0.9, 0.3, 0.2, 1.0))
        self.sex = TextInput(hint_text="male/female", size=(300,50), pos=(645,450))
        self.sextext = Label(text="เพศ", font_size=35, pos=(546, 430))
        self.age = TextInput(size=(300,50), pos=(645, 380))
        self.agetext = Label(text="อายุ", font_size=35, pos=(546, 360))
        self.weight = TextInput(hint_text="kg.", size=(300,50), pos=(645, 310))
        self.weighttext = Label(text="น้ำหนัก", font_size=35, pos=(530, 290))
        self.hhh = TextInput(hint_text="cm.", size=(300,50), pos=(645, 240))
        self.hhhtext = Label(text="ส่วนสูง", font_size=35, pos=(530, 220))
        self.next = Button(text="Next", font_size=30, background_color=(3.0,1.0,1.0,1.0), size=(100,50), pos=(1300,40))
        self.next.bind(on_press=self.change1)


        self.add_widget(self.name)
        self.add_widget(self.sex)
        self.add_widget(self.sextext)
        self.add_widget(self.age)
        self.add_widget(self.agetext)
        self.add_widget(self.weight)
        self.add_widget(self.weighttext)
        self.add_widget(self.hhh)
        self.add_widget(self.hhhtext)
        self.add_widget(self.next)

    def change1(self, *args):
        self.clear_widgets()
        return self.page2()

    def change2(self, *args):
        self.clear_widgets()
        return self.page1()
    
    def change3(self, *args):
        self.clear_widgets()
        return self.page3()

    def change4(self, *args):
        self.clear_widgets()
        return self.page4()

    def change5(self, *args):
        self.clear_widgets()
        return self.page3()
    
    def page1(self):
        self.name = Label(text="BMI & REE", font_size=150, pos=(720,650), color=(0.9, 0.3, 0.2, 1.0))
        self.sex = TextInput(hint_text="male/female", size=(300,50), pos=(645,450))
        self.sextext = Label(text="เพศ", font_size=35, pos=(546, 430))
        self.age = TextInput(size=(300,50), pos=(645, 380))
        self.agetext = Label(text="อายุ", font_size=35, pos=(546, 360))
        self.weight = TextInput(hint_text="kg.", size=(300,50), pos=(645, 310))
        self.weighttext = Label(text="น้ำหนัก", font_size=35, pos=(530, 290))
        self.hhh = TextInput(hint_text="cm.", size=(300,50), pos=(645, 240))
        self.hhhtext = Label(text="ส่วนสูง", font_size=35, pos=(530, 220))
        self.next = Button(text="Next", font_size=30, size=(100,50), pos=(1300,40), background_color=(3.0,1.0,1.0,1.0))
        self.next.bind(on_press=self.change1)


        self.add_widget(self.name)
        self.add_widget(self.sex)
        self.add_widget(self.sextext)
        self.add_widget(self.age)
        self.add_widget(self.agetext)
        self.add_widget(self.weight)
        self.add_widget(self.weighttext)
        self.add_widget(self.hhh)
        self.add_widget(self.hhhtext)
        self.add_widget(self.next)
    def page2(self):
        self.name = Label(text="BMI & REE", font_size=150, pos=(720,650), color=(0.9, 0.3, 0.2, 1.0))
        self.add_widget(self.name)
        self.bmi = Button(text="BMI", size=(300,150), pos=(400,300), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.bmi)
        self.ree = Button(text="REE", size=(300,150), pos=(820, 300), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.ree)
        self.back = Button(text="Back", font_size=30, size=(100,50), pos=(100, 40), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.back)
        self.graph = Button(text="Graph BMI", font_size=25, size=(100, 50), pos=(1300, 40), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.graph)
        self.back.bind(on_press=self.change2)
        self.bmi.bind(on_press=self.calbmi)
        self.ree.bind(on_press=self.page3)

    def page3(self, *args):
        self.name = Label(text="BMI & REE", font_size=150, pos=(720,650), color=(0.9, 0.3, 0.2, 1.0))
        self.add_widget(self.name)
        self.ree2 = Button(text="REE only", size=(300,150), pos=(400,300), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.ree2)
        self.tdee = Button(text="REE & TDEE", size=(300,150), pos=(820, 300), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.tdee)
        self.back2 = Button(text="Back", font_size=30, size=(100,50), pos=(100,40), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.back2)
        self.back2.bind(on_press=self.change1)
        self.ree2.bind(on_press=self.calree)
        self.tdee.bind(on_press=self.change4)

    def page4(self):
        self.name = Label(text="BMI & REE", font_size=150, pos=(720,650), color=(0.9, 0.3, 0.2, 1.0))
        self.add_widget(self.name)
        self.name2 = Label(text="ความถี่การออกกำลังกาย", font_size=50, pos=(720,500), color=(0.9, 0.3, 0.2, 1.0))
        self.add_widget(self.name2)
        self.level1 = Button(text="No exercise", font_size=30, size=(150,100), pos=(200,300), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.level1)
        self.level2 = Button(text="1 - 3 days/week", font_size=30, size=(150,100), pos=(450,300), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.level2)
        self.level3 = Button(text="3 - 5 days/week", font_size=30, size=(150,100), pos=(700,300), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.level3)
        self.level4 = Button(text="6 - 7 days/week", font_size=30, size=(150,100), pos=(950,300), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.level4)
        self.level5 = Button(text="Every day", font_size=30, size=(150,100), pos=(1200,300), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.level5)
        self.back3 = Button(text="Back", font_size=30, size=(100,50), pos=(100,40), background_color=(3.0,1.0,1.0,1.0))
        self.add_widget(self.back3)

        self.level1.bind(on_press=self.caltdee1)
        self.level2.bind(on_press=self.caltdee2)
        self.level3.bind(on_press=self.caltdee3)
        self.level4.bind(on_press=self.caltdee4)
        self.level5.bind(on_press=self.caltdee5)
        self.back3.bind(on_press=self.change5)

    def calbmi(self, *args):
        try:
            weight = float(self.weight.text)
            hhh = float(self.hhh.text)
            result = weight/((hhh/100)**2)
            result = "%.2f"%(result)
            if self.sex.text == "male":
                if float(result) < 19:
                    result1 = Popup(title="BMI", content=Label(text=result+"  ผอม", size=(100,200)), size_hint_y=None, size_hint_x=None, \
                        size=(300, 300), pos=(400, 400), title_size=20, title_color=(0,0,0,1))
                    result1.open()
                elif 19 <= float(result) <= 24.9:
                    result1 = Popup(title="BMI", content=Label(text=result+"  สมส่วน", size=(100,200)), size_hint_y=None, size_hint_x=None, \
                        size=(300, 300), pos=(400, 400), title_size=20, title_color=(0,0,0,1))
                    result1.open()
                elif 25 <= float(result) < 29.9:
                    result1 = Popup(title="BMI", content=Label(text=result+"  น้ำหนักเกิน", size=(100,200)), size_hint_y=None, size_hint_x=None, \
                        size=(300, 300), pos=(400, 400), title_size=20, title_color=(0,0,0,1))
                    result1.open()
                else:
                    result1 = Popup(title="BMI", content=Label(text=result+"  อ้วน", size=(100,200)), size_hint_y=None, size_hint_x=None, \
                        size=(300, 300), pos=(400, 400), title_size=20, title_color=(0,0,0,1))
                    result1.open()
            elif self.sex.text == "female":
                if float(result) < 18:
                    result1 = Popup(title="BMI", content=Label(text=result+"  ผอม", size=(100,200)), size_hint_y=None, size_hint_x=None, \
                        size=(300, 300), pos=(400, 400), title_size=20, title_color=(0,0,0,1))
                    result1.open()
                elif 18 <= float(result) <= 23.9:
                    result1 = Popup(title="BMI", content=Label(text=result+"  สมส่วน", size=(100,200)), size_hint_y=None, size_hint_x=None, \
                        size=(300, 300), pos=(400, 400), title_size=20, title_color=(0,0,0,1))
                    result1.open()
                elif 24 <= float(result) < 29.9:
                    result1 = Popup(title="BMI", content=Label(text=result+"  น้ำหนักเกิน", size=(100,200)), size_hint_y=None, size_hint_x=None, \
                        size=(300, 300), pos=(400, 400), title_size=20, title_color=(0,0,0,1))
                    result1.open()
                else:
                    result1 = Popup(title="BMI", content=Label(text=result+"  อ้วน", size=(100,200)), size_hint_y=None, size_hint_x=None, \
                        size=(300, 300), pos=(400, 400), title_size=20, title_color=(0,0,0,1))
                    result1.open()
            else:
                result1 = Popup(title="BMI", content=Label(text="ERROR", size=(100, 200)), size_hint_y=None, size_hint_x=None,\
                    size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
                result1.open()

        except:
            result1 = Popup(title="BMI", content=Label(text="ERROR", size=(100, 200)), size_hint_y=None, size_hint_x=None,\
                size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
            result1.open()

    def calree(self, *args):
        try:
            if self.sex.text == "male":
                weight = float(self.weight.text)
                hhh = float(self.hhh.text)
                age = int(self.age.text)
                result = (10*weight) + (6.25*hhh) - (5*age) +5
                result = "%.2f"%result
                result1 = Popup(title="REE & TDEE", content=Label(text=result, size=(100,200)), size_hint_y=None, size_hint_x=None, \
                    size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
                result1.open()
            elif self.sex.text == "female":
                weight = float(self.weight.text)
                hhh = float(self.hhh.text)
                age = int(self.age.text)
                result = (10*weight) + (6.25*hhh) - (5*age) - 161
                result = "%.2f"%result
                result1 = Popup(title="REE & TDEE", content=Label(text=result, size=(100,200)), size_hint_y=None, size_hint_x=None, \
                    size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
                result1.open()
            else:
                result1 = Popup(title="BMI", content=Label(text="ERROR", size=(100, 200)), size_hint_y=None, size_hint_x=None,\
                    size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
                result1.open()
        except:
            result1 = Popup(title="REE", content=Label(text="ERROR", size=(100, 200)), size_hint_y=None, size_hint_x=None,\
                size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
            result1.open()
            
    def caltdee1(self, *args):
        try:
            if self.sex.text == "male":
                weight = float(self.weight.text)
                hhh = float(self.hhh.text)
                age = int(self.age.text)
                result = ((10*weight) + (6.25*hhh) - (5*age) +5)*1.2
                result = "%.2f"%result
                result1 = Popup(title="REE & TDEE", content=Label(text=result, size=(100,200)), size_hint_y=None, size_hint_x=None, \
                    size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
                result1.open()
            elif self.sex.text == "female":
                weight = float(self.weight.text)
                hhh = float(self.hhh.text)
                age = int(self.age.text)
                result = ((10*weight) + (6.25*hhh) - (5*age) - 161)*1.2
                result = "%.2f"%result
                result1 = Popup(title="REE & TDEE", content=Label(text=result, size=(100,200)), size_hint_y=None, size_hint_x=None, \
                    size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
                result1.open()
            else:
                result1 = Popup(title="BMI", content=Label(text="ERROR", size=(100, 200)), size_hint_y=None, size_hint_x=None,\
                    size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
                result1.open()
        except:
            result1 = Popup(title="REE", content=Label(text="ERROR", size=(100, 200)), size_hint_y=None, size_hint_x=None,\
                size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
            result1.open()
    
    def caltdee2(self, *args):
        try:
            if self.sex.text == "male":
                weight = float(self.weight.text)
                hhh = float(self.hhh.text)
                age = int(self.age.text)
                result = ((10*weight) + (6.25*hhh) - (5*age) +5)*1.375
                result = "%.2f"%result
                result1 = Popup(title="REE & TDEE", content=Label(text=result, size=(100,200)), size_hint_y=None, size_hint_x=None, \
                    size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
                result1.open()
            elif self.sex.text == "female":
                weight = float(self.weight.text)
                hhh = float(self.hhh.text)
                age = int(self.age.text)
                result = ((10*weight) + (6.25*hhh) - (5*age) - 161)*1.375
                result = "%.2f"%result
                result1 = Popup(title="REE & TDEE", content=Label(text=result, size=(100,200)), size_hint_y=None, size_hint_x=None, \
                    size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
                result1.open()
            else:
                result1 = Popup(title="BMI", content=Label(text="ERROR", size=(100, 200)), size_hint_y=None, size_hint_x=None,\
                    size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
                result1.open()
        except:
            result1 = Popup(title="REE", content=Label(text="ERROR", size=(100, 200)), size_hint_y=None, size_hint_x=None,\
                size=(300,300), pos=(400,400), title_size=20, title_color=(0,0,0,1))
            result1.open()

class test(App):
    def build(self):
        return page1()
if __name__ == "__main__":
    test().run()
