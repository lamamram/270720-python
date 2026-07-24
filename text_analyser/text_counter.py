# import ABSOLU
# les imports sont calculés (sauf relatif) à partir du module PRINCIPAL
from text_analyser.text_cleaner import Cleaner
# from .text_cleaner import Cleaner

## décision architecturale:
## ici le counter A BESOIN du cleaner donc il est fortement couplé

## autre décision archi
## je ne veux pas que le counter sache créer le cleaner
class Counter:
    
     # def __init__(self, text: str, cleaner: Cleaner, nb_words: int=5, min_word_length: int=3):
        # self.__text = Cleaner(text, min_word_length=min_word_length).clean()
    def __init__(self, cleaner: Cleaner, nb_words: int=5, min_word_length: int=3):
        self.__text = cleaner.clean()
        self.__nb_words = nb_words

    def get_occurences(self):
        # count occurences
        occurences = {}
        for word in self.__text.split():
            if word in occurences:
                occurences[word] += 1
            else:
                occurences[word] = 1
        
        # tri et limiter
        return dict(
          sorted(
            occurences.items(), 
            key=lambda x: x[1], 
            reverse=True
          )[:self.__nb_words])

# if __name__ == "__main__":
#     print("ok") # ModuleNotFoundError: on ne travaille pas en direct dans un module importé