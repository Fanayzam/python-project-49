#!/usr/bin/env python3


from brain_games.games.utils import play_game, welcome


def main():
    user_name = welcome()
    print("What is the result of the expression?")
    play_game(user_name)

if __name__ == "__main__":
    main()
