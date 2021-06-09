import csv
import sys
from search import *



# Maps Cities to their ids

Cities = {}

# Map Cities to their heuristics

Heuristics = {}


# Map Cities to their neighbours

Connections = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    with open(f"{directory}/cities.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f,fieldnames=["City"])
        index = 0
        for row in reader:
            Cities[row["City"]]=index
            index+=1

    with open(f"{directory}/Connections.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            del row['']
            Connections[count] = dict()
            
            for key,value in row.items():
                Connections[count][Cities[key]]=int(value)
            count+=1
  
    with open(f"{directory}/heuristics.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            del row['']
            Heuristics[count] = dict()
            for key,value in row.items():
                Heuristics[count][Cities[key]]=int(value)
            count+=1
def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "CSV"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")
    
 
    source = city_id_for_name(input("Source: "))
    if source is None:
        sys.exit("City not found.")
    target = city_id_for_name(input("Target: "))
    if target is None:
        sys.exit("City not found.")


    RouteSearchProblem = RoutePlanning(source,target)
    path = aStarSearch(RouteSearchProblem)

    for i in path:

        print(city_name_for_id(i.current))
def city_name_for_id(id):
    for key,value in Cities.items():
        if value == id: return key

def city_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    if name not in Cities: return False 
    else: return Cities[name]

class RoutePlanning(SearchProblem):
    def __init__(self,source,target):
        self.start = Node(source)
        self.target = Node(target)

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        return self.start

    def isGoalState(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        return  state.current== self.target.current

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        Successors = []
        City_id = state.current
        for key,value in Connections[City_id].items():
            if value !=-1 and value!=0:
                x = Node(key)
                Successors.append ((x,key,value))
        return Successors

    def getHeuristic(self,state): 

        return Heuristics[state.current][self.target.current]

if __name__ == "__main__":
    main()
