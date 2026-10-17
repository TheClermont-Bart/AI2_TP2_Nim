from __future__ import annotations

from math import gamma
import random
from typing import Literal

from nim import Action, Board, Probability, QValue, available_actions

type Algorithm = Literal["greedy", "epsilon-greedy"]


class QLearning:
    def __init__(
        self,
        epsilon: Probability = 0.1,
        alpha: Probability = 0.5,
        gamma: Probability = 0.7,
    ):
        r"""Initialise l'IA.

        Une IA nouvellement initialisée possède
        un dictionnaire d'apprentissage Q vide,
        un taux d'apprentissage (alpha)
        et un taux d'exploration (epsilon).

        Args:
            epsilon:
                Le taux d'exploration.

                TODO: epsilon (5 points)
                    Identifier une valeur par défaut
                    et documenter le paramètre epsilon de manière à expliquer
                    le sens du paramètre et le choix de sa valeur.

                Epsilon = chance de jouer un coup au hasard pour decouvrir

            alpha:
                Le facteur d'apprentissage.

                TODO: alpha (5 points)
                    Identifier une valeur par défaut
                    et documenter le paramètre alpha de manière à expliquer
                    le sens du paramètre et le choix de sa valeur.

                Alpha = Apprentisage du passer.
                Chiffre entre 0(On apprend rien) et 1(On oublie le passer).

            gamma:
                Le facteur d'actualisation.

                Dans le Q-learning, γ (:math:`\gamma`) multiplie l'estimation
                de la valeur future optimale.
                L'importance accordée à la récompense suivante est définie
                par le paramètre gamma.

                Gamma est un nombre réel compris entre 0 et 1
                (:math:`0 \leq \gamma \leq 1`).
                Si l'on fixe gamma à zéro, l'agent ignore totalement les
                récompenses futures ;
                de tels agents ne prennent en compte que les récompenses
                immédiates.
                En revanche, si l'on fixe gamma à 1,
                l'algorithme recherche des récompenses élevées à long terme.

                TODO: gamma (2 points)
                    Identifier une valeur par défaut


        Le dictionnaire d'apprentissage Q associe les paires (état, action) à
        une valeur-Q.

        """
        self.q: dict[tuple[Board, Action], QValue] = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def update(
        self, old_state: Board, action: Action, new_state: Board, reward: QValue
    ) -> None:
        """Met à jour le modèle Q-learning.

        Args:
            old_state:
                L'état avant l'action.
            action:
                L'action entreprise.
            new_state:
                L'état résultant de l'action.
            reward:
                La récompense obtenue.

        """
        old = self.get_q_value(old_state, action)
        best_future = self.best_future_reward(new_state)
        self.update_q_value(old_state, action, old, reward, best_future)

    def get_q_value(self, state: Board, action: Action) -> QValue:
        """Retourne la valeur-Q pour un état et une action donnés.

        Si aucune valeur-Q n'existe encore dans `self.q`, retourne 0.
        """
        # TODO: get_q_value (10 points)
        #   Tester et implémenter get_q_value

        if self.q.get((state, action)):
            return self.q[(state, action)]
        else:
            return 0

    def update_q_value(
        self,
        state: Board,
        action: Action,
        old_q: QValue,
        reward: QValue,
        future_rewards: QValue,
    ) -> None:
        """Met à jour le Q-value.

        Args:
            state:
                L'état actuellement mis à jour.
            action:
                L'action qui met à jour l'état.
            old_q:
                L'ancienne valeur-Q pour cette paire état-action.
            reward:
                La récompense actuelle.
            future_rewards:
                L'estimation des récompenses futures.

        Utilise la formule:

        .. math::

            Q(S, A) <- Q_{old} + \alpha * (Q_{new} - Q_{old})

        telle que :math:`Q_{old}` est l'ancienne Q-Value, :math:`\alpha` est le
        taux d'apprentissage, et :math:`Q_{new}` est la somme de la récompense
        actuelle et l'estimation des récompenses futures pondérée par le
        facteur d'actualisation.

        """
        # TODO: update_q_value (10 points)
        #   Tester et implémenter update_q_value

        q_new = reward + future_rewards * self.gamma
        #Somme de la récompense actuelle + l'estimation des récompenses futures * par le facteur d'actualisation.

        q = old_q + self.alpha * (q_new - old_q)
        #Q_{old} + alpha * (Q_{new} - Q_{old})

        self.q[(state, action)] = q


    def best_future_reward(self, state: Board) -> QValue:
        """Estime la meilleure récompense future étant donné un état `state`.

        Considère toutes les paires `(état, action)` possibles disponibles
        dans cet état et retourne le maximum de toutes leurs valeurs-Q.
        Utilise 0 comme valeur-Q si une paire n'a pas de valeur-Q dans
        `self.q`.
        S'il n'y a aucune action disponible dans l'état, retourne 0.

        """
        # TODO: best_future_reward (10 points)
        #   Tester et implémenter best_future_reward

        actions = list(available_actions(state)) #List des coups possibles

        if len(actions) == 0:
            return 0

        best_action = self.get_q_value(state, actions[0])
        # [0] car doit en choisir un avant de comparer au autre

        for action in actions: #Pour chaque action, verifier la valeur de Q
            result = self.get_q_value(state, action)
            if result > best_action:
                best_action = result

        return best_action

    def choose_action(self, state: Board, train: bool = True) -> Action:
        """Étant donné un état, retourne une action à entreprendre.

        Si `train` est `False`, retourne la meilleure action disponible dans cet
        état (celle ayant la plus haute valeur-Q, en utilisant 0 pour les paires
        sans valeur-Q).

        Si `train` est `True`, choisit une action disponible aléatoire avec la
        probabilité `self.epsilon`, sinon choisit la meilleure action
        disponible.

        Si plusieurs actions ont la même valeur-Q, n'importe laquelle d'entre
        elles est une valeur de retour acceptable.

        """
        # TODO: choose_action (10 points)
        #   Tester et implémenter choose_action

        actions = list(available_actions(state)) # List des coups possibles

        best_action = actions[0]
        best_q = self.get_q_value(state, best_action)

        for action in actions:
            result = self.get_q_value(state, action)
            if result > best_q:
                best_action = action
                best_q = result

        random_value = random.random()

        if train and random_value < self.epsilon:
            random_action = random.choice(actions)
            return random_action

        return best_action




