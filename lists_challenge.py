import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user = input("Press enter to pick a card, or Press Q then enter to quit ")
    if user == "Q":
        break
    elif user == "":
        cards = random.choice(diamonds)
        diamonds.remove(cards)
        hand.append(cards)
        print (f"Your hand: {hand}")
        print (f"These are the remainder of cards {diamonds}")
        

if not diamonds:
    print("There are no more cards to pick.")