from art import logo, vs
from game_data import data
import random


def format_data(account):
    """"this function formats the data for accounts into a printable state"""
    account_name = account["name"]
    account_desription = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desription} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """"Check if user is correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    guess = input("Who has more followers? 'A' or 'B' ?").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"You are right! The current score is {score}")
    else:
        print(f"Sorry, you are wrong...Your score is {score}")
        game_should_continue = False
