import customtkinter as ctk
from PIL import Image

class SplashScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Welcome!")
        self.geometry("600x400")
        self.overrideredirect(True)  # Remueve la barra de título y bordes

        # Cargar imagen para el splash screen
        self.splash_image = ctk.CTkImage(Image.open("images/welcome.png"), size=(600, 400))
        
        # Mostrar la imagen
        self.splash_label = ctk.CTkLabel(self, image=self.splash_image, text="")
        self.splash_label.pack(fill="both", expand=True)

    def close_splash(self):
        self.destroy()

def show_splash():
    splash = SplashScreen()
    splash.after(3000, splash.close_splash)  # Cierra el splash después de 3 segundos
    splash.mainloop()
