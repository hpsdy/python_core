# This is a guess the number game.
import random
import gettext

guessesTaken = 0

name = 'text'
dir = './share/locale'
lang = ['zh_CN']
es = gettext.translation(name,localedir=dir,languages=lang)
print(es)
_ = es.gettext

#gettext.bindtextdomain(name, dir)
#gettext.textdomain(name)
#_ = gettext.gettext
print(_('Hello! What is your name?'))
myName = input()

number = random.randint(1, 20)
print(_('Well, %s, I am thinking of a number between 1 and 20.') % (myName))

while guessesTaken < 6:
    print(_('Take a guess.'))
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print(_('Your guess is too low.'))

    if guess > number:
        print(_('Your guess is too high.'))

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print(_('Good job, %s! You guessed my number in %s guesses!') % (myName, guessesTaken))

if guess != number:
    number = str(number)
    print(_('Nope. The number I was thinking of was %s.') % (number))