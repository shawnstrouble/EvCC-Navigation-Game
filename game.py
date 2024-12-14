print("EVERETT COMMUNITY COLLEGE ADVENTURE\n+---------------------------------+")

careers = ['Computing and IT', 'Science', 'Engineering', 'Health Sciences']
characters = ['Wizard', 'Thief', 'Knight']

name = input('Hello! Welcome to your EvCC Adventure. What is your name?\n')
print('Nice to meet you, ' + name + '!')

userCharacter = int(input('Which fantasy character would you like to play as? Here is your selection:\n\n' + '1 - ' + characters[0] + ': Gets a cool robe and can use magic.\n' + '2 - ' + characters[1] + ': Good at sleight of hand and collecting objects.\n' + '3 - ' + characters[2] + ': Gets a shiny suit of armor and a sword.\n\nPlease select your character by number.\n')) - 1

if userCharacter > 2:
    while userCharacter > 2:
        print('That number is not listed. Please try again.')
        userCharacter = int(input())-1

print('So, ' + characters[userCharacter] + ' ' + name + ', Which career path would you like to take?\n\nHere is your selection:')
count = 0
for i in careers:
    count += 1
    print(str(count) + ' ' + i)
print('Please select by number.')
userCareer = int(input())-1

if userCareer > 3:
    while userCareer > 3:
        print('That number is not listed. Please try again.')
        userCareer = int(input())-1

print('You have selected ' + careers[userCareer] + ' as your pathway at EvCC.\nThis is your first step!')
input('Press enter to proceed to step 2!\n')
print('Step Two is to apply. Apply using your selected path.')
input('Press enter to submit your application.\n')
print('You have been accepted!\n\nStep Three: finding ways to pay for college.\nYou have a lot of options when it comes to funding. \nYou can choose financial aid, work study as an extra way to pay, as well as scholarships and grants. \nThere is also, of course, getting loans or paying out of pocket.')
input('Once you have figured out funding, press enter to continue.\n')
print('Step Four: please complete orientation.')
input('Once you have completed orientation, press enter.\n')
print('Step Five: establish placement. This will help match you with the classes you should take.')
input('Press enter to establish placement.\n')
print('\nStep Six: entry advising. This will help you learn what classes you need.')
input('Press enter to finish advising.\n')

if userCareer == 0:
    print('Your reccomended classes are STEM 101, STEM 103, and an English course.')
elif userCareer == 1:
    print('Your reccomended classes are STEM 101, STEM 102, and a Math course.')
elif userCareer == 2:
    print('Your reccomended classes are STEM 101, ENGR 111, and a Math course.')
elif userCareer == 3:
    print('Your reccomended classes are STEM 101, STEM 102, and an English course.')

print('Now that you know your classes, your last step is to register.')
input('Press enter to register and pay for your classes.\n')
print('\nYou have registered and are now enrolled at EvCC! I hope you enjoy your classes, ' + characters[userCharacter] + ' ' + name + '!')
print('\n+---------THE END--------+')
