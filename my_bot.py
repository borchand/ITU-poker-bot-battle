from poker_game_runner.state import Observation
from poker_game_runner.utils import Range, HandType


class Bot:
    def get_name(self):
        return "Nissemand"

    def act(self, obs: Observation):
        current_board_hand = obs.get_board_hand_type()
        can_raise = obs.can_raise()
        my_hand = obs.get_my_hand_type()
        board = obs.get_board_hand_type()

        decent_hand = Range(
            "22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 84s+, 73s+, 64s+, 53s+, A2o+, K2o+, Q4o+, J6o+, T7o+, 97o+, 87o"
        )

        if obs.current_round == 0:
            if (decent_hand.is_hand_in_range(obs.my_hand)):
                if can_raise:
                    return obs.get_min_raise()
                else:
                    return 1

        if obs.current_round == 1 or obs.current_round == 2:
            if current_board_hand >= 2:
                if can_raise and my_hand > board:
                    return obs.get_min_raise()
                else:
                    return 1

            if current_board_hand >= 9 and my_hand > board:
                return obs.get_max_raise()
            else:
                return 1

        if obs.current_round == 3:
            if current_board_hand >= 3:
                if can_raise and my_hand > board:
                    return obs.get_min_raise()
                else:
                    return 1

            if current_board_hand >= 5 and my_hand > board:
                return obs.get_min_raise() * 2
            else:
                return 1
            if current_board_hand >= 8:
                return obs.get_max_raise()

        if obs.current_round == 4:
            if current_board_hand >= 4:
                return obs.get_min_raise()
            if current_board_hand >= 7:
                return obs.get_max_raise()

        return 0
        # Returning 0 will fold or check
        # return 1 - Returning 1 will call or check
        # return x > 1 - Returning a number greater than 1 will raise
