import pyjokes as joke
from PyDictionary import PyDictionary
from auto_corrector import correct as spellcheck

myJoke = joke.get_joke("en")
dictionary = PyDictionary()
wrong_sentence = "Thsi is wwrong"
correct_sentence = spellcheck(wrong_sentence)

print(dictionary.meaning("Computer"))
print(myJoke)
print(correct_sentence)