from string import punctuation
import re

class Cleaner:
    def __init__(self, text, min_word_length=3):
        self.__text = text
        self.__min_word_length = min_word_length
    
    def __clean_punctuation(self):
        self.__text = re.sub(f"[{punctuation}]", " ", self.__text)
      
    def __clean_newlines(self):
        # raw string: permet de ne pas échapper le \ lui même
        self.__text = re.sub(r"[\r\n]+", " ", self.__text)
    
    def __clean_spaces(self):
        self.__text = re.sub(r"\s+", " ", self.__text)
    
    def __clean_short_words(self):
        self.__text = " ".join(
          list(
            filter(
              lambda w: len(w) > self.__min_word_length, 
              self.__text.split()
            )
          )
        )

    def clean(self):
        self.__clean_punctuation()
        self.__clean_newlines()
        self.__clean_spaces()
        self.__clean_short_words()
        return self.__text.lower()