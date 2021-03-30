# -*- coding: utf-8 -*-
# @Time    : 27/03/2021 14:52
# @Author  : Oliver Buček
# @Email   : info@robotics-slovenia.com
# @File    : pool1.py
# @Software: PyCharm
import random

import pyfiglet


class Game:
    def pool_game(self):
        user_lives = 6
        computer_lives = 6
        balls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        pockets = [1, 2, 3, 4, 5, 6]
        computer_random_balls = random.choice(balls)
        computer_random_pockets = random.choice(pockets)
        print("*" * 53)
        print("Welcome to Pool Game. You will play against computer!")
        print("*" * 53)
        while user_lives != 0 or computer_lives != 0:
            if user_lives == 0 or computer_lives == 0:
                ascii_banner = pyfiglet.figlet_format("Game over!")
                print(ascii_banner)
                if user_lives > computer_lives:
                    ascii_banner1 = pyfiglet.figlet_format("You Winn!")
                    print(ascii_banner1)
                    question = input("Are you ready to play the game? Yes/No\n")
                    if question.lower().startswith("y"):
                        obj.pool_game()
                    else:
                        if question.lower().startswith("n"):
                            print("Goodbye and thank you!!!\n")
                            print("*" * 30)
                            print("Visit www.robotic-slovenia.com")
                            print("*" * 30)
                            exit()
                else:
                    print("Im sorry. The winner is a computer.")
                    ascii_banner2 = pyfiglet.figlet_format("You loose!")
                    print(ascii_banner2)
                    question = input("Are you ready to play the game? Yes/No\n")
                    if question.lower().startswith("y"):
                        obj.pool_game()
                    else:
                        if question.lower().startswith("n"):
                            print("Goodbye and thank you!!!\n")
                            print("*" * 30)
                            print("Visit www.robotic-slovenia.com")
                            print("*" * 30)
                            exit()
                break
            else:
                user_choice = int(input(f"Choose a ball {balls}:\n"))
                choose_pocket = int(input(f"Choose a pocket 1 - 6:\n"))
                if user_choice > 15:
                    print("You choose ball that does not exist")

                elif choose_pocket > 6:
                    print("You choose pocket that does not exist")

                elif choose_pocket == random.choice(
                        pockets) and user_choice in balls and user_choice != computer_random_balls:

                    print(f"You select ball number {user_choice}")
                    print(f"You choose pocket number {choose_pocket}")
                    print(f"Computer select ball number {computer_random_balls}")
                    print(f"Computer choose pocket number {computer_random_pockets}")

                    print("*" * 53)
                    print(f"You put a ball {user_choice} in a pocket {choose_pocket}!")
                    print("*" * 53)

                    computer_lives -= 1
                    print(f"{computer_lives} Computer lives left")
                    print(f"{user_lives} User lives left\n")
                    balls.remove(user_choice)


                elif computer_random_pockets == computer_random_pockets and computer_random_balls != user_choice and computer_random_balls in balls:
                    print(f"You select ball number {user_choice}")
                    print(f"You choose pocket number {choose_pocket}")
                    print(f"Computer select ball number {computer_random_balls}")
                    print(f"Computer choose pocket number {computer_random_pockets}")

                    balls.remove(computer_random_balls)

                    print("*" * 53)
                    print(f"Computer put a ball {computer_random_balls} in a pocket {computer_random_pockets}!")
                    print("*" * 53)

                    user_lives = user_lives - 1
                    print(f"{user_lives} User lives left")
                    print(f"{computer_lives} Computer lives left\n")


                elif user_choice == 8 and 8 in balls and choose_pocket == random.choice(pockets):
                    print(f"You select ball number {user_choice}")
                    print(f"You choose pocket number {choose_pocket}")
                    print(f"Computer select ball number {computer_random_balls}")
                    print(f"Computer choose pocket number {computer_random_pockets}")

                    balls.remove(8)

                    print(f"You put a ball {user_choice} in a pocket!\n")
                    print("*" * 53)
                    print("You got an extra live!")
                    print("*" * 53)
                    user_lives = user_lives + 1
                    print(f"{user_lives} User lives left")
                    print(f"{computer_lives} Computer lives left\n")



                elif computer_random_balls == 8 and 8 in balls and computer_random_pockets == computer_random_pockets:
                    print(f"You select ball number {user_choice}")
                    print(f"You choose pocket number {choose_pocket}")
                    print(f"Computer select ball number {computer_random_balls}")
                    print(f"Computer choose pocket number {computer_random_pockets}")

                    balls.remove(8)

                    print("*" * 53)
                    print(f"Computer put a ball {computer_random_balls} in a pocket {computer_random_pockets}\n")
                    print("*" * 53)

                    computer_lives = computer_lives + 1
                    print("*" * 53)
                    print("Computer got an extra live!")
                    print("*" * 53)
                    print(f"{user_lives} User lives left")
                    print(f"{computer_lives} Computer lives left\n")



                elif user_choice not in balls and computer_random_balls not in balls:
                    print(f"You cant take that ball. Is already in a pocket!\n")
                    pass
                    if balls == []:
                        print(f"There is no ball that you can use! All balls are in pockets!\n")
                        question = input("Are you ready to play the game? Yes/No\n")
                        if question.lower().startswith("y"):
                            obj.pool_game()
                        else:
                            if question.lower().startswith("n"):
                                print("Goodbye")
                                exit()
                else:
                    print(f"You select ball number {user_choice}")
                    print(f"You choose pocket number {choose_pocket}")
                    print(f"Computer select ball number {computer_random_balls}")
                    print(f"Computer choose pocket number {computer_random_pockets}\n")

                    print(f"Nobody put ball in a pocket!\n")
                    user_lives = user_lives - 1
                    print(f"{user_lives} User lives left")
                    computer_lives = computer_lives - 1
                    print(f"{computer_lives} Computer lives left\n")

                    if user_lives == 0 and computer_lives == 0:
                        ascii_banner = pyfiglet.figlet_format("Game over!")
                        print(ascii_banner)
                        question = input("Are you ready to play the game? Yes/No\n")
                        if question.lower().startswith("y"):
                            obj.pool_game()
                        else:
                            if question.lower().startswith("n"):
                                print("Goodbye and thank you!!!\n")
                                print("*" * 30)
                                print("Visit www.robotic-slovenia.com")
                                print("*" * 30)
                                exit()


question = input("Are you ready to play the game? Yes/No\n")
obj = Game()
if question.lower().startswith("y"):
    obj.pool_game()
else:
    if question.lower().startswith("n"):
        print("Goodbye and thank you!!!\n")
        print("*" * 30)
        print("Visit www.robotic-slovenia.com")
        print("*" * 30)
        exit()
