import random
import pandas as pd

# Define card interactions based on the game rules
# Format: {Card1: {Card2: (strong/normal, points)}}
interactions = {
    "Fire": {"Water": (2, -2), "Earth": (1, -1)},
    "Water": {"Ether": (2, -2), "Fire": (1, -1)},
    "Earth": {"Air": (2, -2), "Ether": (1, -1)},
    "Air": {"Fire": (2, -2), "Water": (1, -1)},
    "Ether": {"Earth": (2, -2), "Air": (1, -1)},
}

cards = list(interactions.keys())  # Available card types

def play_round(player1_card, player2_card):
    # Determine points lost by each player in this round
    if player2_card in interactions[player1_card]:
        advantage, points = interactions[player1_card][player2_card]
        player2_loss = points
    else:
        player2_loss = 0

    if player1_card in interactions[player2_card]:
        advantage, points = interactions[player2_card][player1_card]
        player1_loss = points
    else:
        player1_loss = 0

    return player1_loss, player2_loss

def simulate_game(rounds, simulations): 
    results = {"Player 1 Wins": 0, "Player 2 Wins": 0, "Ties": 0}
    for _ in range(simulations):
        # Reset each player's points
        player1_points, player2_points = 0, 0

        # Each player receives a random set of 20 cards
        player1_cards = random.choices(cards, k=rounds)
        player2_cards = random.choices(cards, k=rounds)

        for _ in range(rounds):
            # Each player randomly selects a card from their hand
            player1_card = random.choice(player1_cards)
            player2_card = random.choice(player2_cards)
            
            # Calculate points lost in this round
            player1_loss, player2_loss = play_round(player1_card, player2_card)
            player1_points += abs(player1_loss)
            player2_points += abs(player2_loss)
            
            # Remove the played cards from each player's hand
            player1_cards.remove(player1_card)
            player2_cards.remove(player2_card)

        # Determine the result of this simulation
        if player1_points < player2_points:
            results["Player 1 Wins"] += 1
        elif player2_points < player1_points:
            results["Player 2 Wins"] += 1
        else:
            results["Ties"] += 1

    return pd.DataFrame([results])
print(simulate_game(100, 100000))
