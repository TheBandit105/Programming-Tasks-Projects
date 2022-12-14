import time
print('Welcome to the Pythonator Quiz!')

while True:
    play = input('Do you want to play? ')

    if play.lower() == 'yes':
        break
    elif play.lower() == 'no':
        quit()
    else:
        print('Invalid input. Please try again!')
    

name = input('\nWhat is your name? ')

print('\nOK', name, 'quiz starting!')

time.sleep(2.4)

score = 0

print('\nScore: ', score)
ans = input('(1) Continental United States has 4 different time zones, can you name them?\n')

if ans == 'Pacific, Mountain, Central, Eastern':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Pacific, Mountain, Central, Eastern.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(2) What was the Turkish city of Istanbul called before 1930?\n')

if ans == 'Constantinople':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Constantinople.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(3) From which US city do the band The Killers originate?\n')

if ans == 'Las Vegas':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Las Vegas.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(4) Name the Coffee shop in US sitcom Friends.\n')

if ans == 'Central Perk':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Central Perk.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(5) How many human players are there on each side in a polo match?\n')

if ans.lower() == 'four' or '4':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was 4.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(6) In what year did Tony Blair become British Prime Minister?\n')

if ans == '1997':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was 1997.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(7) How many times has England won the men’s football World Cup?\n')

if ans.lower() == 'once' or ans == 'Once (1966)' or 'once (1996)':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was once (1996).')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(8) What is the capital of New Zealand?\n')

if ans == 'Wellington':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Wellington.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(9) Street artist Banksy is originally associated with which British city?\n')

if ans == 'Bristol':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Bristol.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(10) From what grain is the Japanese spirit Sake made?\n')

if ans.lower() == 'rice':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was rice.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(11) In which part of your body would you find the cruciate ligament?\n')

if ans.lower() == 'knee':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was knee.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(12) What is the name of the main antagonist in the Shakespeare play Othello?\n')

if ans == 'Lago':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Lago.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(13) What element is denoted by the chemical symbol Sn in the periodic table?\n')

if ans == 'Tin':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Tin.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(14) What is the name of the 1976 film about the Watergate scandal, starring Robert Redford and Dustin Hoffman?\n')

if ans == "All the President's Men":
    print('\nCorrect!')
    score += 1
else:
    print("\nIncorrect! The correct answer was All the President's Men.")

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(15) How many of Henry VIII’s wives were called Catherine?\n')

if ans.lower() == 'three' or '3':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was 3.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(16) What was the most popular girls name in the UK in 2019?\n')

if ans == 'Olivia':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Olivia.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(17) Which comedian was the second permanent host of Never Mind the Buzzcocks after Mark Lamarr?\n')

if ans == 'Simon Amstell':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Simon Amstell.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(18) Which popular video game franchise has released games with the subtitles World At War and Black Ops?\n')

if ans == 'Call of Duty':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Call of Duty.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(19) In what US State is the city Nashville?\n')

if ans == 'Tennessee':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Tennessee.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(20) Which rock band was founded by Trent Reznor in 1988?\n')

if ans == 'Nine Inch Nails':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Nine Inch Nails.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(21) What is the currency of Denmark?\n')

if ans == 'Krone':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Krone.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(22) Which Tennis Grand Slam is played on a clay surface?\n')

if ans == 'The French Open (Roland Garros)' or 'Roland Garros':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was The French Open (Roland Garros).')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(23) In which European country would you find the Rijksmuseum?\n')

if ans == 'Netherlands':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Netherlands.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(24) How many films have Al Pacino and Robert De Niro appeared in together?\n')

if ans.lower() == 'four' or '4':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was 4.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(25) What was the old name for a Snickers bar before it changed in 1990?\n')

if ans == 'Marathon':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Marathon.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(26) Who was the head of state in Japan during the second world war?\n')

if ans == 'Emperor Hirohito':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Emperor Hirohito.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(27) What is the smallest planet in our solar system?\n')

if ans == 'Mercury':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Mercury.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(28) Who wrote the novels Gone Girl and Sharp Objects?\n')

if ans == 'Gillian Flynn':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Gillian Flynn.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(29) Which legendary surrealist artist is famous for painting melting clocks?\n')

if ans == 'Salvador Dali':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Salvador Dali.')

time.sleep(2.4)

print('\nScore: ', score)
ans = input('(30) Which football club plays its home games at Loftus Road?\n')

if ans == 'Queen’s Park Rangers' or 'QPR':
    print('\nCorrect!')
    score += 1
else:
    print('\nIncorrect! The correct answer was Queen’s Park Rangers (QPR).')

time.sleep(2.4)

print('\nTHANK YOU FOR PLAYING, THAT IS THE END OF THE QUIZ!')

if score >= 15:
    print('\nWell done', name, '! Your final score is', score, '/30')
else:
    print('\nUnlucky', name, 'better luck next time! Final score: ', score, '/30')




