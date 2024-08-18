import random

# 1. Initial Setup

def introduce_game():
    """
    Remind the player of the rules.
    """
    print("Welcome to Blackjack!")
    print("Try to get as close to 21 as possible without going over.")
    print("Face cards (Jack, Queen, King) are worth 10 points.")
    print("Aces are worth 1 or 11 points.")
    print("Good luck!\n")

def prepare_deck():
    """
    Use a standard deck of 52 cards.
    """
    deck = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    for suit in suits:
        for rank in ranks:
            card = {"suit": suit, "rank": rank}
            deck.append(card)

    return deck

# Shuffle the Deck
def shuffle_deck(deck):
    """
    Shuffle the deck to randomize the order of cards.
    """
    random.shuffle(deck)

# 2. Initial Deal
def deal_cards(dealer, player, deck):
    """
    The player and the dealer each receive two cards.
    The player's cards are dealt face up.
    The dealer has one card face up (the "upcard") and one card face down (the "hole card").
    """
    player['hand'] = [deck.pop(), deck.pop()]
    dealer['hand'] = [deck.pop(), deck.pop()]

# 3. Player Actions

def calculate_hand_value(hand):
    """
    Calculate the total value of a hand.
    """
    value = 0
    num_aces = 0

    for card in hand:
        rank = card['rank']
        if rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            value += 11
            num_aces += 1
        else:
            value += int(rank)

    # Adjust for Aces
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value

def check_for_blackjack(dealer, player):
    """
    Immediately check for Blackjack (an Ace and a 10-value card).
    """
    player_value = calculate_hand_value(player['hand'])
    dealer_value = calculate_hand_value(dealer['hand'])

    if player_value == 21 and dealer_value != 21:
        print("Player has Blackjack! Player wins!")
        return True
    elif dealer_value == 21 and player_value != 21:
        print("Dealer has Blackjack! Dealer wins!")
        return True
    elif player_value == 21 and dealer_value == 21:
        print("Both player and dealer have Blackjack! It's a push (tie).")
        return True
    return False

def player_hit(player, deck):
    """
    Request an additional card to try to get as close to 21 as possible without going over.
    """
    player['hand'].append(deck.pop())
    print("Player hits.")
    print_hand(player, reveal_all=True)

def player_stand():
    """
    Keep the current hand and end the turn.
    """
    print("Player stands.")

# Not Implementing split, double down, and surrender for simplicity
def player_actions(player, deck):
    """
    Allow the player to take actions until they stand or bust.
    """
    while True:
        action = input("Do you want to hit or stand? (h/s): ").strip().lower()
        if action == 'h':
            player_hit(player, deck)
            if calculate_hand_value(player['hand']) > 21:
                print("Player busts!")
                break
        elif action == 's':
            player_stand()
            break
        else:
            print("Invalid input, please enter 'h' to hit or 's' to stand.")

# 4. Dealer Actions

def dealer_reveal_hole_card(dealer):
    """
    The dealer reveals the face-down card.
    """
    print("Dealer's hand:")
    print_hand(dealer, reveal_all=True)

def dealer_plays(dealer, deck):
    """
    The dealer plays according to fixed rules:
    - Hits until reaching a hand value of 17 or more.
    """
    dealer_reveal_hole_card(dealer)
    while calculate_hand_value(dealer['hand']) < 17:
        dealer['hand'].append(deck.pop())
        print("Dealer hits.")
        dealer_reveal_hole_card(dealer)

    dealer_value = calculate_hand_value(dealer['hand'])
    if dealer_value > 21:
        print("Dealer busts!")

# 5. Resolution

def determine_winner(dealer, player):
    """
    Compare the player’s hand value to the dealer’s hand value.
    """
    player_value = calculate_hand_value(player['hand'])
    dealer_value = calculate_hand_value(dealer['hand'])

    if player_value > 21:
        print("Dealer wins!")
    elif dealer_value > 21 or player_value > dealer_value:
        print("Player wins!")
    elif dealer_value > player_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# 6. End of Round

def end_round(deck, player, dealer):
    """
    Collect cards and reshuffle if necessary. Decide whether to play another round.
    """
    player['hand'].clear()
    dealer['hand'].clear()

    if len(deck) < 10:
        print("Reshuffling deck.")
        deck = prepare_deck()
        shuffle_deck(deck)

    return deck

def print_hand(entity, reveal_all=False):
    """
    Print the current hand of the player or dealer.
    """
    hand_str = []
    for i, card in enumerate(entity['hand']):
        if i == 0 and not reveal_all and entity == dealer:
            hand_str.append("Hidden Card")
        else:
            hand_str.append(f"{card['rank']} of {card['suit']}")
    print("Hand:", ", ".join(hand_str))
    if reveal_all or entity != dealer:
        print("Hand Value:", calculate_hand_value(entity['hand']))
    print()

def main():
    deck = prepare_deck()
    shuffle_deck(deck)
    player = {"hand": []}
    dealer = {"hand": []}

    introduce_game()

    while True:
        # 2. Initial Deal
        deal_cards(dealer, player, deck)
        print("Player's hand:")
        print_hand(player, reveal_all=True)

        if not check_for_blackjack(dealer, player):
            # 3. Player Actions
            player_actions(player, deck)

            # 4. Dealer Actions
            if calculate_hand_value(player['hand']) <= 21:
                dealer_plays(dealer, deck)

            # 5. Resolution
            determine_winner(dealer, player)

        # 6. End of Round
        deck = end_round(deck, player, dealer)
        play_again = input("Do you want to play another round? (y/n): ").strip().lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
