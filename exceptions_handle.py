__author__ = 'rls'
import random

for i in range(1, 6):
    word = random.randint(1,7)
    print(word)


'''
try:
    text = input('Enter something -->')
except EOFError:
    print("Why did you EOF on me?")
except KeyboardInterrupt:
    print("You cancelled the operation.")
else:
    print("You entered {}".format(text))
'''
__version__ = 0.1
