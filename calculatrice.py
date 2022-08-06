from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.core.window import Window
from kivy.lang.builder import Builder 
from kivy.uix import *
import re

Builder.load_file('./calculatrice.kv')
Window.size =(350 , 550)

class CalcuWidget(Widget):
    def result(self):
        p_number =self.ids.input_text.text
        try:
            result = eval(p_number)
            self.ids.input_text.text = str(result)
        except:
            self.ids.input_text.text = "erreur"
        
            
    def remove(self):
        prev = self.ids.input_text.text
        prev = prev[:-1]
        self.ids.input_text.text = prev
        
    def clear(self):
        self.ids.input_text.text = "0"
         
    def chan(self,):
        self.ids.input_text.text
        
    def Button_value(self, number):
        p_number =self.ids.input_text.text
        if "erreur" in p_number:
            p_number = ""
        if p_number == "0":
            self.ids.input_text.text =""
            self.ids.input_text.text = f"{number}"
        else:
            self.ids.input_text.text = f"{p_number}{number}"
    def dot(self):
        p_number = self.ids.input_text.text
        num_list = re.split("\+|\*|/|-|%", p_number)
        
        if ("+" in p_number or "-" in p_number or "/" in p_number or "*" in p_number or "%" in p_number) and "." not in num_list[-1]:
            p_number = f"{p_number}."
            self.ids.input_text.text = p_number
        
        elif "." in p_number:
            pass
        else:
            p_number = f"{p_number}."
            self.ids.input_text.text = p_number
        
    def signe(self ,sign):
        p_number = self.ids.input_text.text
        self.ids.input_text.text = f"{p_number}{sign}"
    def Nsign(self):
        p_number = self.ids.input_text.text
        
        if "-" in p_number:
            self.ids.input_text.text =f"{p_number.replace('-' , '')}"
        else:
            self.ids.input_text.text =f"-{p_number}"    

       
         
         
       
        
        
    
    
class Calcula_ZopsApp(App):
    def build(self):
        self.icon = "z.png"
        return CalcuWidget()
    
    
if __name__ == "__main__":
    Calcula_ZopsApp().run()
 
 

