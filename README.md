# Description de notre projet Reversi

## Algorithmes Implémentés

- **MiniMax** : Un algorithme classique de recherche en arbre pour les jeux à deux joueurs.
- **AlphaBeta** : Une version optimisée de MiniMax qui utilise l'élagage alpha-bêta pour réduire le nombre de nœuds évalués.
- **NegaMax** : Une variante simplifiée de MiniMax qui unifie les fonctions d'évaluation pour les deux joueurs.
- **NegaMaxAlphaBeta** : Combine NegaMax avec l'élagage alpha-bêta, offrant une exploration rapide et profonde avec optimisation du temps.

## Performances des Algorithmes

### MiniMax

- Temps pour le premier meilleur coup avec une profondeur de 7 : 6.39 sec.
- Profondeur maximale atteinte en 10 secondes (ID) : 8.

### AlphaBeta

- Temps pour le premier meilleur coup avec une profondeur de 7 : 1.49 sec.
- Profondeur maximale en 10 secondes (ID) : 9.

### NegaMax

- Temps pour le premier meilleur coup avec une profondeur de 7 : 5.17 sec.
- Profondeur maximale atteinte en 10 secondes (ID) : 8.

### NegaMaxAlphaBeta (Meilleure Performance)

- Temps pour le premier meilleur coup avec une profondeur de 7 : 0.85 sec.
- Profondeur maximale atteinte en 10 secondes (ID) : 10.
- **Note**: C'est l'algorithme qui va chercher le plus loin possible dans l'arbre de jeu avec une contrainte de temps.

**Pour que notre IA soit la plus performante possible, il faut qu'elle utilise l’algorithme NegaMaxAlphaBeta.**

**Raison de la performance** : Optimisation maximale avec élagage alpha-bêta et recherche itérative, permettant une exploration rapide et profonde de l'arbre de jeu.

## Description Heuristique Codée

**Heuristique V2** : Heuristique utilisée par notre joueur. Elle ajoute une pondération en fonction de la position sur le plateau (coins, bords, intérieur). On aurait pu intégrer des facteurs supplémentaires comme la mobilité et la stabilité pour améliorer encore sa performance.

## Description des Classes

### Player

- **Rôle** : Classe abstraite de base pour différents types de joueurs (humains ou IA).
- **Fonctionnalités** :
  - Stockage de la couleur du joueur.
  - Méthode abstraite `get_move` pour obtenir le mouvement du joueur.

### HumanPlayer

- **Rôle** : Sous-classe de `Player`, représentant un joueur humain.
- **Fonctionnalités** :
  - Implémentation de la méthode `get_move`.

### AIPlayer

- **Rôle** : Sous-classe de `Player`, représentant notre joueur IA sans Iterative Deepening (Première version).
- **Fonctionnalités** :
  - Implémentation de différentes stratégies d'IA (MiniMax, Alpha-Beta, NegaMax, etc.).
  - Sélection du meilleur coup basé sur l'état actuel du plateau.

### AIPlayer_id

- **Rôle** : Deuxième version de notre joueur IA, utilisant "Iterative Deepening".
- **Fonctionnalités** :
  - Gestion du temps pour chaque coup.
  - Amélioration des algorithmes existants pour une recherche dynamique avec contrainte de temps.

### Game

- **Rôle** : Classe principale orchestrant le jeu.
- **Fonctionnalités** :
  - Initialisation du plateau et des joueurs.
  - Gestion de la boucle de jeu et détermination du gagnant.
