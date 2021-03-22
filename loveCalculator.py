import time

print('''
LOVE CALCULATOR

In love? We’ve all been there. Have you tried asking them? Of course not!
You’ve come to the right place.
I’ll tell you how compatible you two are!
''')

user1 = input("What is your name? ").lower()
user2 = input("What is the name of the person you love? ").lower()

score = 0
vowels = ["a", "e", "i", "o", "u", "y"]
consonants = ["b", "c", "d", "f", "g", 'h', 'j', 'k', 'l', 'm',
              'n', 'l', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
vowels_in_user1 = 0
vowels_in_user2 = 0

user1_letters = []
user2_letters = []


for letter in user1:
    user1_letters.append(letter)
for letter in user2:
    user2_letters.append(letter)

# both names have the same amount of consonants/vowels (work!) put in a function


def letters(user1, user2, letters):
    user1_consonants = {}
    user2_consonants = {}
    global score
    for i in range(len(user1)):
        if (user1[i] in letters):
            try:
                user1_consonants[user1[i]] += 8
            except KeyError:
                user1_consonants[user1[i]] = 8
    for i in range(len(user2)):
        if (user2[i] in letters):
            try:
                user2_consonants[user2[i]] += 8
            except KeyError:
                user2_consonants[user2[i]] = 8
    for key in user1_consonants:
        if key in user2_consonants:
            score += min([user1_consonants[key], user2_consonants[key]])

    user1_vowels = {}
    user2_vowels = {}
    for i in range(len(user1)):
        if (user1[i] in letters):
            try:
                user1_vowels[user1[i]] += 8
            except KeyError:
                user1_vowels[user1[i]] = 8
    for i in range(len(user2)):
        if (user2[i] in letters):
            try:
                user2_vowels[user2[i]] += 8
            except KeyError:
                user2_vowels[user2[i]] = 8
    for key in user1_vowels:
        if key in user2_vowels:
            score += min([user1_vowels[key], user2_vowels[key]])


letters(user1, user2, consonants)
letters(user1, user2, vowels)


# if both names start with the same letter (Works!)
if user1[0] == user2[0]:
    score = score + 15

# if first letter in user 2 is in user1 name [Works!]
if user2_letters[0] in user1_letters:
    score = score + 30

# if the names have the same amount of characters, plus 20 points (WORKS!)
if len(user1) == len(user2):
    score = score + 20

# if both users name has an L O V or E in it (Works!)
if "l" in user1:
    score = score + 3
elif "o" in user1:
    score = score + 3
elif "v" in user1:
    score = score + 3
elif "e" in user1:
    score = score + 3

if "l" in user2:
    score = score + 3
elif "o" in user2:
    score = score + 3
elif "v" in user2:
    score = score + 3
elif "e" in user2:
    score = score + 3

# make into a function, accept a score varible, based off the score varible = prints message
# look into putting messages in a list


def zero():
    print("\n" + str(score) + "%: Absolutely no chance. Like ever... ever ever. I'm literally mad you asked about this and I'm a bot.\n")


def one():
    print("\n" + str(score) + "%: Yeeeeeaaaaaahhhhhhhhh—nnnnnooooo.\n")


def two():
    print("\n" + str(score) + "%: I’d be surprised if you even to the friend zone.\n")


def three():
    print("\n" + str(score) +
          "%: I mean, if this was a school grade, it’d only be like a F minus minus... minus?\n")


def four():
    print("\n" + str(score) +
          "%: I mean… not TERRIBLE... definitely not good though.\n")


def five():
    print("\n" + str(score) + "%: I haven't figured out what to write here yet.\n")


def six():
    print("\n" + str(score) +
          "%: At least you’re on the positive side! I’ll give it a Potential2Grow sticker.\n")


def seven():
    print("\n" + str(score) + "%: I definitely see sparks. ;)\n")


def eight():
    print("\n" + str(score) +
          "%: You’re either on the first date, or in the Best-Friend stage. Keep at it.\n")


def nine():
    print("\n" + str(score) + "%: Yaaaaassssssss!!! This. Just. This.\n")


def ten():
    print("\n" + str(score) +
          "%: RED ALERT! RED ALERT! THESE TWO ARE FIRE TOGETHER!!\n")


def perfect():
    print("\n" + str(score) + "%: < 3 Always + Forver < 3\n")


def result():
    global score
    if score == 0:
        zero()
    elif score <= 10:
        one()
    elif score <= 20:
        two()
    elif score <= 30:
        three()
    elif score <= 40:
        four()
    elif score <= 50:
        five()
    elif score <= 60:
        six()
    elif score <= 70:
        seven()
    elif score <= 80:
        eight()
    elif score <= 90:
        nine()
    elif score <= 99:
        ten()
    elif score == 100:
        perfect()


print("\nCalculating...\n")
time.sleep(3)
result()
# if score == 0:
#    print(str(score) + "%: Absolutely no chance. Like ever... ever ever. I'm literally mad you asked about this and I'm a bot.")
# elif score <= 10:
#    print(str(score) + "%: Yeeeeeaaaaaahhhhhhhhh—nnnnnooooo.")
# elif score <= 20:
#    print(str(score) + "%: I’d be surprised if you even to the friend zone.")
# elif score <= 30:
#    print(str(score) + "%: I mean, if this was a school grade, it’d only be like a F minus minus... minus?")
# elif score <= 40:
#    print(str(score) + "%: I mean… not TERRIBLE... definitely not good though.")
# elif score <= 50:
#    print(str(score) + "%: I haven't figured out what to write here yet.")
# elif score <= 60:
#    print(str(score) + "%: At least you’re on the positive side! I’ll give it a Potential2Grow sticker.")
# elif score <= 70:
#    print(str(score) + "%: I definitely see sparks. ;)")
# elif score <= 80:
#    print(str(score) + "%: You’re either on the first date, or in the Best-Friend stage. Keep at it.")
# elif score <= 90:
#    print(str(score) + "%: Yaaaaassssssss!!! This. Just. This.")
# elif score <= 99:
#    print(str(score) + "%: RED ALERT! RED ALERT! THESE TWO ARE FIRE TOGETHER!!")
# elif score == 100:
#    print(str(score) + "%: <3 Always + Forever <3")
