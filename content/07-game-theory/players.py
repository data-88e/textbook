import functools
import numpy as np
from datascience import *

most_common = lambda a: a[np.argmax([np.count_nonzero(np.equal(i, a)) for i in a])]

def payoff(p1, p2):
    p1_defect = p1.play(p2)
    p2_defect = p2.play(p1)
    
    p1.update_history()
    p2.update_history()
    
    if p1_defect and p2_defect:
        return 4, 4
    elif p1_defect and not p2_defect:
        return 0, 5
    elif not p1_defect and p2_defect:
        return 5, 0
    else:
        return 2, 2

def run_match(p1, p2, n=5, winner=True):
    p1.reset_history()
    p2.reset_history()
    
    p1_years = []
    p2_years = []
    
    for i in range(n):
        p1_score, p2_score = payoff(p1, p2)
        p1_years.append(p1_score)
        p2_years.append(p2_score)
        
    if winner:
        p1_mean = np.mean(p1_years)
        p2_mean = np.mean(p2_years)

        if p1_mean < p2_mean:
            return p1
        else:
            return p2
    else:
        return p1_years, p2_years

def determine_winner(p1, p1_mean, p2, p2_mean):
    if p1_mean < p2_mean:
        return p1
    else:
        return p2

def flatten_results(tbl):
    t = Table()
    t = t.with_column("player", np.append(tbl.column("p1"), tbl.column("p2")))
    t = t.with_column("score", np.append(tbl.column("p1_mean"), tbl.column("p2_mean")))
    df = t.to_df()
    df["player"] = df["player"].apply(repr)
    return df

def create_player_class(player_name, play_method):
    @functools.total_ordering
    class Player:
        def __init__(self, p=0.5):
            self.history = make_array(True)[:0]
            assert len(self.history) == 0
            self.prob = p
            self.name = player_name
            self.last_move = None
        
        def play(self, opponent):
            """Returns True if player defects, False otherwise"""
            defect = play_method(self, opponent)
            self.last_move = defect
            return defect
        
        def reset_history(self):
            self.history = make_array()
        
        def update_history(self):
            assert self.last_move is not None
            self.history = np.append(self.history, self.last_move)
            self.last_move = None
        
        def __repr__(self):
            if player_name == "Random":
                return player_name + "({})".format(self.prob)
            return player_name
        
        def __hash__(self):
            return hash(self.name)
        
        def __eq__(self, other):
            return self.name == other.name
        
        def __lt__(self, other):
            return self.name < other.name
    
    return Player

def defector_play(self, opponent):
    return True

Defector = create_player_class("Defector", defector_play)

def cooperator_play(self, opponent):
    return False

Cooperator = create_player_class("Cooperator", cooperator_play)

def random_play(self, opponent):
    return np.random.random() < self.prob

Random = create_player_class("Random", random_play)

def alternator_play(self, opponent):
    if len(self.history) > 0:
        return not self.history.item(-1)
    else:
        return False

Alternator = create_player_class("Alternator", alternator_play)

def tit_for_tat_play(self, opponent):
    if len(opponent.history) > 0 and opponent.history.item(-1):
        return True
    else:
        return False

TitForTat = create_player_class("TitForTat", tit_for_tat_play)

def backstabber_play(self, opponent):
    return np.sum(opponent.history) > 3

Backstabber = create_player_class("Backstabber", backstabber_play)

def bully_play(self, opponent):
    if len(self.history) == 0:
        return True
    return not opponent.history.item(-1)

Bully = create_player_class("Bully", bully_play)

def desperate_play(self, opponent):
    return np.sum(np.logical_and(self.history, opponent.history)) < 1

Desperate = create_player_class("Desperate", desperate_play)

def fool_me_once_play(self, opponent):
    return np.sum(opponent.history) > 1

FoolMeOnce = create_player_class("FoolMeOnce", fool_me_once_play)

def forgiver_play(self, opponent):
    if len(self.history) == 0:
        return False
    return np.sum(opponent.history) / len(opponent.history) > 0.1

Forgiver = create_player_class("Forgiver", forgiver_play)

def once_bitten_play(self, opponent):
    if not hasattr(self, "defects_left"):
        self.defects_left = 0
    if self.defects_left > 0:
        self.defects_left -= 1
        return True
    if len(opponent.history) >= 2:
        if opponent.history[-1] and opponent.history[-2]:
            self.defects_left = 9
            return True
    return False

OnceBitten = create_player_class("OnceBitten", once_bitten_play)

def grudger_play(self, opponent):
    return np.sum(opponent.history) > 0

Grudger = create_player_class("Grudger", grudger_play)
