from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import csv

class WordApp(App):
    def build(self):
        self.words = []

        layout = BoxLayout(orientation='vertical')

        self.word_input = TextInput(hint_text='Enter word')
        self.meaning_input = TextInput(hint_text='Enter meaning')

        add_button = Button(text='Add Word')
        add_button.bind(on_press=self.add_word)

        self.word_label = Label(text='Words will appear here')

        layout.add_widget(self.word_input)
        layout.add_widget(self.meaning_input)
        layout.add_widget(add_button)
        layout.add_widget(self.word_label)

        return layout

    def add_word(self, instance):
        word = self.word_input.text
        meaning = self.meaning_input.text
        if word and meaning:
            self.words.append((word, meaning))
            self.word_label.text += f'\n{word}: {meaning}'
            self.word_input.text = ''
            self.meaning_input.text = ''

    def save_to_csv(self, instance):
        with open('words.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Word', 'Meaning'])  # Write the header
            for word, meaning in self.words:
                writer.writerow([word, meaning])  # Write each word and its meaning
        self.word_label.text += '\nWords saved to words.csv'

if __name__ == '__main__':
    WordApp().run()