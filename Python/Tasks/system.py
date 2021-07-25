import sys, keyword 

print('Python Version: ', sys.version)

print('Python Interpreter Location: ', sys.executable)

print('Python Module Search Path: ')
for folder in sys.path:
    print(folder)

print('Python Keywords: ')
for word in keyword.kwlist:
    print(word)
