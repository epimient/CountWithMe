import customtkinter as ctk
from PIL import Image
import time

def show_splash():
    # Crear la ventana de splash
    splash = ctk.CTk()
    splash.overrideredirect(True)  # Oculta la barra de título y bordes
    splash.wm_attributes("-transparentcolor", "white")  # Simula transparencia usando el color blanco como fondo transparente
    
    # Tamaño de la imagen del splash (ajusta según tu imagen)
    splash_width = 600
    splash_height = 400
    
    # Obtén la resolución de la pantalla
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    
    # Calcular la posición x, y para centrar la ventana
    x_cordinate = int((screen_width / 2) - (splash_width / 2))
    y_cordinate = int((screen_height / 2) - (splash_height / 2))
    
    # Configura la geometría de la ventana con la posición centrada
    splash.geometry(f"{splash_width}x{splash_height}+{x_cordinate}+{y_cordinate}")
    
    # Cargar la imagen PNG con transparencia
    splash_image = ctk.CTkImage(Image.open("images/welcome.png"), size=(splash_width, splash_height))
    
    # Crear una etiqueta para mostrar la imagen en la ventana
    splash_label = ctk.CTkLabel(splash, image=splash_image, text="", fg_color="white")
    splash_label.pack(fill="both", expand=True)
    
    # Mostrar el splash durante 3 segundos
    splash.update()
    time.sleep(3)
    
    # Destruir el splash screen
    splash.destroy()

# Ejecutar el splash en el bloque principal
if __name__ == "__main__":
    show_splash()

    # Aquí continúa la aplicación principal
    from controller import Controller  # Importa el controlador después del splash
    controlador = Controller()
    controlador.run()
