from text_analyser.text_cleaner import Cleaner

class Counter:
    def __init__(self, text, nb_words=5, min_word_length=3):
        self.__text = Cleaner(text, min_word_length=min_word_length).clean()
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
