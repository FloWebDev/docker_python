class GameController:
    def __init__(self, deck: Deck, view, high_card_wins=True):
        # Model
        self.players = []
        self.deck = deck
 
        # View
        self.view = view
 
        # Controller
        self.high_card_wins = high_card_wins
 
    def evaluate_game(self):
        best_rank = None
        best_rank_suit = None
        best_candidate = None
 
        for player in self.players:
            this_rank = RANKS[player.hand.card_by_index(0).rank]
            this_suit = SUITS[player.hand.card_by_index(0).suit]
            if (best_rank is None
                or (self.high_card_wins
                    and ((this_rank > best_rank)
                        or (this_rank == best_rank
                            and this_suit > best_rank_suit)))
                or (not self.high_card_wins
                    and ((this_rank < best_rank)
                        or (this_rank == best_rank
                            and this_suit < best_rank_suit)))
            ):
                best_candidate = player.name
                best_rank = this_rank
                best_rank_suit = this_suit
 
        return best_candidate