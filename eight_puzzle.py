#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename, algorithm, param):
    ''' processes a file, algorithm, and param and analyzes the amount of
    moves and states it would take to solve it
    '''
    file = open(filename, 'r')
    count = 0
    avg_moves = 0
    avg_test_states = 0
    
    for line in file:
        line = line[:-1]
        
        init_board = Board(line)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        if searcher == None:
            return

        soln = None
        print(line + ': ', end='')
       
        try:
            soln = searcher.find_solution(init_state)
        except KeyboardInterrupt:
            print('search terminated,', end = '')



        if soln == None:
            print(' no solution')
        else:
            count += 1
            avg_moves += soln.num_moves
            print(soln.num_moves, 'moves, ', end = '')
            avg_test_states += searcher.num_tested
            print(searcher.num_tested, 'states', end = '')
            
            print()
            
    print()
    print('solved', count, 'puzzles')
    if (count != 0):
        print('averages:', avg_moves/count, 'moves,', avg_test_states/count, 'states tested')
    
        