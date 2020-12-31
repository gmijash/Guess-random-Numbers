import random

num_guesses = 0
val_range = input('Enter the range of values for the guessing game:').split()
val_range.sort()
random.seed(900)
correct_num = random.randint(int(val_range[0]), int(val_range[1]))

while True:
    user_int = int(input("Enter a guess between {} and {} :".format(val_range[0], val_range[1])))
    if user_int == correct_num:
        num_guesses += 1
        print("{} is correct!".format(correct_num))
        print('Total guesses was {}'.format(num_guesses))
        break
    elif int(val_range[0]) <= user_int < correct_num:
        print("{} is too low".format(user_int))
        num_guesses +=1
    elif int(val_range[1])>= user_int > correct_num:
        print("{} is too high.".format(user_int))
        num_guesses += 1
    else:
        print("Out of range,try again")
