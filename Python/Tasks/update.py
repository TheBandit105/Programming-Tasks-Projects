text = 'The political slogan "Workers Of The World Unite!"\n is from The Communist Manifesto.'

with open('update.txt', 'w') as file:
    file.write(text)
    print('\nFile Now Closed?: ', file.closed)

print('File Now Closed?: ', file.closed)

with open('update.txt', 'r+') as file:
    text = file.read()
    print('\nString: ', text)

    print('\nPosition In File Now: ', file.tell())
    position = file.seek(33)
    print('Position In File Now: ', file.tell())

    file.write('All Lands')

    file.seek(61)
    file.write('the tombstone of Karl Max.')

    file.seek(0)
    text = file.read()
    print('\nString: ', text)
