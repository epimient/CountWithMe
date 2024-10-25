import customtkinter as ctk
from PIL import Image
import tkinter.font as tkFont
import time

class View(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.iconbitmap("images/icono.ico")
        self.title("Count With Me")
        self.geometry("400x300")
        self.resizable(False, False)
        
        ctk.set_appearance_mode("System")  # Opcional: "Dark", "Light", or "System"
        ctk.set_default_color_theme("blue")  # Opcional: "blue" o "dark-blue"
    
        
        self.font_monserrat = tkFont.Font(family="Montserrat", size=12)
        
        self.texto = ctk.CTkTextbox(self)
        self.texto.pack(side="top", fill="both", expand=True)
        
        self.image = ctk.CTkImage(Image.open("images/hand.png"), size=(20, 20))
        
        self.boton = ctk.CTkButton(self, text="Count Words", image=self.image, fg_color="#7B5BF2", hover_color="#453583")
        self.boton.pack(side="top", fill="both", expand=True)
        
        self.label_result = ctk.CTkLabel(self, text="Número de palabras: 0")
        self.label_result.pack(side="bottom", fill="both", expand=True)

    def get_text(self):
        return self.texto.get("1.0", "end").strip()  # Obtenemos el texto desde la caja de texto

    def set_results(self, results):
        self.label_result.configure(text=f"Número de palabras: {results}")