#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created April 2022
# This program gets a users age and tells them if they
# are of suitable age to date someone's grandchild


def main():
    # this function calculates if age is suitable

    # input
    user_age_string = input("Enter your age: ")

    # process & output
    try:
        user_age = int(user_age_string)

        if user_age >= 25 and user_age <= 40:
            print("You may date my Grandchild.")
        else:
            print("You may NOT date my Grandchild.")

    except Exception:
        print("That is not a valid age!")
    print("\nDone.")


if __name__ == "__main__":
    main()
