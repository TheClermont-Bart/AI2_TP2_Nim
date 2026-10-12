from nim import available_actions
from nim import transition
from nim.ai import QLearning


def test_empty_board_falsy():
    empty_board = ()

    assert not available_actions(empty_board)


def test_empty_board_empty():
    empty_board = ()
    assert len(available_actions(empty_board)) == 0


def test_documented_example():
    assert {(0, 1), (1, 1), (0, 2)} == set(available_actions((2, 1, 0, 0)))


# TODO: test_available_actions (10 points)
#   Ajouter des tests pour les cas-limites de available_actions
def test_one_stack_one_object():
    # Une pile et un objet.
    assert {(0, 1)} == set(available_actions((1,)))


def test_two_stack_one_object():
    # Deux piles avec un objet
    assert {(0, 1), (1, 1)} == set(available_actions((1, 1)))


def test_transition():
    assert (0, 1, 0) == transition((2,1,0),(0,2))
    assert (2, 0, 0) == transition((2,1,0),(1,1))

def test_qvalue_empty():
    ai = QLearning() #self = QLearning class et aucun Q

    assert ai.get_q_value((2,1),(0,1)) == 0

def test_qvalue_one():
    ai = QLearning()
    ai.q[(2,1), (0,1)] = 1

    assert ai.get_q_value((2,1),(0,1)) == 1

def test_best_reward():
    ai = QLearning()

    assert ai.best_future_reward((1,1)) == 0
    assert ai.best_future_reward((1,1)) == 0
