# Mad lib zanabria
from random import randint
import copy

madlib = """zanabria era un chico muy {}, y era el mas veloz de la clase. 
Cuando corria parecia un {} y humillaba a todos.
Un dia en plena clase, zanabria empezo {} tan rapido que el profesor {} del susto. 
zanabria ni se inmuto, y se fue {}."""

# crear un diccionario de palabras por tipo
word_dict = {
    'noun':['bandido','sano','atlético','leopardo'],
    'verb':['corriendo','salto','cojeando']
}

def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0,cnt)
    return local_dict[type].pop(index)

def create_madlib():
    local_dict = copy.deepcopy(word_dict)
    return madlib.format(
  get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('verb', local_dict),
        get_word('verb', local_dict),
        get_word('verb', local_dict),
    )

print("madlib: ")
print(create_madlib())
print()
print("madlib2: ")
print(create_madlib())
print()
print ("madlib3: ")
print(create_madlib())
print()







