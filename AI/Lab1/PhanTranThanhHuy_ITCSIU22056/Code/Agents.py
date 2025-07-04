from game import Agent
from game import Directions
import random

class DumbAgent(Agent):
    "An agent that goes East until it can't."
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.EAST in state.getLegalPacmanActions():
            print("Going East.")
            return Directions.EAST
        else:
            print("Stopping.")
            return Directions.STOP

 
class RandomAgent():
    "An agent that goes randomly."
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py) and chooses a random action."
        legal_actions = state.getLegalPacmanActions()
        
        if legal_actions:
            action = random.choice(legal_actions)
            return action
        else:
            return Directions.STOP

class BetterRandomAgent(Agent):
    "An agent that selects a random legal action at each step, excluding 'Stop' unless necessary."
    
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py) and chooses a random action."
        legal_actions = state.getLegalPacmanActions()
        
        if Directions.STOP in legal_actions and len(legal_actions) > 1:
            legal_actions.remove(Directions.STOP)
        
        if legal_actions:
            action = random.choice(legal_actions)
            return action
        else:
            return Directions.STOP
        
class ReflexAgent(Agent):
    "An agent that prioritizes eating food pellets and moves randomly otherwise."
    
    def getAction(self, state):
        "Determines the best action to take based on food availability."
        legal_actions = state.getLegalPacmanActions()
        
        if Directions.STOP in legal_actions and len(legal_actions) > 1:
            legal_actions.remove(Directions.STOP)
        
        for action in legal_actions:
            successor = state.generatePacmanSuccessor(action)
            if successor and successor.getNumFood() < state.getNumFood():
                return action
        
        action = random.choice(legal_actions)
        return action
