# Author: Alexander Baker
# Date: 5/27/2021
# Description: Creates a game of Kuba where players have the goal of knocking off 7 red marbles or knocking off all
# opposing marbles or blocking all opposing marbles from making a move. The program has 3 classes, Marble, Board,
# and KubaGame, which all create a physical environment where the game is played out.
#
# This program utilizes Linked List to track marbles, a dictionary with list to track the board, and uses a variety
# of methods that showcase loops, ifs/elifs, recursion, and helper functions. Get/Set methods are also used across
# the classes as the 3 work together almost entirely.



class marble:
    '''
    The marble class represents a marble on the board
    Each marble in play is a node that references another marble on the board
    When marbles are knocked out of play, they are removed from the linked list (Forever...)
    '''

    def __init__(self, color, id):
        '''
        Initializes a marble object with a color and identifying ID string
        :param color: 'B', 'W', 'R'
        :param id:  '1' - '29'
        When a board is initialized, so are the marbles on that board
        '''
        self._color = color
        self._id = id
        self._next = None

    def get_id(self):
        '''
        :return: marble object id name
        '''
        return self._id

    def get_color(self):
        '''
        :return: marble object color
        '''
        return self._color

    def get_next(self):
        '''
        :return: next marble object in Linked List
        '''
        return self._next

    def set_id(self, id):
        '''
        sets a marbles objects id
        '''
        self._id = id

    def set_color(self, color):
        '''
        sets a marble objects color
        '''
        self._color = color


    def set_next(self, next_node):
        '''
        sets the next marble object in linked list
        '''
        self._next = next_node

class board:
    '''
    The board class represents a board object that a game of Kuba is played out on.
    '''

    def __init__(self):
        '''
        Initializes the Kuba board by:
            Creating 29 marble objects
            Creating an 8x8 board (7x7 of which is playable)
            Placing marble objects on that board
        '''
        self._head = None           # First marble object created/ first marble in list
        self.set_up()               # Creates 29 marbles
        self._empty = None          # An empty space on the board that is a unique None
        self._edge = "Edge"         # An edge piece on the board that is considered empty but has special attributes
                                    # when being investigated in methods

        self._gameboard = {"row0" : [self._edge,self._edge,self._edge,self._edge,self._edge,self._edge,self._edge,
                                     self._edge,self._edge],
                           "row1" : [self._edge, self.get_marble("9"), self.get_marble("10"), self._empty, self._empty,
                                     self._empty, self.get_marble("1"), self.get_marble("2"), self._edge],
                           "row2" : [self._edge, self.get_marble("11"), self.get_marble("12"), self._empty,
                                     self.get_marble("17"), self._empty, self.get_marble("3"), self.get_marble("4"),
                                     self._edge],
                           "row3" : [self._edge, self._empty, self._empty, self.get_marble("18"), self.get_marble("19"),
                                     self.get_marble("20"), self._empty, self._empty, self._edge],
                           "row4" : [self._edge, self._empty, self.get_marble("21"), self.get_marble("22"),
                                     self.get_marble("23"), self.get_marble("24"), self.get_marble("25"),
                                     self._empty, self._edge],
                           "row5" : [self._edge, self._empty, self._empty, self.get_marble("26"), self.get_marble("27"),
                                     self.get_marble("28"), self._empty, self._empty, self._edge],
                           "row6" : [self._edge, self.get_marble("5"), self.get_marble("6"), self._empty,
                                     self.get_marble("29"), self._empty, self.get_marble("13"), self.get_marble(
                                   "14"), self._edge],
                           "row7" : [self._edge, self.get_marble("7"), self.get_marble("8"), self._empty, self._empty,
                                     self._empty, self.get_marble("15"), self.get_marble("16"), self._edge],
                           "row8" : [self._edge,self._edge,self._edge,self._edge,self._edge,self._edge,self._edge,
                                     self._edge,self._edge], }

    def set_up(self):
        '''
        :return: 29 marble node objects that are used to play the game
        '''
        color = ["B", "W", "R"]
        id = "1"
        for x in range(len(color)):     # 0 = 'B', 1 = 'W', 2 = 'R'
            if x <= 1:
                for y in range(8):      # 8 'B' marbles and 8 'W' marbles
                    self.add(color[x], id)
                    id = int(id)
                    id += 1             # increases id key
                    id = str(id)
            if x == 2:
                for y in range(13):     # 13 'R' marbles
                    self.add(color[x], id)
                    id = int(id)
                    id += 1             # increases id key
                    id = str(id)

    def get_row(self, rowkey):
        '''
        :param rowkey: 'row' + str(0-8)
        :return: returns row list [edge, c0, c1, c2, c3, c4, c5, c6, edge]
        '''
        return self._gameboard[rowkey]

    def get_marble(self, id):
        '''
        :param id: id number 1-29
        :return: returns a marble that has a matching id
         Helper function for rec_get_marble
        '''
        return self.rec_get_marble(self.get_head(), id)

    def rec_get_marble(self, a_marble, id):
        '''
        :param a_marble: inspected marble (starts at head)
        :param id: id number 1-29
        :return: def get_marble, marble object
        iterates through a linked list of marbles, starting at head until it finds a matching id or falls of the list
        '''
        if a_marble is None:            #Falls off the edge of the linked list
            return False
        if a_marble.get_id() == id:     #Finds the marble identiying with the id
            return a_marble
        else:                           #Recurssive call
            return self.rec_get_marble(a_marble.get_next(), id)

    def get_head(self):
        '''
        :return: a boards first marble in the linked list
        '''
        return self._head

    def set_head(self, head):
        '''
        :param head: marble object/node
        :return: sets the head of the board object with a marble object
        '''
        self._head = head

    def get_coordinate(self, coordinates):
        '''
        :param coordinates: location on the board from 0,0 to 6,6 (you can look from -1,-1 to 7,7 but those will return
        none as they are the edge of the board)
        :return: Returns 'X' if location is empty or marble object if occupied
        '''
        t_row = coordinates[0]
        column = coordinates[1]
        t_row += 1                  # Because 0,0 is in column 1, row 1, we add 1 to each
        column += 1                 # The reason for offset is the board edge
        row = "row" + str(t_row)    # 'row' + str(t_row) = (e.g) row0 or row1 or row2
        if self._gameboard[row][column] == self._empty:     # Unoccupied board space
            return "X"
        if self._gameboard[row][column] == self._edge:      # edge of board
            return "X"
        return self._gameboard[row][column].get_color()     # In case of marble in location of coordinates

    def get_gameboard(self):
        '''
        :return: returns the gameboard
        '''
        return self._gameboard

    def set_gameboard(self, state):
        '''
        :param state: current state of the board
        :return: sets the game board
        '''
        self._gameboard = state

    def set_empty(self):
        '''
        :return: sets a space to empty
        '''
        return self._empty

    def add(self, color, id):
        """
        Adds a marble node containing a color and id to the linked list
        """
        if self._head is None:                  #If first marble
             self.set_head(marble(color, id))
        else:                                   #Every marble there on out
            current = self._head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(marble(color, id))

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print("[", current.get_id(), "+", current.get_color(), "]", end=" ")
            current = current.get_next()
        print()

    def remove(self, id):
        '''
        :param id: marble id string
        :return: removes marble object with matching id from linked list
        recursive helper function
        '''
        self.rec_remove(id, self.get_head())

    def rec_remove(self, id, marble, prev=None):
        '''
        :param id: marble id string
        :param marble: marble object being inspected (starts with head)
        :param prev: last marble inspected in case current marble is removed
        :return:
        '''
        if marble is None:                          # If no marble exist / end of linked list
            return
        elif marble.get_id() == id:                 # If current marble id matches
            if prev is None:                        # If marble is the head
                self.set_head(marble.get_next())
            else:                                   # If marble is not head
                prev.set_next(marble.get_next())
        else:                                       # Recurrsive call to iterate through linked list
            self.rec_remove(id, marble.get_next(), marble)

    def display_board(self):
        '''
        :return: returns a digital display of the current game board
        Used in debugging and playing physically
        Because this is not part of the assignment, my comments will be absent from this method
        '''
        key = "row1"
        row_display = []
        while len(row_display) != 9:
            row_display.append("Edge" + "  |||")
        print(row_display)
        row_display = []
        print("--------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||")
        for x in range(7):
            for y in range(9):
                piece = self._gameboard[key][y]
                if piece == self._empty:
                    row_display.append("X    " + " |||")
                    continue
                if piece == self._edge:
                    row_display.append("Edge" + "  |||")
                elif piece.get_color() == "R":
                    row_display.append(piece.get_color() + "  " + "   |||")
                else:
                    row_display.append(piece.get_color() + "     |||")
            print(row_display)
            row_display = []
            print("--------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||----------|||")
            temp = int(key[3])
            temp +=1
            key = str(key[:3] + str(temp))
        while len(row_display) != 9:
            row_display.append("Edge" + "  |||")
        print(row_display)


class KubaGame:
    '''
    The KubaBoard object represents a "round" of Kuba between two players on a board object.
    '''

    def __init__(self, player_1, player_2):
        """
        Intilazies a Kuba game between 2 players
        :param player_1: (playername string, color string) "'B', 'W'"
        :param player_2: (playername string, color string) "'B', 'W'"
        """
        self._board = board()           # Creates and stores a board object
        self._player_1 = player_1       # (playername, color)
        self._player_2 = player_2
        self._current_turn = None       # Tracks player turn
        self._score = [0, 0]            # [Player 1 Red Points, Player 2 Red Points]
        self._winner = None             # Tracks the winner of the game
        self._previous = None           # Stores a previous row or column for the Ko Rule
        self._current = None            # Stores a current row or column for the Ko Rule
        self._attempt = None            # Stores an attempted row or column for the Ko Rule

    def display_board(self):
        '''
        Personal flair for debugging, not part of the project requirements
        Calls onto the board object to display itself
        :return: A text generated representation of the game board
        '''
        return self._board.display_board()

    def get_coords(self, coords):
        '''
        :param coords: (row, column)
        :return: returns marble or x at coordinate
        '''
        return self._board.get_coordinate(coords)

    def set_score(self):
        '''
        Used to set a players score
        '''
        if self._current_turn == self._player_1[0]:
            self._score[0] += 1
        else:
            self._score[1] += 1

    def get_score(self):
        '''
        :return: Current score
        '''
        return self._score

    def get_player(self, player):
        '''
        :param player: returns a player and color
        :return:
        '''
        if player == self._player_1[0]:
            return self._player_1
        else:
            return self._player_2

    def get_color(self, player):
        '''
        :param player: player string
        :return: color of player
        '''
        return self.get_player(player)[1]

    def get_current_turn(self):
        '''
        :return: Current players turn
        '''
        return self._current_turn

    def set_current_turn(self, player):
        '''
        :param player: player name string
        :return: sets the turn to the current player
        '''
        self._current_turn = player
        return self._current_turn

    def get_winner(self):
        '''
        :return: name of winner, None if invalid
        '''
        return self._winner

    def set_winner(self, player):
        '''
        :param player: player name
        :return: sets the winner to the player string
        '''
        self._winner = player


    ### Kobo Rule ###
    def make_move(self, player, coordinates, direction, pushed = False):
        '''
        :param player:          player string being assessed
        :param coordinates:     coordinates player is trying to push
        :param direction:       direction player wants to move
        :param pushed:          NOT FOR CLASS, used to check for a repetition of turns
        :return:                If move is viable, moves marble and changes player turn
                                If move is un-viable, returns board to state before move and keeps turn the same
        '''

        if self.get_current_turn() is None and (player == self._player_1[0] or player == self._player_2[0]):
            self.set_current_turn(player)
            # Sets players turn for very first turn

        if player != self.get_current_turn():
            # If player attempts to take turn out of order
            return False

        if self.get_marble(coordinates) != self.get_color(player):
            # If player attempts to move marble other than their own
            return False

        if self._winner != None:
            #If a winner has been declared
            return False

        if direction == "L":
            if self.get_marble((coordinates[0], coordinates[1] + 1)) != 'X':
                #If space is not self._empty (Such that there is a marble or edge)
                #Will continue is that space is an edge
                if self.get_marble((coordinates[0], coordinates[1] + 1)) is not None:
                    # If opposite of "L" has a marble, returns None
                    return False
            rowkey = "row" + str(coordinates[0]+1)          #Determines the row being moved left and right
            temp_list = self._board.get_row(rowkey)         #Holds the row in the key in the dictionary
            self._current = self._board.get_row(rowkey)[:]      #Holds the current row, in case of revert
            temp_list[coordinates[1]+2:coordinates[1]+2] = [self._board.set_empty()] #Inserts an empty space ?
            x = 0
            #Loops until it finds a valid place to remove a marble/push marbles into empty space
            while rowkey:
                if temp_list[coordinates[1] - x] == None:
                    #If space is empty, pushes marbles
                    del temp_list[coordinates[1] - x]      #removes extra space in row
                    break
                if temp_list[coordinates[1] - x] == "Edge":
                    #If space is edge, removes marble from play
                    if temp_list[coordinates[1] - x + 1].get_color() == self.get_color(self.get_current_turn()):
                        #If marble is current players, reverts back and returns False
                        del temp_list[coordinates[1]+2]
                        return False
                    if temp_list[coordinates[1] - x + 1].get_color() == "R":
                        #If red, add points
                        self.set_score()
                        ###pushed = True   #allows player to take another turn
                        self._board.remove(temp_list[coordinates[1] - x + 1].get_id())
                        del temp_list[coordinates[1] - x + 1]
                    else:
                        # If opponent marble, removes it from play
                        self._board.remove(temp_list[coordinates[1] - x + 1].get_id())
                        ###pushed = True       #allows player to take another turn
                        del temp_list[coordinates[1] - x + 1]
                    break
                x += 1
            self._attempt = temp_list
            if self.The_Kudo_Rule() is False:
                temp_list[:] = self._current
                return False

        elif direction == "R":
            if self.get_marble((coordinates[0], coordinates[1] - 1)) != 'X':
                #If space is not self._empty (Such that there is a marble or edge)
                #Will continue is that space is an edge
                if self.get_marble((coordinates[0], coordinates[1] - 1)) is not None:
                    # If opposite of "R" has a marble, returns None
                    return False
            rowkey = "row" + str(coordinates[0]+1)              #Determines the row being moved left and right
            temp_list = self._board.get_row(rowkey)             #Holds the row in the key in the dictionary
            self._current = self._board.get_row(rowkey)[:]      #Holds the current row, in case of revert
            temp_list[coordinates[1]+1:coordinates[1]+1] = [self._board.set_empty()] #Inserts an empty space ?
            x = 0
            #Loops until it finds a valid place to remove a marble/push marbles into empty space
            while rowkey:
                if temp_list[coordinates[1]+2 + x] == None:
                    # If space is empty, pushes marbles
                    del temp_list[coordinates[1]+2 + x]     #removes extra space in row
                    break
                if temp_list[coordinates[1]+2 + x] == "Edge":
                    # If space is edge, removes marble from play
                    if temp_list[coordinates[1] + x + 1].get_color() == self.get_color(self.get_current_turn()):
                        # If marble is current players, reverts back and returns False
                        del temp_list[coordinates[1]+1]
                        return False
                    if temp_list[coordinates[1] + x + 1].get_color() == "R":
                        # If red, add points
                        self.set_score()
                        self._board.remove(temp_list[coordinates[1] + x + 1].get_id())
                        ###pushed = True   #allows player to take another turn
                        del temp_list[coordinates[1] + x + 1]
                    else:
                        # If opponent marble, removes it from play
                        self._board.remove(temp_list[coordinates[1] + x + 1].get_id())
                        ###pushed = True       #allows player to take another turn
                        del temp_list[coordinates[1] + x + 1]
                    break
                x += 1
            self._attempt = temp_list
            if self.The_Kudo_Rule() is False:
                temp_list[:] = self._current
                return False

        elif direction == "F":
            if self.get_marble((coordinates[0]+1, coordinates[1])) != 'X':
                #If space is not self._empty (Such that there is a marble or edge)
                #Will continue is that space is an edge
                if self.get_marble((coordinates[0]+1, coordinates[1])) is not None:
                    # If opposite of "F" has a marble, returns None
                    return False
            inspected_column = []
            for x in range(9):
                rowkey = "row" + str(x)
                inspected_column.append(self._board.get_row(rowkey)[coordinates[1] +1])
            x = 1
            self._current = inspected_column[:]      #Holds the current row, in case of revert
            inspected_column[coordinates[0] + 2:coordinates[0] + 2] = [self._board.set_empty()]
            while inspected_column:
                if inspected_column[coordinates[0] + x] == None:
                    # If space is empty, pushes marbles
                    del inspected_column[coordinates[0] + x]
                    self.column_exchange(inspected_column, coordinates[1] + 1)
                    break
                if inspected_column[coordinates[0] + x] == "Edge":
                    # If space is edge, removes marble from play
                    if inspected_column[coordinates[0] +x + 1].get_color() == self.get_color(self.get_current_turn()):
                        # If marble is current players, reverts back and returns False
                        return False
                    if inspected_column[coordinates[0] + x + 1].get_color() == "R":
                        # If red, add points
                        self.set_score()
                        self._board.remove(inspected_column[coordinates[0] + x + 1].get_id())
                        ###pushed = True  # allows player to take another turn
                        del inspected_column[coordinates[0] + x + 1]
                        self.column_exchange(inspected_column, coordinates[1] + 1)
                    else:
                        # If opponent marble, removes it from play
                        self._board.remove(inspected_column[coordinates[0] + x + 1].get_id())
                        ###pushed = True  # allows player to take another turn
                        del inspected_column[coordinates[0] + x + 1]
                        self.column_exchange(inspected_column, coordinates[1] + 1)
                    break
                x -= 1
            self._attempt = inspected_column
            if self.The_Kudo_Rule() is False:
                inspected_column[:] = self._current
                self.column_exchange(inspected_column, coordinates[1] + 1)
                return False

        elif direction == "B":
            if self.get_marble((coordinates[0]-1, coordinates[1])) != 'X':
                #If space is not self._empty (Such that there is a marble or edge)
                #Will continue is that space is an edge
                if self.get_marble((coordinates[0]-1, coordinates[1])) is not None:
                    # If opposite of "F" has a marble, returns None
                    return False
            inspected_column = []
            for x in range(9):
                rowkey = "row" + str(x)
                inspected_column.append(self._board.get_row(rowkey)[coordinates[1] +1])
            x = 2
            self._current = inspected_column[:]      #Holds the current row, in case of revert
            inspected_column[coordinates[0] + 1:coordinates[0] + 1] = [self._board.set_empty()]
            while inspected_column:
                if inspected_column[coordinates[0] + x] == None:
                    # If space is empty, pushes marbles
                    del inspected_column[coordinates[0] + x]
                    self.column_exchange(inspected_column, coordinates[1] + 1)
                    break
                if inspected_column[coordinates[0] + x] == "Edge":
                    # If space is edge, removes marble from play
                    if inspected_column[coordinates[0] + x - 1].get_color() == self.get_color(self.get_current_turn()):
                        # If marble is current players, reverts back and returns False
                        return False
                    if inspected_column[coordinates[0] + x - 1].get_color() == "R":
                        # If red, add points
                        self.set_score()
                        self._board.remove(inspected_column[coordinates[0] + x - 1].get_id())
                        ###pushed = True  # allows player to take another turn
                        del inspected_column[coordinates[0] + x - 1]
                        self.column_exchange(inspected_column, coordinates[1] + 1)
                    else:
                        # If opponent marble, removes it from play
                        self._board.remove(inspected_column[coordinates[0] + x - 1].get_id())
                        ###pushed = True  # allows player to take another turn
                        del inspected_column[coordinates[0] + x - 1]
                        self.column_exchange(inspected_column, coordinates[1] + 1)
                    break
                x += 1
            self._attempt = inspected_column
            if self.The_Kudo_Rule() is False:
                inspected_column[:] = self._current
                self.column_exchange(inspected_column, coordinates[1] + 1)
                return False
        else:
            return False


        if pushed is False:
            # If opposing/neutral marble is pushed, player will repeat turn
            # This is the case in which that DOES NOT happen
            if self._current_turn == self._player_1[0]:
                self.set_current_turn(self._player_2[0])
            else:
                self.set_current_turn(self._player_1[0])
        self.check_winner(player)
        return True

    def column_exchange(self, inspected_column, column_coord):
        '''
        Make Move helper function used to insert in a new column after a successful move
        :param inspected_column: A copy of the updated column
        :param column_coord: Column in which is being replaced
        :return:
        '''
        for x in range(len(inspected_column)):
            rowkey = "row" + str(x)
            temp_list = self._board.get_row(rowkey)
            temp_list[column_coord] = inspected_column[x]
        return

    def The_Kudo_Rule(self):
        '''
        Helper function that checks to see if the players move violates the Ko Rule of repetition
        '''
        if self._attempt == self._previous:
            return False
        else:
            self._previous = self._current
            self._current = self._attempt
            self._attempt = None
            return True


    def check_winner(self, player):
        '''
        helper function that checks to see if a player has made a game winning move after all the events of a turn
        Checks for:
            Total Red marble count
            Remaining opponent marbles
            Available opponent moves
        '''

        # Checks to see if player has 7 red marbles
        if player == self._player_1[0]:
            if self._score[0] == 7:
                return self.set_winner(player)
        elif player == self._player_2[0]:
            if self._score[1] == 7:
                return self.set_winner(player)

        # Checks to see if player has any remaining marbles
        if player == self._player_1[0]:
            #checks remianing marbles
            temp_color = self.get_color(self._player_2[0])
            if temp_color == 'B':
                if self.get_marble_count()[1] == 0:
                    return self.set_winner(player)
            if temp_color == 'W':
                if self.get_marble_count()[0] == 0:
                    return self.set_winner(player)

        if player == self._player_2[0]:
            #checks remaining marbles
            temp_color = self.get_color(self._player_1[0])
            if temp_color == 'B':
                if self.get_marble_count()[1] == 0:
                    return self.set_winner(player)
            if temp_color == 'W':
                if self.get_marble_count()[0] == 0:
                    return self.set_winner(player)

        # Calls check_winner_move for viable moves on opposing player (such as a stalemate or blockade)
        if self.check_winner_move(player) is False:
            self.set_winner(player)


        return

    def check_winner_move(self, player):
        '''
        Check_winner helper function that looks at opposing players marbles and checks for viable moves
        '''
        # Goes through marble list until first "B" or "W", according to opposing players color
        # Check for an X or Edge for each marble, if any have an open space, returns true
        # If all marbles of opposing player do not have a viable move, returns False
        if player == self._player_1[0]:
            #Does not inspect outer rows and edges because those always have an open sapce to be pushed
            marble_count = 0
            temp_color = self.get_color(self._player_2)
            for row in range(5):                                                # Row being inspected
                for column in range(5):                                         # Column being inspected
                    if self.get_marble((row +1, column+1)) != 'X':
                        current = self.get_marble((row+1, column+1))
                        if current != temp_color:
                            continue
                        elif self.get_marble((row+1, column + 2)) == 'X':
                            return True
                        elif self.get_marble((row+1, column)) == 'X':
                            return True
                        elif self.get_marble((row + 2, column+1)) == 'X':
                            return True
                        elif self.get_marble((row, column+1)) == 'X':
                            return True
                        else:
                            marble_count += 1
            if temp_color == "B":                                           # If marbles exist outside 1,1 - 5,5
                if marble_count < self.get_marble_count()[1]:               # returns True because move is viable
                    return True
            elif temp_color == "W":
                if marble_count < self.get_marble_count()[0]:
                    return True
        if player == self._player_2[0]:
            marble_count = 0
            temp_color = self.get_color(self._player_1)
            for row in range(5):
                for column in range(5):
                    if self.get_marble((row +1, column+1)) != 'X':
                        current = self.get_marble((row+1, column+1))
                        if current != temp_color:
                            continue
                        elif self.get_marble((row+1, column + 2)) == 'X':
                            return True
                        elif self.get_marble((row+1, column)) == 'X':
                            return True
                        elif self.get_marble((row + 2, column+1)) == 'X':
                            return True
                        elif self.get_marble((row, column+1)) == 'X':
                            return True
                        else:
                            marble_count += 1
            if temp_color == "B":
                if marble_count < self.get_marble_count()[1]:
                    return True
            elif temp_color == "W":
                if marble_count < self.get_marble_count()[0]:
                    return True

        return False




    def get_captured(self, player):
        '''
        :param player: player name string
        :return: current red marbles captured by player
        '''
        if player == self._player_1[0]:
            return self._score[0]
        if player == self._player_2[0]:
            return self._score[0]
        return False

    def get_marble(self, coordinates):
        '''
        takes the coordinates of a cell as a tuple and returns the marble that is present at the location. If no
        marble is present at the coordinate location return 'X'.
        '''
        return self._board.get_coordinate(coordinates)

    def get_marble_count(self):
        '''
        Helper function for rec_marble_count
        '''
        return self.rec_get_marble_count(self._board.get_head())


    def rec_get_marble_count(self, current = None, White = None, Black = None, Red = None):
        '''
        :param current: current color being inspected
        :param White: white number
        :param Black: black number
        :param Red: red number
        :return: number of marbles per color
        '''
        if White is None:
            White = 0
            Black = 0
            Red = 0

        if current == None:
            return (White, Black, Red)

        if current.get_color() == "W":
            White += 1
        elif current.get_color() == "B":
            Black += 1
        else:
            Red += 1

        current = current.get_next()

        return self.rec_get_marble_count(current, White, Black, Red)

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
