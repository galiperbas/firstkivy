from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class AverageCalculatorApp(App):
    def build(self):
        self.title = 'Ortalama Hesaplayici'
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.result_label = Label(text="Sonuc: 0")
        self.input_text = TextInput(hint_text="Sayiları bosluk birakarak giriniz")
        calculate_button = Button(text="Hesapla")
        calculate_button.bind(on_press=self.calculate_average)

        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.input_text)
        self.layout.add_widget(calculate_button)

        return self.layout

    def calculate_average(self, instance):
        input_text = self.input_text.text
        try:
            numbers = [float(num) for num in input_text.split(' ')]
            if numbers:
                average = sum(numbers) / len(numbers)
                self.result_label.text = f"Sonuc: {average:.2f}"
            else:
                self.result_label.text = "Sonuc: 0"
        except ValueError:
            self.result_label.text = "Gecersiz Islem"


if __name__ == '__main__':
    app = AverageCalculatorApp()
    app.run()
