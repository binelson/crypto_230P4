"""
*
*   Title: Cryptography
*
*   Description: Encode or Decode a string given by the user.
*
*   Creator: Ben Nelson
*
"""

import random
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# encodes the phrase provided with the key
def encode(key, phrase):

    newPhrase = ""
    
    for letter in phrase:
        if letter.isalpha() != True:
            newPhrase += letter
        else:
            if letter.isupper():
                newPhrase += key[alpha.find(letter)]
            else:
                newPhrase += key[alpha.find(letter.upper())].lower()

    return newPhrase

# decodes the phrase provided with the key
def decode(key, phrase):

    newPhrase = ""

    for letter in phrase:
        if letter.isalpha() != True:
            newPhrase += letter
        else:
            if letter.isupper():
                newPhrase += alpha[key.find(letter)]
            else:
                newPhrase += alpha[key.find(letter.upper())].lower()

    return newPhrase

# the menu of choices for the user
def menu():
    print "\n\nSECRET DECODER MENU\n"
    print "0) Quit"
    print "1) Encode"
    print "2) Decode"
    print "3) Generate New Key\n"
    return raw_input("What do you want to do? ")

# generates a new key by copying the alphabet, randomly removing a letter
# from it, and adding each letter to make the new key
def generateKey():
    random.seed()
    copy = alpha
    newKey = ""

    while len(newKey) < len(alpha):
        randNum = random.randint(1, len(copy))-1

        newKey += copy[randNum]
        copy = copy.split(copy[randNum])[0] + copy.split(copy[randNum])[1]

    return newKey


def main():
    # starting key
    key =   "XPMGTDHLYONZBWEARKJUFSCIQV"

    keepGoing = True

    # show user the menu and perform their request
    while keepGoing:
        response = menu()
        if response == "1":
            plain = raw_input("text to be encoded: ")
            print encode(key, plain)
        elif response == "2":
            coded = raw_input("code to be decyphered: ")
            print decode(key, coded)
        elif response == "3":
            key = generateKey()
            print "Key Changed!"
            # print "The new key is: " + key
        elif response == "0":
            print "Thanks for doing secret spy stuff with me."
            keepGoing = False    
        else:
            print "I don't know what you want to do..."

main()
