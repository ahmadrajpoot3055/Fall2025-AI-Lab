import random

def fizzbuzz_value(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return str(num)

def play_game():
    start = random.randint(1, 10)
    current = start
    previous = start
    score = 0
    rounds = 0

    print("Welcome to the Buzz Game!")
    print(f"Starting number is: {start}\n")

    while True:
        correct = fizzbuzz_value(current)
        guess = input(f"Your guess for {current}: ").strip()

        if guess.lower() == "quit":
            print("\nGame Over!")
            print(f"Final Score: {score}/{rounds}")
            break

        rounds += 1


        
        if guess == correct:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong: {correct}\n")



        next_num = current + previous
        previous, current = current, next_num


play_game()