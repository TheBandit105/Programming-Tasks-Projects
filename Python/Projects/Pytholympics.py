from random_word import RandomWords
import time
import random

print('Hello there! Welcome to the Pytholympics!')

time.sleep(2.4)

name = input('\nPlease enter your name to begin: ')

print(f'\nWelcome {name}! Let us begin this Pytholympics journey!')

time.sleep(2.4)

print('\nYou walk along a path and you reach the centre of the Pytholympics park.')

time.sleep(2.4)

while True:
    print('\nTeam Red')
    print('Team Blue')
    print('Team Yellow')
    print('Team Green')

    team_select = input('\nIt is time to choose a team! Select one or type E to exit the game: ')

    if team_select == 'Team Red':
        print(f"\n{name}, you have selected Team Red. Let's continue with our journey!")
        break
    elif team_select == 'Team Blue':
        print(f"\n{name}, you have selected Team Blue. Let's continue with our journey!")
        break
    elif team_select == 'Team Yellow':
        print(f"\n{name}, you have selected Team Yellow. Let's continue with our journey!")
        break
    elif team_select == 'Team Green':
        print(f"\n{name}, you have selected Team Green. Let's continue with our journey!")
        break
    elif team_select == 'E' or team_select == 'e':
        quit()
    else:
        print('\nYou did not select a team provided in the list. Please input a team of choice and try again!')        

time.sleep(2.4)

print('\nThere are many activities for you to do in the Pytholympics park.')
time.sleep(2.4)
print('\nThe activities are divided into 7 islands.')
time.sleep(2.4)

while True:
    print('\nKyriyos Island')
    print('Papoloc Island')
    print('Kuusama Island')
    print('Tykore Island')
    print('Asanaimo Island')

    island_select = input('\nSelect an island to go to or type E to exit: ')

    if island_select == 'Kyriyos Island':

        points = 0
    
        print('\nWelcome to Kyriyos Island. You will solve some detective riddles. You get 5 points for each correct answer and 0 for a wrong answer.')
        time.sleep(3)
        print('\nRiddle 1 - Empty cell mystery')
        time.sleep(3)
        print("\nAndy is put in a cell with a dirt floor and only one window.")
        time.sleep(3)
        print("\nThe window is too high for him to reach. The only thing in the cell is a shovel.")
        time.sleep(3)
        print("\nHe won’t be able to get any food or water and only has two days to escape or he’ll die.")
        time.sleep(3)
        print("\nAndy can’t dig a tunnel because it will take him much longer than two days to do it.")
        time.sleep(3)
        print('\nHow will Andy escape from the cell?\n')

        riddleOneIn = input()

        if riddleOneIn == 'Andy has to use the shovel to create a pile of dirt under the window so he can climb up onto it and escape from the cell.':
            print('\nCorrect! Well done! You are certainly intuitive!')
            points += 5
            print(f'\nPoints: {str(points)}/60')
        else:
            print('\nOops! Wrong answer buddy! Andy has to use the shovel to create a pile of dirt under the window so he can climb up onto it and escape from the cell.')

        time.sleep(3)

        print('\nRiddle 2 - Poisonous drinks')
        time.sleep(3)
        print('\nMarissa and Juliana went out for drinks together.')
        time.sleep(3)
        print('\nThey ordered the same drink.')
        time.sleep(3)
        print('\nJuliana was really thirsty and finished five in the time it took Marissa to finish one.')
        time.sleep(3)
        print('\nThe drinks were poisoned, but only Marissa died. How?\n')

        riddleTwoIn = input()

        if riddleTwoIn == 'The poison was in the ice. Since Marissa’s ice had time to melt, she was poisoned but Juliana wasn’t.':
            print('\nCorrectomundo! Seems like you are increasing your detective skills nicely, my friend.')
            points += 5
            print(f'\nPoints: {str(points)}/60')
        else:
            print('\nSorry my friend that is the incorrect answer. The poison was in the ice. Since Marissa’s ice had time to melt, she was poisoned but Juliana wasn’t.')

        time.sleep(3)

        print('\nRiddle 3 - Suicide or not?')
        time.sleep(3)
        print('\nA dead female body lies at the bottom of a multistory building.')
        time.sleep(3)
        print('\nIt looks as though she committed suicide by jumping from one of the floors.')
        time.sleep(3)
        print('\nWhen the detective arrives, he goes to the first floor of the building, opens the closed window, and flips a coin towards the floor.')
        time.sleep(3)
        print('\nHe goes to the second floor and does the exact same thing.')
        time.sleep(3)
        print('\nHe continues to do this until he gets to the top floor of the building.')
        time.sleep(3)
        print('\nWhen he comes back down, he states that it was a murder and not a suicide.')
        time.sleep(3)
        print('\nHow does he know that?\n')

        riddleThreeIn = input()

        if riddleThreeIn == 'She couldn’t have jumped from any of the floors because when the detective went to each floor, all of the windows were closed.':
            print('\nGreat work! Looks like you are getting the hang of this.')
            points += 5
            print(f'\nPoints: {str(points)}/60')
        else:
            print('\nUh Oooh! Looks like you need to improve on your skills. She couldn’t have jumped from any of the floors because when the detective went to each floor, all of the windows were closed.')

        time.sleep(3)

        print('\nRiddle 4 - Love at a funeral')
        time.sleep(3)
        print('\nA girl is at the funeral of her mother.')
        time.sleep(3)
        print('\nShe meets a nice guy that she didn’t know who also was at the funeral and they hit it off.')
        time.sleep(3)
        print('\nShe was busy at the funeral and didn’t have time to ask him for his number before he left.')
        time.sleep(3)
        print('\nShe tried really hard to track him down, but no one knew who he was or how to contact him.')
        time.sleep(3)
        print('\nA few days later her sister dies and the police suspect it to be a murder.')
        time.sleep(3)
        print('\nWho killed her sister?\n')

        riddleFourIn = input()

        if riddleFourIn == 'She killed her sister. She was hoping that if someone else in her family died, the man she met at her mother’s funeral would show up again.':
            print('\nExcellent! Keep it up!')
            points += 5
            print(f'\nPoints: {str(points)}/60')
        else:
            print('\nOh snap! Try to think about the riddle next time. She killed her sister. She was hoping that if someone else in her family died, the man she met at her mother’s funeral would show up again.')

        time.sleep(3)

        print('\nRiddle 5 - Stolen ring')
        time.sleep(3)
        print('\nNicole went to the police to report that someone had stolen her vintage ring.')
        time.sleep(3)
        print('\nWhen the police got to her house they notice that the window was broken,')
        time.sleep(3)
        print('\nthere was a total mess inside, and there were dirty footprints on the carpet.')
        time.sleep(3)
        print('\nBut, there were no other signs of a break-in.')
        time.sleep(3)
        print('\nThe next day, the police arrested Nicole for fraud.')
        time.sleep(3)
        print('\nWhy?\n')

        riddleFiveIn = input()

        if riddleFiveIn == 'As soon as the police got to the “crime scene,” they knew that Nicole has most likely staged the break-in. The glass from the broken window was all outside of the house, meaning that it had been broken from the inside.':
            print('\nFantastic work! On your way to becoming a pro!')
            points += 5
            print(f'\nPoints: {str(points)}/60')
        else:
            print('\nNope, better luck next time. As soon as the police got to the “crime scene,” they knew that Nicole has most likely staged the break-in.\nThe glass from the broken window was all outside of the house, meaning that it had been broken from the inside.')
            
        time.sleep(3)

        print('\nRiddle 6 - Thief at sea')
        time.sleep(3)
        print('\nA Japanese ship was leaving the port and on its way to open sea.')
        time.sleep(3)
        print('\nThe captain went to go oil some parts of the ship and took his ring off so it wouldn’t get damaged.')
        time.sleep(3)
        print('\nHe left it on the table next to his bunk.')
        time.sleep(3)
        print('\nWhen he returned, it was missing.')
        time.sleep(3)
        print('\nHe had suspected three crew members could be guilty and asked them what they had been doing for the ten minutes that he had been gone.')
        time.sleep(3)
        print('\nThe cook said, “I was in the kitchen preparing tonight’s dinner.”')
        time.sleep(3)
        print('\nThe engineer said, “I was working in the engine room making sure everything was running smoothly.”')
        time.sleep(3)
        print('\nThe seaman said, “I was on the mast correcting the flag because someone had attached it upside down by mistake.”')
        time.sleep(3)
        print('\nThe captain immediately knew who it was. How?\n')

        riddleSixIn = input()

        if riddleSixIn == 'It was clearly the seaman. It was a Japanese ship and a Japanese flag is white with a single red dot in the middle. It can’t be hung upside down.':
            print('\nBrilliant! Keep it up!')
            points += 5
            print(f'\nPoints: {str(points)}/60')
        else:
            print('\nUnlucky. It was clearly the seaman. It was a Japanese ship and a Japanese flag is white with a single red dot in the middle. It can’t be hung upside down.')

        time.sleep(3)

        print('\nRiddle 7 - Murder at school')
        time.sleep(3)
        print('\nOn the first day of school, someone murdered a history teacher.')
        time.sleep(3)
        print('\nThere were four people at the school that the police suspected had done it: the landscaper, a math teacher, a basketball coach, and the principal.')
        time.sleep(3)
        print('\nThese were their alibis:')
        time.sleep(3)
        print('\nThe landscaper said he was outside mowing the lawn.')
        time.sleep(3)
        print('\nThe math teacher said he was giving a mid-year test.')
        time.sleep(3)
        print('\nThe basketball coach said he was running practice drills with his players.')
        time.sleep(3)
        print('\nThe principal said she was in her office.')
        time.sleep(3)
        print('\nAfter giving their alibies, the police arrested the killer immediately. ')
        time.sleep(3)
        print('\nWho killed the history teacher and how did the police know?\n')

        riddleSevenIn = input()

        if riddleSevenIn == 'The math teacher killed the history teacher. He claimed that he was giving a mid-year test, but it was the first day of school.':
            print('\nAwesome! You are already semi-pro!')
            points += 5
            print(f'\nPoints: {str(points)}/60')
        else:
            print('\nOh flip, that is not right. The math teacher killed the history teacher. He claimed that he was giving a mid-year test, but it was the first day of school.')

        time.sleep(3)

        print('\nRiddle 8 - Poisonous pills')
        time.sleep(3)
        print('\nA serial killer kidnapped five different people and sat them down each with two pills in their hand and a glass of water.')
        time.sleep(3)
        print('\nHe told them each to take one pill but warned them that one was poisonous and the other was harmless.')
        time.sleep(3)
        print('\nWhichever pill the victim didn’t take, the serial killer would take.')
        time.sleep(3)
        print('\nEvery victim somehow chose the poisonous pill and died.')
        time.sleep(3)
        print('\nHow did the serial killer get them all to take the poisonous pill?\n')

        riddleEightIn = input()

        if riddleEightIn == 'Neither of the pills was poisonous. The poison was in the water that all the victims used to swallow their pill.':
            print('\nWow! Nice one buddy!')
            points += 5
            print(f'\nPoints: {str(points)}/60')
        else:
            print('\nIncorrect. Neither of the pills was poisonous. The poison was in the water that all the victims used to swallow their pill.')

        time.sleep(3)

        print('\nRiddle 9 - Honeymoon mystery')
        time.sleep(3)
        print('\nA couple went to Hawaii for their honeymoon.')
        time.sleep(3)
        print('\nUnfortunately, the husband returned home alone because his wife had died in a horrible boating accident.')
        time.sleep(3)
        print('\nThe police contacted the travel agent he booked the trip with and arrested him for murdering his wife.')
        time.sleep(3)
        print('\nHow did they know he did it?\n')

        riddleNineIn = input()

        if riddleNineIn == 'The travel agent revealed that he had only booked a one-way ticket for his wife.':
            print('\nSuperb! You could be my teacher one day in criminology!')
            points += 5
            print(f'\nPoints: {str(points)}/60')
        else:
            print('\nToo bad. The travel agent revealed that he had only booked a one-way ticket for his wife.')

        time.sleep(3)

        print('\nRiddle 10 - Science case')
        time.sleep(3)
        print('\nA chemist was murdered in his own lab.')
        time.sleep(3)
        print('\nThe only evidence was a piece of paper that had the names of chemical substances written on it.')
        time.sleep(3)
        print('\nThe substances were nickel, carbon, oxygen, lanthanum, and sulfur.')
        time.sleep(3)
        print('\nThe chemist only had three people come by his lab on the day of the murder: fellow scientist Claire, his nephew Nicolas, his wife, and his friend Marc.')
        time.sleep(3)
        print('\nThe police arrested the murderer right away.')
        time.sleep(3)
        print('\nHow did they know who it was?\n')

        riddleTenIn = input()

        if riddleTenIn == 'There was a very obvious clue on the piece of paper. If you combine the abbreviations of the chemical substances on the paper, you’ll get a name: Ni-C-O-La-S.' or \
           riddleTenIn == 'If you combine the abbreviations of the chemical substances on the paper, you’ll get a name: Ni-C-O-La-S.':
            print('\nOh wow, I think I ran out of words to say!')
            points += 5
            print(f'\nPoints: {str(points)}/60')
        else:
            print('\nOh dear, the chemistry lab is not for you. If you combine the abbreviations of the chemical substances on the paper, you’ll get a name: Ni-C-O-La-S.')

        time.sleep(3)

        print('\nRiddle 11 - Recorded last words')
        time.sleep(3)
        print('\nA man was found on the floor dead with a cassette recorder in one hand and a gun in the other.')
        time.sleep(3)
        print('\nWhen the police arrive at the scene they pressed play on the recorder.')
        time.sleep(3)
        print('\nIt was the man’s voice.')
        time.sleep(3)
        print('\nHe said, “I have nothing else to live for. I can’t go on,” followed by the sound of a gunshot.')
        time.sleep(3)
        print('\nAfter listening, the police knew that this was a murder, not a suicide.')
        time.sleep(3)
        print('\nHow?\n')

        riddleElevenIn = input()

        if riddleElevenIn == 'If the dead man had killed himself, he wouldn’t have been able to press the reverse button on the cassette recorder.':
            print('\nDayum, you are on a roll! Epic!')
            points += 5
            print(f'\nPoints: {str(points)}/60')
        else:
            print('\nCome on you still got this. If the dead man had killed himself, he wouldn’t have been able to press the reverse button on the cassette recorder.')

        time.sleep(3)

        print("\nAlright, you've made it this far, you have one final riddle left to do before you complete this island! Here it comes...")

        time.sleep(3)

        print('\nRiddle 12 - Guilty in court')
        time.sleep(3)
        print('\nA woman was in court for killing her husband.')
        time.sleep(3)
        print('\nShe said she wasn’t guilty and that she dearly missed him.')
        time.sleep(3)
        print('\nIn the closing statement, the woman’s lawyer stands up and says, “Her husband was just missing.')
        time.sleep(3)
        print('\nEveryone look at the doors.')
        time.sleep(3)
        print('\nHe’s going to walk through them in about 30 seconds.”')
        time.sleep(3)
        print('\nThe entire jury stares at the doors waiting for waiting for this woman’s husband to walk through the doors.')
        time.sleep(3)
        print('\nThe lawyer and the woman stare at the jury.')
        time.sleep(3)
        print('\nThe lawyer concludes by saying, “See! If you were so sure she killed her husband, you wouldn’t be watching that door!”')
        time.sleep(3)
        print('\nThe jury immediately gave a guilty verdict. Why?\n')

        riddleTwelveIn = input()

        if riddleTwelveIn == 'The woman was watching the jury and not the doors because she knew that her husband wouldn’t walk through them because she had killed him. If she has really missed him like she said, she would have been watching the doors.':
            print('\nYou know you stuff. You are now an expert at this!')
            points += 5
            print(f'\nPoints: {str(points)}/60')
        else:
            print('\nHmmm... I think you need retraining. The woman was watching the jury and not the doors because she knew that her husband wouldn’t walk through them because she had killed him.\n If she has really missed him like she said, she would have been watching the doors.')

        time.sleep(3)

        print(f'\nFINAL SCORE: {str(points)}/60')

    elif island_select == 'Papoloc Island':

        print('\nWelcome to Papoloc Island. You will solve some quick sums. You get 5 points for each correct answer and 0 for a wrong answer.')
        time.sleep(3)

        questionNo = 1
        score = 0

        while questionNo <= 12:
            operations = ['+','-','*','/']
            randomNum1 = random.randint(0,100)
            randomNum2 = random.randint(0,100)
            randomOp = random.choice(operations)

            print(f'\n Q{str(questionNo)}. {str(randomNum1)}{randomOp}{str(randomNum2)} = ?')
            ans = float(input())

            if ans == round((eval(str(randomNum1) + randomOp + str(randomNum2))),2):
                print('\nCorrect!')
                score += 5
            else:
                print('\nIncorrect!')

            questionNo += 1

        print(f'\nFINAL SCORE = {score}/60')
    
    elif island_select == 'Kuusama Island':
        
        print('\nWelcome to Kuusama Island. You will complete a pop quiz. You get 5 points for each correct answer and 0 for a wrong answer.')
        time.sleep(3)

        score = 0

        print('\n1. What was Meta Platforms Inc formerly known as?')
        print('A.Mastodon\nB.Facebook')
        print('C.WhatsApp\nD.Instagram')

        ans = input('\nAns: ')

        if ans == 'B' or 'b':
            print('\nCorrect!')
            score += 5
        else:
            print('\nIncorrect!')
        
        time.sleep(3)

        print('\n2. Which English city is known as the Steel City?')
        print('A.Treeton\nB.Bradford')
        print('C.Leeds\nD.Sheffield')

        ans = input('\nAns: ')

        if ans == 'D' or 'd':
            print('\nCorrect!')
            score += 5
        else:
            print('\nIncorrect!')
        
        time.sleep(3)

        print('\n3. Which former British colony was given back to China in 1997?')
        print('A.Taiwan\nB.Weihai')
        print('C.Hong Kong\nD.Brunei')

        ans = input('\nAns: ')

        if ans == 'C' or 'c':
            print('\nCorrect!')
            score += 5
        else:
            print('\nIncorrect!')
        
        time.sleep(3)

        print('\n4. The logo for luxury car maker Porsche features which animal?')
        print('A.Horse\nB.Eagle')
        print('C.Equus\nD.Akhal-Teke')

        ans = input('\nAns: ')

        if ans == 'A' or 'a':
            print('\nCorrect!')
            score += 5
        else:
            print('\nIncorrect!')
        
        time.sleep(3)

        print('\n5. Which element is said to keep bones strong?')
        print('A.Iron\nB.Sodium')
        print('C.Calcium\nD.Potassium')

        ans = input('\nAns: ')

        if ans == 'C' or 'c':
            print('\nCorrect!')
            score += 5
        else:
            print('\nIncorrect!')
        
        time.sleep(3)

        print('\n6. What does CIA stand for?')
        print('A.Common iliac artery\nB.Central Intelligence Agency')
        print('C.Certified Internal Auditor\nD.Cleveland Institute of Art')

        ans = input('\nAns: ')

        if ans == 'B' or 'b':
            print('\nCorrect!')
            score += 5
        else:
            print('\nIncorrect!')
        
        time.sleep(3)

        print('\n7. Suriname is located on which continent?')
        print('A.Asia\nB.North America')
        print('C.Europe\nD.South America')

        ans = input('\nAns: ')

        if ans == 'D' or 'd':
            print('\nCorrect!')
            score += 5
        else:
            print('\nIncorrect!')
        
        time.sleep(3)

        print('\n8. In tennis, what piece of fruit is found at the top of the men’s Wimbledon trophy?')
        print('A.Pineapple\nB.Banana')
        print('C.Apple\nD.Orange')

        ans = input('\nAns: ')

        if ans == 'A' or 'a':
            print('\nCorrect!')
            score += 5
        else:
            print('\nIncorrect!')
        
        time.sleep(3)

        print('\n9. Haematology is the study of what?')
        print('A.Plasma\nB.The blood.')
        print('C.Bile\nD.Circulation')

        ans = input('\nAns: ')

        if ans == 'B' or 'b':
            print('\nCorrect!')
            score += 5
        else:
            print('\nIncorrect!')
        
        time.sleep(3)

        print('\n10. What is the main ingredient in guacamole?')
        print('A.Onion\nB.Tomato')
        print('C.Avocado\nD.Coriander')

        ans = input('\nAns: ')

        if ans == 'C' or 'c':
            print('\nCorrect!')
            score += 5
        else:
            print('\nIncorrect!')
        
        time.sleep(3)

        print('\n11. Which body sets the interest rates in the UK?')
        print('A.HM Revenue & Customs\nB.Bank of England')
        print('C.Global Bank\nD.Natwest')

        ans = input('\nAns: ')

        if ans == 'B' or 'b':
            print('\nCorrect!')
            score += 5
        else:
            print('\nIncorrect!')
        
        time.sleep(3)

        print('\n12. How many lives is a cat said to have?')
        print('A.9\nB.11')
        print('C.7\nD.13')

        ans = input('\nAns: ')

        if ans == 'A' or 'a':
            print('\nCorrect!')
            score += 5
        else:
            print('\nIncorrect!')
        
        time.sleep(3)

        print(f'\nFINAL SCORE = {score}/60')

    elif island_select == 'Tykore Island':

        print('\nWelcome to Tykore Island. A random number will be chosen between 0 and 50. You get 5 points for each correct answer \
        and lose a life for each wrong answer. \n If lives reaches 0, then the game ends.')
        time.sleep(3)

        lives = 5
        score = 0

        while lives > 0:
            
            invalid = 'abcdefghijklmnopqrstuvwxyz'

            randomNum = random.randint(0,50)

            print(f'\nLives remaining: {lives}')
            print('\n Guess my number: ')
            ans = input()

            if ans in invalid:
                print('\nInvalid input, please input a number between 0 and 50.')
            elif int(ans) == randomNum:
                print('\nCorrect!')
                score += 5
                time.sleep(3)
            elif int(ans) > 50 or int(ans) < 0: 
                print('\nInvalid input, please input a number between 0 and 50.')
            else:
                print(f'\nIncorrect! My number was {randomNum}. You lose a life!')
                lives -= 1
                time.sleep(3)

        print('\nGAME OVER!')
        print(f'\nFINAL SCORE = {score}')
    
    elif island_select == 'Asanaimo Island':

        print('\nWelcome to Asanaimo Island. This is word guess')
        time.sleep(3)

        r = RandomWords()
        word = r.get_random_word()

        lives = 7
        guesses = ''
    
        print('Guess the characters: ')
        
        while lives > 0:

            fail = 0

            for i in word:
                if i in guesses:
                    print(f'{i} ', end = '')
                else:
                    print('_ ', end = '')
                    fail += 1
            
            if fail == 0:
                print(f'\n\nYou win! The word is: {word}')
                break

            print(f'\nLives Remaining: {lives}')
            print(f'Guesses: {guesses}')    
            guess = input('\nGuess the characters: ')

            guesses += guess

            if guess not in word:
                lives -= 1
                
                if lives > 1:
                    print(f'\nWrong! You have {lives} lives remaining!')
                elif lives == 1:
                    print(f'\nWrong! You have {lives} life remaining!')
                elif lives == 0:
                    print(f'\nGAME OVER! You have ran out of lives! The word was {word}.')
                    break

    elif island_select == 'E' or island_select == 'e':
        break
    else:
        print('\nYou did not select an island or type E to exit! Please input the appropriate option and try again!')

    

    
    


