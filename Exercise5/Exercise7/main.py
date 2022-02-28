# File: main.py
# Author: Steve Hommy
# Description: Deck of cards and card games.

import card
import deck


def main():

    print("Let's test that a single card works...")

    my_card = card.Card("Hearts", 12)
    my_card.show_card()
    print(my_card)

    print("Single card testing is over.\n")

    print("Let's test that a deck of card is created...")

    my_deck = deck.Deck()
    my_deck.show_deck()

    print("Card deck testing is over.\n")

    print("Let's shuffle the deck.")
    my_deck.shuffle_deck()

    print("Let's test that a deck of card is shuffled...")

    my_deck.show_deck()

    print("Cards should be suffled now.\n")

    print("Let's draw 2 cards and show them.")
    print("You draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
    print("Your opponent draw:")
    card1 = my_deck.draw_card()
    card1.show_card()

    # Code your Exercise 5 taks 7 game here.
    print("\nDraw 3 cards and highest value wins")

    while True:
        print("Here are the cards that have been draw ")
        draw1 = my_deck.draw_card()
        draw2 = my_deck.draw_card()
        draw3 = my_deck.draw_card()
        draw1.show_card(), draw2.show_card(), draw3.show_card()
        if draw1.value == draw2.value == draw3.value:
            print("We have to re-draw because there is a tie")
        elif draw1.value > draw2.value and draw3.value:
            print("Winner is"), draw1.show_card()
            break
        elif draw2.value > draw1.value and draw3.value:
            print("Winner is"), draw2.show_card()
            break
        else:
            print("Winner is"), draw3.show_card()
        break


# Calling the main function here, do not change...
main()
