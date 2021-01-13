import random

# What does the user want to find the answer to
userneed = input("What do you want to get an answer to? ")

# All the 8-ball possible answers
ball_choice = ["● It is certain", "● It is decidedly so", "● Without a doubt", "● Yes definitely", "● You may rely on it", "● As I see it, yes", "● Most likely", "● Outlook good", "● Yes", "● Signs point to yes", "● Don't count on it", "● My reply is no", "● My sources say no", "● Outlook not so good", "● Very doubtful", "● Reply hazy try again", "● Ask again later", "● Better not tell you now", "● Cannot predict now", "● Concentrate and ask again"]

# A random choice from the given answers
print (random.choice(ball_choice))