#!/usr/bin/env python
# coding: utf-8

# ## Challenges

# ### Are we prepared for the weather?
# 
# You are considered to be prepared for the weather if:
# 
# - I have an umbrella...
# - or if the rain isn't too heavy (below 3) and I have a hood...
# - otherwise, I'm still fine unless it's raining and it's a workday
# 
# Write a code that validates your rediness for the climate conditions. It should return True or False.

# In[5]:


## Consider the values below to test your solution. 
##Feel free to change these values in order to test the code to validate it covers all the possible scenarios.

have_umbrella = True
rain_level = 1.0
have_hood = True
is_workday = True

if (have_umbrella) or (rain_level < 3 and have_hood):
    print("I am prepared for the weather.")
else:
    if (rain_level > 0) and (is_workday):
        print("I came unprepared for the weather.")
    else:
        print("I'm still fine")
    


# ### Odd or Even?
# 
# Write some code that prints out a different message for each number in the list below depending on whether it is odd or even.
# 

# In[6]:


challenge = [2,5,76,89,77,103,24,65,66,12,1,0,19]

for i in challenge:
    if(i % 2) == 0:
        print("{0} is Even number".format(i))  
    else:
        print("{0} is Odd number".format(i)) 
        


# ### Find the hidden message
# 
# Write a code that can find the hidden message in the text by extracting the uppercase letters.
# 
# _"mr. and mrs. dursley, of number four, prIvet drive, were proud to say that they were perfectLy normal, thank you very much. they were the last peOple you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense. mr. dursley was the director of a firm called grunnings, which made drills. he was a big, beefy man with hardly any neck, although he did have a Very largE mustache. mrs. dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she sPent so much of her time craning over garden fences, spYing on THe neighbors. the ursleys had a small sOn called dudley and in their opinion there was No finer boy anywhere."_
# 
# Rowling, J. K. (2014). Harry potter and the philosopher’s stone. Bloomsbury Childrens Books.
# 
# 

# In[13]:


message = 'mr. and mrs. dursley, of number four, prIvet drive, were proud to say that they were perfectLy normal, thank you very much. they were the last peOple you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense. mr. dursley was the director of a firm called grunnings, which made drills. he was a big, beefy man with hardly any neck, although he did have a Very largE mustache. mrs. dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she sPent so much of her time craning over garden fences, spYing on THe neighbors. the dursleys had a small sOn called dudley and in their opinion there was No finer boy anywhere.'
##Your code:

''.join([a for a in message if a.isupper()])


# In[14]:


''.join(a for a in message if a.isupper())


# ### Mario Kart red shell simulator
# The next exercise will feature a Mario Kart race where a player uses the Red Shell. When used, it hits the competitor in front of the payer who shot it and the places in the leaderboard are switched. Complete the function below to implement the Red Shell's effect. 
# 
# Note: 
# - If the first player shoots the Shell, there will be no changes in the leaderboard.
# - Remember that the indexes in lists start in 0.

# In[1]:


leaderboard = ['Mario', 'Luigi', 'Peach', 'Daisy', 'Yoshi', 'Toad', 'Toadette', 'Rosalina']
##Remember that in lists, the first possition is 0
##
print('The positions of the race are the following:', leaderboard)

##define the position of the player that is going to shoot the shell(1st, 2nd, 3rd place)
shooter = 2

print('The position',shooter ,'in the race,',leaderboard[shooter -1], ', shoot a Red shell!!!')
##Your code:

leaderboard[0], leaderboard[shooter -1] = leaderboard[0 + 1], leaderboard[0]

print('Now the leaderboard is:', leaderboard)


# ### Keyword finder
# You have collected a series of articles and you would like to filter them for the most relevant regarding a particluar word. 
# 
# The code should meet the following criteria:
# 
# - Do not include documents where the keyword string shows up only as a part of a larger word. For example, if you are looking for the keyword “closed”, you would not include the string “enclosed.”
# - Not distintion between upper case from lower case letters. Phrases “Closed the case.” would be included when the keyword is “closed”
# - Periods or commas shouldn't affect what is matched. “It is closed.” or “It is closed,” would be included when the keyword is “closed”. You can assume there are no other types of punctuation.
# - It should return the amount of times the keyword was found in each article.
# 
# (https://docs.python.org/3/library/stdtypes.html)

# In[19]:


##Test your solution considering as an input the list below that contains an extraction of three articles
articles = [['An Avro customer in a household using a typical amount of gas and electricity, who got a fixed rate deal in August, would have been paying £1,087 a year, according to price comparison site Uswitch. In March, they could have got a deal costing £920 a year.'],
           ['But attention is increasingly falling on those who havent had it. Speculation has centred on which dancers on Strictly Come Dancing have so far not taken up the offer, as well as how many Premier League footballers are potentially unvaccinated.'],
           ['Mrs Merkel has been proclaimed by Forbes as the most powerful woman in the world for 10 years running. There is a whole generation in Germany that has never known anything other than a woman leader. Her position has been symbolically important for womens representation, and she is known for bringing women into key positions. For example, she supported Ursula von der Leyen, the first female German defence minister and European Commission president.']]


# In[61]:


keyword = 'avro'
##Your code:

a0 = str(articles[0]).lower()
a1 = str(articles[1]).lower()
a2 = str(articles[2]).lower()

print('In article 0 The keyword: ' + keyword + ' was found: ' + str(a0.count(keyword)))
print('In article 1 The keyword: ' + keyword + ' was found: ' + str(a1.count(keyword)))
print('In article 2 The keyword: ' + keyword + ' was found: ' + str(a2.count(keyword)))


# In[ ]:





# In[ ]:




