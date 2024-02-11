import random

def main():
    card_types = ["2", "3", "4", "5", "6", \
                  "7", "8", "9", "10", "J", \
                  "Q", "K", "Ace"]
    suits = ["Diamonds", "Spades", "Clubs", \
             "Hearts"]
    deck = {}
    for type in card_types:
        for suit in suits:
            if type.isnumeric():
                deck[type + " of " + suit] = type
            elif type == "Ace":
                deck[type + " of " + suit] = "11"
            else:
                deck[type + " of " + suit] = "10"
    
    while len(deck) != 0:
        deck = play_round(deck)
        print()
        print(f"В колоде осталось {len(deck)} карт")
    
def play_round(deck):
    hand_1 = 0
    hand_2 = 0
    while hand_1 <= 21 and hand_2 <= 21 and len(deck) != 0:
        w_1, deck = deal_card(deck, hand_1, "1")
        hand_1 += w_1
        print(f"На руке у 1 игрока {hand_1} очков.")
        print()
        if len(deck) != 0:
            w_2, deck = deal_card(deck, hand_2, "2")
            hand_2 += w_2
            print(f"На руке у 2 игрока {hand_2} очков.")
            print()

    if hand_1 > 21 and hand_2 > 21:
        print("У обоих больше 21, победителя нет!")
    if hand_1 > 21 and hand_2 <= 21:
        print("1 набрал больше 21 и проиграл!")
    if hand_2 > 21 and hand_1 <= 21:
        print("2 набрал больше 21 и проиграл!")
    return deck
                
def deal_card(deck, hand, n):
    card = random.choice(list(deck))
    weight = deck.pop(card)
    if ("Ace" in card) and (hand + int(weight) > 21):
        weight = "1"
    print(f"Игроку {n} сдана карта {card}, стоимостью {weight} очков!")
    return int(weight), deck

      
if __name__ == "__main__":
    main()           