

def collatz(number):
    if number%2 == 0:
        answer = number//2
        print(answer)
        return answer
    else:
        answer = 3 * number + 1
        print(answer)
        return answer

try:
    user_says = int(input("Give me a number"))

    while user_says != 1:
        user_says = collatz(user_says)
except ValueError:
    print("That's not a number, please give me a number")

