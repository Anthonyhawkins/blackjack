# blackjack

## Requirements
- **Python**: 3.9+

## Rules of Blackjack
1. Initial Setup
    - Introduce the Game: Remind the player of the rules.
    - Deck Preparation: Use a standard deck of 52 cards.
    - Shuffle the Deck: Shuffle the deck to randomize the order of cards.
2. Initial Deal
    - Deal Cards:
      - The player and the dealer each receive two cards.
      - The player's cards are dealt face up.
      - The dealer has one card face up (the "upcard") and one card face down (the "hole card").
3. Player Actions
    - Blackjack Check: Immediately check for Blackjack (an Ace and a 10-value card).
      - If the player has Blackjack and the dealer does not, the player wins instantly.
      - If both have Blackjack, it's a push (tie).
      - If the dealer has Blackjack and the player does not, the dealer wins.
    - Player Decisions: The player takes their turn with the following options:
      - Hit: Request an additional card to try to get as close to 21 as possible without going over.
      - Stand: Keep the current hand and end the turn.
      - Double Down: Receive one more card and then stand.
      - Split: If the player's first two cards have the same value, they can split them into two separate hands and play each hand separately.
      - Surrender: Forfeit the hand and end the turn (optional and depends on house rules).
4. Dealer Actions
    - Reveal Hole Card: The dealer reveals the face-down card.
    - Dealer Plays: The dealer plays according to fixed rules:
      - Hits until reaching a hand value of 17 or more.
5. Resolution
    - Determine Winner: Compare the player’s hand value to the dealer’s hand value.
    - Bust: Any hand exceeding 21 automatically loses.
    - Player Wins: The player's hand value is higher than the dealer’s without busting.
    - Dealer Wins: The dealer’s hand value is higher than the player's without busting.
    - Push: Both hands have equal value, resulting in a tie.
6. End of Round
    - Collect Cards: Collect all cards and reshuffle if necessary.
    - Continue: Decide whether to play another round.

## Usage
`python blackjack.py`