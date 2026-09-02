import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class AngkaRandomApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.angka = Label(
            text="0",
            font_size=100
        )

        tombol = Button(
            text="GENERATE ANGKA",
            font_size=30
        )

        tombol.bind(on_press=self.generate)

        layout.add_widget(self.angka)
        layout.add_widget(tombol)

        return layout

    def generate(self, tombol):
        self.angka.text = str(random.randint(1, 100))


AngkaRandomApp().run()