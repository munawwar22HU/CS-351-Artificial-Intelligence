# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from util import *

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
       
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """

        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """

        util.raiseNotDefined()
        
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        util.raiseNotDefined()





def aStarSearch(problem):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR A* CODE HERE ***"  
    # Initialize frontier to just the starting position
    frontier=PriorityQueue()
    initialState=problem.getStartState() 
    frontier.push(initialState,0)


    #Dictionaries to maintain path and cost
    previousNode={}
    previousNode[initialState]=None
    previousCost={}
    explored = set()
    nodes=[]
    previousCost[initialState]=0

    # Keep looping until solution found
    while True:

        #If nothing left in frontier, then no path
        if frontier.isEmpty():
            raise Exception("no solution")

        # Choose a node from the frontier
        current=frontier.pop()
        
        # Mark node as explored
        explored.add(current)
     
        # Add neighbors to frontier
        for successor,action,stepcost in problem.getSuccessors(current):
            newCost=previousCost[current]+stepcost
            if successor not in previousCost or newCost<previousCost[successor]:
                previousCost[successor]=newCost
                priority=newCost+problem.getHeuristic(successor)
                frontier.push(successor,priority)
                previousNode[successor]=current
                
                #If node is the goal, then we have a solution
                if problem.isGoalState(successor):
                    current = successor
                    while True:
                        nodes=[current]+nodes
                        temp=current
                        current=previousNode[current]
                        del previousNode[temp]
                        if not current:
                            break      
                    return nodes

    
                

