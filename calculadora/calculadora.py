from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculadoraApp(App):
    def build(self):
        root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        top_layout = BoxLayout(orientation='horizontal', spacing=5, size_hint_y=(0.2))

        self.display = TextInput(
            text="0", 
            readonly=True, 
            halign="right", 
            font_size=32, 
            size_hint_x=(0.75)
        )
        top_layout.add_widget(self.display)

        btn_c = Button(text="C", font_size=24, size_hint_x=(0.25))
        btn_c.bind(on_press=self.on_button_press)
        top_layout.add_widget(btn_c)

        root_layout.add_widget(top_layout)

        botones_layout = GridLayout(cols=4, rows=4, spacing=5, size_hint_y=(0.8))

        elementos_botones = [
            '7', '8', '9', '*',
            '4', '5', '6', '/',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for simbolo in elementos_botones:
            btn = Button(text=simbolo, font_size=20)
            btn.bind(on_press=self.on_button_press)
            botones_layout.add_widget(btn)

        root_layout.add_widget(botones_layout)

        return root_layout

    def on_button_press(self, instance):
        texto_actual = self.display.text
        pulsado = instance.text

        if pulsado == 'C':
            self.display.text = "0"
        elif pulsado == '=':
            try:
                self.display.text = str(eval(texto_actual))
            except Exception:
                self.display.text = "Error"
        else:
            if texto_actual == "0" and pulsado not in ('/', '*', '+', '-', '.'):
                self.display.text = pulsado
            else:
                self.display.text += pulsado

if __name__ == '__main__':
    CalculadoraApp().run()