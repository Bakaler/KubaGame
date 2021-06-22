# KubaGame

Creates a game of Kuba where players have the goal of knocking off 7 red marbles, knocking off all
opposing marbles, or blocking all opposing marbles from making a move. The program has 3 classes, Marble, Board,
and KubaGame, which all create a physical environment where the game is played out.

This program utilizes Linked List to track marbles, a dictionary with list to track the board, and uses a variety
of methods that showcase loops, ifs/elifs, recursion, and helper functions. Get/Set methods are also used across
the classes as the 3 work together almost entirely.

# Classes
    
Marble
    The marble class represents a marble on the board
    Each marble in play is a node that references another marble on the board
    When marbles are knocked out of play, they are removed from the linked list (Forever...)

    The Marble class represents marble nodes in a linked list.
    Each marble has an 'color' and an 'id'
    The color is used to determine the player who owns the marble where as the id is used to idetify the specific marble
    being assessed in a situation
        More on the id -
         The id is important because when iterating through the linked list, without the id, the first marble to match
         the associating color would undergo KubaGame methods. This would result in vital errors because the first
         marble associated with a color is not always the marble being requested
    The marble class works with the board class as a physical space for the marbles to exist, and it works with the
    KobaGame class when being moved around the board class
    
Board
    The board class represents a board object that a game of Kuba is played out on.
    The board is responsible for:
        Initializing a linked list of Marbles
        Tracking physical location of Marbles
        Tracking memory location of Marbles
    A board resembles:

Row0        ['Edge  |||', 'Edge  |||', 'Edge  |||', 'Edge  |||', 'Edge  |||', 'Edge  |||', 'Edge  |||', 'Edge  |||', 'Edge  |||']
            --------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||
Row1        ['Edge  |||', 'W     |||', 'W     |||', 'X     |||', 'X     |||', 'X     |||', 'B     |||', 'B     |||', 'Edge  |||']
            --------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||
Row2        ['Edge  |||', 'W     |||', 'W     |||', 'X     |||', 'R     |||', 'X     |||', 'B     |||', 'B     |||', 'Edge  |||']
            --------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||
Row3        ['Edge  |||', 'X     |||', 'X     |||', 'R     |||', 'R     |||', 'R     |||', 'X     |||', 'X     |||', 'Edge  |||']
            --------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||
Row4        ['Edge  |||', 'X     |||', 'R     |||', 'R     |||', 'R     |||', 'R     |||', 'R     |||', 'X     |||', 'Edge  |||']
            --------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||
Row5        ['Edge  |||', 'X     |||', 'X     |||', 'R     |||', 'R     |||', 'R     |||', 'X     |||', 'X     |||', 'Edge  |||']
            --------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||
Row6        ['Edge  |||', 'B     |||', 'B     |||', 'X     |||', 'R     |||', 'X     |||', 'W     |||', 'W     |||', 'Edge  |||']
            --------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||
Row7        ['Edge  |||', 'B     |||', 'B     |||', 'X     |||', 'X     |||', 'X     |||', 'W     |||', 'W     |||', 'Edge  |||']
            --------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||
Row8        ['Edge  |||', 'Edge  |||', 'Edge  |||', 'Edge  |||', 'Edge  |||', 'Edge  |||', 'Edge  |||', 'Edge  |||', 'Edge  |||']

    The physical board consist of a 9x9 grid where each space is occupied by a marble object, self._empty, or self,
    _edge. The self._empty and self._edge both represent an unoccupied space when being assessed in viable pushing,
    but the self._edge is treated special in methods for scoring. Marbles can not be retrieved once they fall off the
    the board

    Each space on the board is stored in a dictionary, as such: { 'rowkeyX' : [EDGE, SPACE, SPACE, ...4..., SPACE, EDGE]
    In the 7 center indices, marble objects or self._empty is stored
    rowkeyX where X has a string of 0-8
    rowkey0 and rowkey8 are reserved for self_edge list
    
KubaGame

    The KubaBoard object represents a "round" of Kuba between two players on a board object.
    The KubaGame class is responsible for:
        Calling, storing, and altering the board class
        Tracking current players, each with a name string and color string
        Tracking the current players turn
        Tracking the score via list [0,0] <-- [Player 1 Red Points, Player 2 Red Points]
        Tracking the Winner
        Using memorization for the Ko rule
        Making moves
