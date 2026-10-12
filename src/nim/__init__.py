"""
Espace de nom principal de `nim`.
"""

from __future__ import annotations

import random
from collections.abc import Collection, Iterable
from typing import Literal, cast

type Board = tuple[int, ...]
r"""
Le plateau de jeu.

Un plateau de jeu de Nim a plusieurs tas d'objets. 

Nous représentons ce plateau par 
un :math:`n`-uplet d'entiers :math:`k`
tels qu'il y a :math:`n` tas de :math:`k` objets, 
:math:`n, k \in \mathbb{N}`.

Exemples:
    >>> ( board_with_3_tas_of_123 := (1, 2, 3) )
    (1, 2, 3)
    >>> ( empty_board := () )
    ()
    >>> ( losing_board_of_2_tas := (0, 0) )
    (0, 0)
    >>> ( winning_board_of_4_tas := (0, 1, 0, 0) )
    (0, 1, 0, 0)
"""

type Action = tuple[int, int]
r"""
Une action posée sur un plateau de jeu.

Une action est la paire :math:`i, j`
telle que de la tas numéro :math:`i` on retire :math:`j` objets
:math:`i, j in \mathbb{N}`.

Exemples:
    >>> ( prendre_7_objets_de_la_première_tas := (0, 7) )
    (0, 7)
    >>> ( ne_rien_prendre_de_la_2e_tas := (1, 0) )
    (1, 0)
  
"""

type Player = Literal[0, 1]
"""
Le joueur zéro commence, le numéro 1 joue deuxième.

On distingue un joueur de l'autre par leur numéro. 
Le premier à jouer porte le numéroi ``0`` et l'autre porte le numéro ``1``.
Aux échecs, les blancs sont ``0`` et les noirs sont ``1``.

Exemples:
    >>> ( le_joueur_qui_commence_la_partie := 0)
    0
    >>> ( l_autre_joueur := 1)
    1
"""


type Probability = float
"""
Un nombre entre 0 et 1 qui quantifie les chances qu'un événement se produise.

Exemples:
    >>> ( une_certitude := 1.0 )
    1.0
    >>> ( c_est_impossible := 0.0 )
    0.0
    >>> ( piger_un_trefle := 13/52 )
    0.25
"""


type QValue = float | int
# TODO: QValue (5 points)
#   Documenter le type nim.QValue
"""
Le QValue est un nombre qui estime la recompense d'un ensemble etat (s) et action (a). 
Une valeur proche de 1 indique un coup qui mène vers une victoire.
Une valeur proche de -1 un coup qui mène vers une défaite.
Une valeur de 0 on ne sait pas encore.
"""


def new_random_board(num_heaps: int | None = None) -> Board:
    """Initialise un nouveau plateau aléatoire.

    Args:
        num_heaps:
            Détermine un nombre de tas. S'il n'est pas défini,
            un nombre aléatoire est déterminé par défaut.
    """
    if num_heaps and num_heaps < 0:
        raise ValueError("Seules des valeurs positives sont acceptées")

    num_heaps = num_heaps or random.randint(1, 10)

    board_data = tuple(random.randint(1, 10) for _ in range(num_heaps))
    return board_data


def transition(board: Board, action: Action) -> Board:
    """Effectue l'action sur le plateau pour le joueur actuel.

    Args:
        board:
            Un état d'un plateau de Nim d'origine.
        action:
            L'action à effectuer, laquelle doit être un tuple ``(i, j)``
            où *i* est le numéro du barrilet et *j* le nombre de charges
            à retirer.

    Raises:
        IndexError:
            Une action qui contient un :math:`i` qui ne corresponde à
            aucune tas lève une erreur.
        ValueError:
            Une action qui contient un :math:`j` trop grand ou trop
            petit pour la quantité d'objets dans la tas math:`i` lève
            une erreur.

    Return:
        L'état du plateau de Nim résultant de l'application de l'action
        sur l'état d'origine.
    """
    # TODO: transition (10 points)
    #   Tester et implémenter nim.transition
    pile = list(board)
    i,j = action

    if  i < 0 or i >= len(pile):
        raise IndexError("`i` qui ne corresponde à aucun tas lève une erreur.")

    if j < 0 or j > pile[i]:
        raise ValueError("`j` trop grand ou trop petit pour la quantité d'objets dans la tas math:`i` lève une erreur.")

    pile[i] -= j
    return tuple(pile)


def available_actions(board_data: Board) -> Collection[Action]:
    # TODO: available_actions (10 points)
    #    Documenter et implémenter nim.available_actions
    """
    Prends les donnees du board sous forme (2,1,0)
    et retourne une liste d'actions valides.

    Args:
        board_data: Le plateau recu representer par le nombre d'objet a l'index de chaque pile
        Example ; (2,1,0) 2 objets sur la pile 0, 1 objets sur la pile 1, etc.

    Returns:
        Retourne une liste des actions possibles.
        Example ; args (2,1,0) retourne (0,1),(0,2),(1,1) qui represente (numero de pile, nombre retirer)
    """
    action_list = [] #Liste des actions possibles

    for pile, obj in enumerate(board_data):
        for i in range(1, obj+1):
            action_list.append((pile, i))

    return action_list


class Nim:
    """Implémente les règles du jeu de Nim."""

    def __init__(self, board: Board | None = None):
        """Initialise un plateau de jeu..

        Args:
            board:
                Un plateau de jeu. S'il n'est pas fourni,
                un plateau aléatoire est généré.

        Attributes:
            player:
                Le joueur à qui le tour.

        """

        self.board = board or new_random_board()
        self.player: Player = 0

    @property
    def available_actions(self) -> Iterable[Action]:
        return available_actions(self.board)

    def _other_player(self, player: Player) -> Player:
        return cast(Player, 1 - player)

    def switch_player(self) -> Player:
        """Change et retourne le joueur à qui c'est le tour."""
        self.player = self._other_player(self.player)
        return self.player

    def move(self, action: Action) -> None:
        """Effectue l'action sur le plateau pour le joueur actuel.

        Args:
            action:
                L'action à effectuer, laquelle doit être un tuple ``(i, j)``
                où *i* est le numéro du barrilet et *j* le nombre de charges
                à retirer.

        """
        if self.winner is not None:
            raise NimError("Game already won")

        try:
            self.board = transition(self.board, action)
        except (IndexError, ValueError) as e:
            raise NimError() from e

        self.switch_player()

    @property
    def winner(self) -> Player | None:
        """Le gagnant de la partie, s'il-y-a lieu."""
        if all(tas == 0 for tas in self.board):
            return self.player
        return None

    @property
    def loser(self) -> Player | None:
        """Le gagnant de la partie, s'il-y-a lieu."""
        if self.winner is not None:
            return self._other_player(self.winner)
        return None


class NimError(RuntimeError):
    """Une erreur de jeu de Nim."""
