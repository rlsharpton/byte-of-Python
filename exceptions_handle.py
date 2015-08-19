__author__ = 'rls'

try:
    text = input('Enter something -->')
except EOFError:
    print("Why did you EOF on me?")
except KeyboardInterrupt:
    print("You cancelled the operation.")
else:
    print("You entered {}".format(text))

__version__ = 0.1
