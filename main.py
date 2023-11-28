from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.text_input = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        main_layout.add_widget(self.text_input)

        buttons_layout = GridLayout(cols=4, spacing=10)

        buttons = [
            ("7", 1), ("8", 1), ("9", 1), ("/", 1),
            ("4", 1), ("5", 1), ("6", 1), ("*", 1),
            ("1", 1), ("2", 1), ("3", 1), ("-", 1),
            ("C", 1), ("0", 1), (".", 1), ("+", 1),
            ("<", 1), (")", 1), ("(", 1), ("=", 2),
        ]

        for button_text, button_span in buttons:
            button = Button(text=button_text, font_size=32, on_press=self.on_button_press, size_hint=(button_span, 1))
            buttons_layout.add_widget(button)

        main_layout.add_widget(buttons_layout)

        return main_layout

    def on_button_press(self, instance):
        current_text = self.text_input.text
        button_text = instance.text

        if button_text == "=":
            try:
                result = str(eval(current_text))
                self.text_input.text = result
            except Exception as e:
                self.text_input.text = "Error"
        elif button_text == "C":
            self.text_input.text = ""
        elif button_text == "<":
            self.text_input.text = current_text[:-1]
        else:
            new_text = current_text + button_text
            self.text_input.text = new_text

        self.last_button = instance.text


if __name__ == "__main__":
    CalculatorApp().run()