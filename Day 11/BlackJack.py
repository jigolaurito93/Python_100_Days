import random
import art

def play_blackjack():

    print(art.logo)
    # Function to deal cards
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, dealer_score):
        if user_score == dealer_score:
            return "It's a draw"
        elif dealer_score == 0:
            return "You lost!"
        elif user_score == 0:
            return "You win!"
        elif user_score > 21:
            return "You went over. You lose!"
        elif dealer_score > 21:
            return "Opponent went over. You win!"
        elif user_score > dealer_score:
            return "You win!"
        else:
            return "You lose!"

    user_cards = []
    dealer_cards = []
    dealer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to HIT, type 'n' to STAY: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))


    while input(f"Do you want to continue playing? 'y' or 'n'? ") == 'y':
        print("\n" * 20)
        play_blackjack()
    quit()

play_blackjack()
