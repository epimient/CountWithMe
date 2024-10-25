from model import WordCounter
from view import View

class Controller:
    def __init__(self):
        self.view = View()
        self.view.boton.configure(command=self.count_words)  # Conectar el botón al método

    def count_words(self):
        # 1. Obtener el texto desde la vista
        texto = self.view.get_text()

        # 2. Crear una instancia del modelo con el texto
        self.model = WordCounter(texto)

        # 3. Contar las palabras utilizando el modelo
        resultado = self.model.count_words()

        # 4. Actualizar la vista con el resultado
        self.view.set_results(resultado)

    def run(self):
        self.view.mainloop()
