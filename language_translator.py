import tkinter as tk
from googletrans import Translator, LANGUAGES

class LanguageTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator ByKomali Kumari Vasamsetti ")
        
        self.root.geometry("400x250")

        self.translator = Translator()

        self.create_widgets()

    def create_widgets(self):
        self.lbl_input = tk.Label(self.root, text="Enter text to translate:")
        self.lbl_input.pack()

        self.entry_text = tk.Entry(self.root, width=40)
        self.entry_text.pack()

        self.lbl_dest_lang = tk.Label(self.root, text="Select destination language:")
        self.lbl_dest_lang.pack()

        self.dest_lang_var = tk.StringVar()
        self.dest_lang_var.set("English")  # Default destination language (English)

        self.dest_lang_dropdown = tk.OptionMenu(self.root, self.dest_lang_var, *self.get_languages())
        self.dest_lang_dropdown.pack()

        self.btn_translate = tk.Button(self.root, text="Translate", command=self.translate_text)
        self.btn_translate.pack()

        self.lbl_output = tk.Label(self.root, text="Translation:")
        self.lbl_output.pack()

        self.lbl_translation = tk.Label(self.root, text="", wraplength=350)
        self.lbl_translation.pack()

    def get_languages(self):
        language_names = [LANGUAGES[lang_code] for lang_code in LANGUAGES]
        language_names.sort()  # Sort languages alphabetically
        return language_names

    def translate_text(self):
        input_text = self.entry_text.get()
        destination_lang = self.dest_lang_var.get()

        if input_text:
            destination_lang_code = [lang_code for lang_code, lang_name in LANGUAGES.items() if lang_name == destination_lang]
            if destination_lang_code:
                translation = self.translator.translate(input_text, src="en", dest=destination_lang_code[0])
                self.lbl_translation.config(text=translation.text)
            else:
                self.lbl_translation.config(text="Invalid destination language.")
        else:
            self.lbl_translation.config(text="Please enter text to translate.")


if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslator(root)
    root.mainloop()
