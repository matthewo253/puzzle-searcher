#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        ''' intializes attributes of the class'''
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit


    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def add_state(self, new_state):
        ''' adds to the state'''
        self.states += [new_state]
        
    def should_add(self, state):
        ''' finds if a state should be added to the states'''
        if(self.depth_limit != -1):
            if(state.num_moves > self.depth_limit):
                return False
        if(state.creates_cycle() == True):
            return False
        return True
    
    def add_states(self, new_states):
        ''' finds if a list of states should be added'''
        for i in new_states:
            if(self.should_add(i) == True):
                self.add_state(i)
        
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        ''' finds the solution to the goal tiles and the amount of moves
        needed '''
        self.add_state(init_state)
        while len(self.states) > 0:
                self.num_tested += 1
                x = self.next_state()
                if(x.is_goal() == True):
                    return x
                else:
                    self.add_states(x.generate_successors())
            
        return None
    


### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    ''' performs breadth firsst search '''
    def next_state(self):
        s = self.states[0]
        self.states.remove(s)
        return s
    
class DFSearcher(Searcher):
    ''' performs depth first search '''
    def next_state(self):
        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def h1(state):
    ''' returns the number of misplaced spots'''
    return state.board.num_misplaced()

def h2(state):
    return (state.board.num_misplaced() + 1)//2

### Add your other heuristic functions here. ###


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        super().__init__(self)
        self.depth_limit = -1
        self.heuristic = heuristic


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        s = max(self.states)
        self.states.remove(s)
        return s[-1]


### Add your AStarSeacher class definition below. ###
class AStarSearcher(Searcher):
    def __init__(self, heuristic):
        super().__init__(self)
        self.depth_limit = -1
        self.heuristic = heuristic

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def add_state(self, state):
        ''' adds priority to the states along with the states'''
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        ''' removes the biggest state depending on the priority '''
        s = max(self.states)
        self.states.remove(s)
        return s[-1]

    
    def priority(self, state):
        ''' creates the priority '''
        return -1 * (self.heuristic(state) + state.num_moves)
