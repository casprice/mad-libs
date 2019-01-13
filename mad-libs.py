print("Let's play some Mad Libs!")

while True:
    adj1 = input('\nEnter a relative adjective: ')
    adj2 = input('\nEnter an adjective: ')
    adj3 = input('\nEnter an adjective: ')
    adj4 = input('\nEnter an adjective: ')
    name1 = input('\nEnter the name of someone in the room: ')
    adj5 = input('\nEnter an adjective: ')
    adj6 = input('\nEnter an adjective: ')
    verb1 = input('\nEnter a verb ending in "ed": ')
    body_part = input('\nEnter a body part: ')
    verb2 = input('\nEnter a verb ending in "ing": ')
    noun1 = input('\nEnter a plural noun: ')
    noun2 = input('\nEnter a noun: ')
    adv = input('\nEnter an adverb: ')
    verb3 = input('\nEnter a verb: ')
    verb4 = input('\nEnter a verb: ')
    adj7 = input('\nEnter a relative adjective: ')
    name2 = input('\nEnter the name of someone else in the room: ')

    print('\n\nLetter From Camp\n')
    print("Dear " + adj1 + ",\n" + "I am having a(n) " + adj2 + " time at camp.")
    print("The counselour is " + adj3 + " and the food is " + adj4 + ". ")
    print("I met " + name1 + " and we became " + adj5 + " friends. ")
    print("Unfortunately, " + name1 + " is " + adj6 + " and I " + verb1+ " my " + body_part + " so we couldn`t go " + verb2 + " like everybody else. ")
    print("I need more " + noun1 + " and a " + noun2 + " sharpener, so please " + adv + " " + verb3 + " more when you " + verb4 + " back. \n")
    print("Your " + adj7 + ",\n" + name2)

    print('\n\nGreat Mad Lib!')
    response = ''
    while response != 'yes' and response != 'no':
        print('\nWould you like to play again? (yes/no)')
        response = input()
        if response == 'yes' or response == 'no':
            break
        print("Sorry, I didn't quite get that.")
    if response == 'no':
        break

print('Thanks for playing!')
