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
        
class test(App):
    def build(self):
        return page1()
if __name__ == "__main__":
    test().run()
