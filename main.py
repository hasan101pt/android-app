import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


Window.clearcolor = (40/255.0, 128/255.0, 255/255.0, 1)


class MyGridLayout(GridLayout):

    uber = ObjectProperty(None)
    bolt = ObjectProperty(None)
    refund = ObjectProperty(None)
    rent = ObjectProperty(None)
    viaverde = ObjectProperty(None)
    diesel = ObjectProperty(None)
    percent = ObjectProperty(None)
   
    def press(self):
        uber = float(self.uber.text)
        bolt = float(self.bolt.text)
        refund = float(self.refund.text)
        rent = int(self.rent.text)
        viaverde = float(self.viaverde.text)   
        diesel= float(self.diesel.text)
        percent = int(self.percent.text)

        total_earn=uber+bolt+refund
        total_expense=rent+viaverde+diesel
        final_payment=total_earn-total_expense

        percentage= final_payment * percent / 100

        self.add_widget(Label(text=f"Your total income is {total_earn}\n,Company's total expenses is {total_expense}!\nYour deal in Percentage is {percentage}, \nCongratulation!You've earned {final_payment} Euro this week"))
        
        self.uber.text = ""
        self.bolt.text = ""
        self.refund.text = ""
        self.rent.text = ""
        self.viaverde.text = ""
        self.diesel.text = ""
        self.percent.text = ""
        
        
        



    def clear(self):
        uber = self.uber.text='0'
        bolt = self.bolt.text='0'
        refund = self.refund.text='0'
        rent = self.rent.text='0'
        viaverde = self.viaverde.text='0'  
        diesel= self.diesel.text='0'
        percent = self.percent.text='0'



class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()