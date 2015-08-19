__author__ = 'rls'

poem = '''\
And in the end
The love you take
is equal to the love
    You make
'''

#Open for writing
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break

    print(line),

f.close()


__version__ = 0.1
