#######################
 Travail pratique: Nim
#######################

> Ce fichier s'affichera mieux dans PyCharm que dans un navigateur

Ce dépôt est géré sur GitLab à l'adresse
https://gitlab.com/cblegareprof/420-611-BT-nim
.
Un miroir est gardé à jour automatiquement sur GitHub à l'adresse
https://github.com/cblegare/420-611-BT-nim
.


Bien commencer
==============

Dans le jeu de Nim, deux joueurs s'affrontent pour vider tour-à-tour des
tas d'objets. 
À chaque tour, un joueur retire un nombre quelconque d'objets d'un tas. 
Le joueur qui prend le dernier objet des tas a perdu.

Nous utiliserons le *Q-Learning* pour entraîner un agent à jouer au Nim.
Rappelez-vous que dans le Q-learning, nous essayons d'apprendre une valeur 
de récompense (un nombre) pour chaque paire `(état, action)`. 
Une action qui fait perdre la partie aura une récompense de -1, 
une action qui gagne la partie aura une récompense de 1, 
et une action qui fait que la séquence continue a une 
récompense immédiate de 0, mais aura également une récompense future.


Rappelez-vous que la formule clé pour le Q-learning est ci-dessous.
Chaque fois que nous sommes dans un état `s` et que nous prenons une action `a`, nous
pouvons mettre à jour la valeur Q `Q(s, a)` selon

.. math::

    Q(s, a) \leftarrow Q(s, a) + \alpha \cdot (Q_{new} - Q_{old})

tel que
:math:`\alpha` est le facteur d'apprentissage,
:math:`Q_{new}` est une nouvelle estimation de valeur,
:math:`Q_{old}` est l'ancienne estimation de valeur,
Le *facteur d'apprentissage* détermine à quel point nous valorisons les
nouvelles informations par rapport aux informations que nous avons déjà.
La *nouvelle estimation de valeur* représente la somme de la
récompense reçue pour l'action en cours et de l'estimation de toutes les
récompenses futures que l'agent recevra.
L'*ancienne estimation de valeur* est la valeur existante pour `Q(s, a)`.
En appliquant cette formule à chaque fois que notre agent entreprend une
nouvelle action, au fil du temps, il commencera à apprendre quelles
manipulations sont meilleures dans n'importe quel état.


Présentation
============

En regardant dans le code source, on trouve le répertoire ``src`` qui contient
les implémentation et le répertoire ``test`` où se trouvent des tests unitaires.

``src/nim/__init__.py``
    Les implémentations qui sont directement sous l'espace de nom (*namespace*)
    ``nim`` sont dans ce fichier. Il s'agit de types de bases et de fonctions
    qui soutiennent les règles du jeu lui-même.

``src/nim/ai.py``
    L'implémentation du Q-Learning est entièrement dans ce fichier.

    Portez une attention particulière aux méthodes
    ``get_q_value``, ``update_q_value``, ``best_future_reward`` et
    ``choose_action`` qui sont à compléter.


``src/nim/run.py``
    L'interface en ligne de commande ainsi que les points d'entrées du projet
    sont dans ce module.
    Vous n'avez pas à modifier ce fichier.

Commencez par lire tous les fichiers du dépôt. Le code y est bien documenté;
il serait redondant de reprendre les explications ici.

**Remarquez les mentions** ``TODO``.
Ces mentions vous indiquent le travail à compléter pour votre TP!
La mentions ``TODO`` précise aussi la valeur de la tâche à accomplir.


Remise
======

Vous avez deux semaines jusqu'à 23h59 pour compléter le TP.

Pour le remettre, créer un *fork* sur GitHub (ou GitLab), complétez votre
code et poussez vos changement sur la branche ``main``

N'oubliez pas de **donner l'URL de votre TP à votre enseignant**.


Aide-mémoire
============

Synchroniser le bon interpréteur et les dépendances

.. code::

    uv sync

Exécuter tous les scripts ``nox``:

.. code::

    uv run nox

Obtenir la liste des scripts ``nox``:

.. code::

    uv run nox -l

Exécuter un script particulier (par exemple ``format_py``):

.. code::

    uv run nox -s format_py

Exécuter tous les scripts ayant une certaine étiquette (par exemple ``py``):

.. code::

    uv run nox -t py

Obtenir de l'aide avec [``nox``](https://nox.thea.codes/en/stable/):

.. code::

    uv run nox --help

Obtenir de l'aide avec [``uv``](https://docs.astral.sh/uv/)

.. code::

    uv --help


Spécifications
==============

Vous devez remplacer chaque mentions ``TODO`` par votre réponse.
Se faisant, suivez les instructions ci-dessous:

*   Chaque mention ``TODO`` comporte un identifiant utilisé pour la correction,
    une valeur d'évaluation et des instruction.

    Les ``TODO`` on la forme suivante:

    .. code:: text
        TODO: qualité_du_code (10 points)
          Respectez le style du dépôt. Utilisez les autres implémentations et
          documentations comme des modèles pour votre contribution.

    (Ceci est aussi un réel ``TODO``)

*   Les tests inclus dans ce dépôt doivent être conservés et passer

*   Ajoutez autant de tests que vous jugez pertinent.

Voici les todos:

=================================  ====================  ==================================
Identifiant                        Points                Chemin
=================================  ====================  ==================================
``qualité_du_code``                10                    README.rst#l92
``discussion``                     10 bonus              README.rst#l128
``QValue``                         5                     src/nim/__init__.py#l80
``transition``                     10                    src/nim/__init__.py#l122
``available_actions``              10                    src/nim/__init__.py#l127
``epsilon``                        5                     src/nim/ai.py#l28
``alpha``                          5                     src/nim/ai.py#l35
``gamma``                          2                     src/nim/ai.py#l56
``get_q_value``                    10                    src/nim/ai.py#l94
``update_q_value``                 10                    src/nim/ai.py#l131
``best_future_reward``             10                    src/nim/ai.py#l145
``choose_action``                  10                    src/nim/ai.py#l164
``test_available_actions``         10                    test/test_available_actions.py#l19
``test_number_of_piles_provided``  3                     test/test_new_random_board.py#l21
**Total cumulatif**                **100 (+ 10 bonus)**  **-**
=================================  ====================  ==================================

Discussion
==========

TODO: discussion (10 points bonus)
  Testez le Q-Learning de nim avec différentes valeurs de
    :math:`\epsilon`, :math:`\alpha` et :math:`\gamma`.
    Commentez vos observations et expliquez votre méthodologie.

J'ai utilisé une seul pile(3,) pour pouvoir mieux observer les changements selon Epsilon, Alpha et Gamma.
Je répète toujours la même action afin de pouvoir comparer mes résultat.
Dans mon exercice,  j'enleve 1 de la pile 0 et je fais 4 parties.

Test-1 Epsilon 0 : :math:`\epsilon` = 0 | :math:`\alpha` = 0,5 | :math:`\gamma` = 0,7
 - Première partie gagné par l'humain (AI retire 2 du tas 0)
 - Deuxième humain partie perdu (AI retire 1 du tas 0)
 - Troisième humain partie perdu (AI retire 1 du tas 0)
 - Quatrième humain partie perdu (AI retire 1 du tas 0)

Test-2 Epsilon 0,5 : :math:`\epsilon` = 0,5 | :math:`\alpha` = 0,5 | :math:`\gamma` = 0,7
 - Première partie gagné par l'humain (AI retire 2 du tas 0)
 - Deuxième humain partie perdu (AI retire 1 du tas 0)
 - Troisième humain partie perdu (AI retire 1 du tas 0)
 - Quatrième humain partie perdu (AI retire 1 du tas 0)

Test-3 Epsilon 1 : :math:`\epsilon` = 1 | :math:`\alpha` = 0,5 | :math:`\gamma` = 0,7
 - Première partie humain perdu (AI retire 1 du tas 0)
 - Deuxième partie humain perdu (AI retire 1 du tas 0)
 - Troisième partie humain perdu (AI retire 1 du tas 0)
 - Quatrième partie humain perdu (AI retire 1 du tas 0)

Test-4 Alpha 0 : :math:`\epsilon` = 0,1 | :math:`\alpha` = 0 | :math:`\gamma` = 0,7
 - Première partie gagné par l'humain (AI retire 2 du tas 0)
 - Deuxième partie humain perdu (AI retire 1 du tas 0)
 - Troisième partie humain perdu (AI retire 1 du tas 0)
 - Quatrième partie gagné par l'humain (AI retire 2 du tas 0)

Test-5 Alpha 0,5 : :math:`\epsilon` = 0,1 | :math:`\alpha` = 0,5 | :math:`\gamma` = 0,7
 - Première partie humain perdu (AI retire 1 du tas 0)
 - Deuxième partie humain perdu (AI retire 1 du tas 0)
 - Troisième partie humain perdu (AI retire 1 du tas 0)
 - Quatrième partie gagné par l'humain (AI retire 2 du tas 0)

Test-6 Alpha 1 : :math:`\epsilon` = 0,1 | :math:`\alpha` = 1 | :math:`\gamma` = 0,7
 - Première partie humain perdu (AI retire 1 du tas 0)
 - Deuxième partie humain perdu (AI retire 1 du tas 0)
 - Troisième partie humain perdu (AI retire 1 du tas 0)
 - Quatrième partie humain perdu (AI retire 1 du tas 0)

Test-7 Gamma 0 : :math:`\epsilon` = 0,1 | :math:`\alpha` = 0,5 | :math:`\gamma` = 0
 - Première partie gagné par l'humain (AI retire 2 du tas 0)
 - Deuxième partie gagné par l'humain (AI retire 2 du tas 0)
 - Troisième partie humain perdu (AI retire 1 du tas 0)
 - Quatrième partie humain perdu (AI retire 1 du tas 0)

Test-8 Gamma 0,5 : :math:`\epsilon` = 0,1 | :math:`\alpha` = 0,5 | :math:`\gamma` = 0,5
 - Première partie humain perdu (AI retire 1 du tas 0)
 - Deuxième partie humain perdu (AI retire 1 du tas 0)
 - Troisième partie gagné par l'humain (AI retire 2 du tas 0)
 - Quatrième partie humain perdu (AI retire 1 du tas 0)

Test-9 Gamma 1 : :math:`\epsilon` = 0,1 | :math:`\alpha` = 0,5 | :math:`\gamma` = 1
 - Première partie humain perdu (AI retire 1 du tas 0)
 - Deuxième partie gagné par l'humain (AI retire 2 du tas 0)
 - Troisième partie gagné par l'humain (AI retire 2 du tas 0)
 - Quatrième partie humain perdu (AI retire 1 du tas 0)


TODO: retroaction (5 points bonus)
  Produisez une rétroaction constructive afin d'améliorer ce TP.
