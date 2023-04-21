from poker_game_runner.state import Observation
from poker_game_runner.utils import Range, HandType
"""
  This bot compares it's hand to the top 50% of poker hands (generated from https://www.pokerhandrange.com/).
  If hand is "good", the bot will call or check every round, until the game is over.
  If hand is "bad", it will fold immediately 
"""


class Bot:
    def get_name(self):
        return "range_bot"

    def act(self, obs: Observation):
        good_cards = Range(
            "22+, A2s+, K2s+, Q2s+, J2s+, T5s+, 96s+, 86s+, 75s+, A2o+, K5o+, Q7o+, J8o+, T8o+"
        )
        if (good_cards.is_hand_in_range(obs.my_hand)):
            return 1
        return 0
