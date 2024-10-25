class WordCounter:
    def __init__(self, texto):
        self.__texto = texto
    
    def get_text(self):
        return self.__texto
    
    def set_text(self, texto):
        self.__texto = texto
    
    def count_words(self):
        return len(self.__texto.split())  
