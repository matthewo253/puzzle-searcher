#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = digitstr[3 * r + c]
                if(self.tiles[r][c] == '0'):
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###
    
    def __repr__(self):
        '''
        creates a row of strings of the tiles and replaces 0 with a blank
        '''
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if(self.tiles[r][c] == '0'):
                    s += '_ '
                else:
                    s += str(self.tiles[r][c]) + ' '
            s += '\n'
        return s
                
    def move_blank(self, direction):
        '''
        moves the blank to positions where it is not going out of bounds
        '''
        vari = 0      
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if(self.tiles[r][c] == '0'):
                    if(direction == 'up' and r != 0):
                        vari = self.tiles[r - 1][c]
                        self.tiles[r - 1][c] = self.tiles[r][c]
                        self.tiles[r][c] = vari
                        self.blank_r = r - 1
                        return True
                    elif(direction == 'left' and c != 0):
                        vari = self.tiles[r][c - 1]
                        self.tiles[r][c - 1] = self.tiles[r][c]
                        self.tiles[r][c] = vari
                        self.blank_c = c - 1
                        return True
                    elif(direction == 'right' and c != len(self.tiles) - 1):
                        vari = self.tiles[r][c + 1]
                        self.tiles[r][c + 1] = self.tiles[r][c]
                        self.tiles[r][c] = vari
                        self.blank_c = c + 1
                        return True
                    elif(direction == 'down' and r != len(self.tiles) - 1):
                        vari = self.tiles[r + 1][c]
                        self.tiles[r + 1][c] = self.tiles[r][c]
                        self.tiles[r][c] = vari
                        self.blank_r = r + 1
                        return True
                    else:
                        return False
    
    def digit_string(self):
        '''
        returns the tiles in a string format 
        '''
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s+= str(self.tiles[r][c])
        return s
    
    def copy(self):
        '''
        copies the board into a new object
        '''
        newCopy = Board(self.digit_string())
        return newCopy
    
    def num_misplaced(self):
        '''
        tells you the amount of numbers in tiles that don't line up with the 
        GOAL_TILES
        '''
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if(self.tiles[r][c] != '0'):
                    if(self.tiles[r][c] != GOAL_TILES[r][c]):
                        count += 1
        return count
    
    def __eq__(self, other):
        '''
        determines if one tile has the same values as another
        '''
        if(self.tiles == other.tiles):
            return True
        return False
                
        
        

