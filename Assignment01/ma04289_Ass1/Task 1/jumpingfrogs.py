from search import *
import copy



def PossibleLegalMoves(current):
    """
    Returns a list of possible legal moves from the current state.

    Moves consist of moving right 1 unit, moving right 2 units, move left 1 unit, move left 2 units.
    Moves are encoded as tuple where the first element is the old position of the vacant rock and the second 
    position is the new position of the vacant rock.

    """
    GreenFrogs = set(["A","B","C"])
    BrownFrogs = set(["X","Y","Z"])
    GreenIndex = {"A":0, "B":1,"C":2}
    BrownIndex = {"X":4, "Y":5,"Z":6}
    moves_index= [-2,-1,1,2]
    moves = list()
    vacantRock = current.index("_")
    for i in moves_index:
        if 0<=(i+vacantRock)<= 6:
            if (current[i+vacantRock] in GreenFrogs) and (vacantRock > GreenIndex[current[i+vacantRock]]):
                moves.append((vacantRock,i+vacantRock))
            elif (current[i+vacantRock] in BrownFrogs) and (vacantRock < BrownIndex[current[i+vacantRock]]):
                moves.append((vacantRock,i+vacantRock))
    return moves


def Results(current,move):
    """Returns a new Puzzle State with the current state and vacant Rock Location
    updated based on the provided move.
    """
    NextState = copy.deepcopy(current)
    NextState[move[1]],NextState[move[0]] =  NextState[move[0]], NextState[move[1]]

    return NextState


class JumpingFrogPuzzleProblem(SearchProblem):
    def __init__(self):
        self.current = Node(["A","B","C","_","X","Y","Z"])
        self.vacantRock = 3
        self.GreenFrogs = set(["A","B","C"])
        self.BrownFrogs = set(["X","Y","Z"])
        self.GreenIndex = {"A":0, "B":1,"C":2}
        self.BrownIndex = {"X":4, "Y":5,"Z":6}

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        return self.current

    def isGoalState(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        GoalState = ["X","Y","Z","_","A","B","C"]

        return state.current == GoalState

    def getSuccessors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        Successors = []
        for move in PossibleLegalMoves(state.current):
            x = Node(Results(state.current,move))
            Successors.append ((x,move,abs(move[1]-move[0])))
        return Successors
    def getHeuristic(self,state):
        """
         state: the current state of agent

        This function returns the heuristic of current state of the agent which will be the 
        estimated distance from goal.
         
        """
        GoalPos = {"X":0,"Y":1,"Z":2,"A":4,"B":5,"C":6}
        ManhattanDistance = 0
        for i in range(7):
            if state.current[i]!="_":
                if state.current[i]!=GoalPos[state.current[i]]:
                    ManhattanDistance+=1
                    
        if len(PossibleLegalMoves(state.current))==0: return ManhattanDistance + 10000000
        return ManhattanDistance


FrogSearchProblem = JumpingFrogPuzzleProblem()
path = aStarSearch(FrogSearchProblem)

for i in path:
    print(i.current)
                






        
