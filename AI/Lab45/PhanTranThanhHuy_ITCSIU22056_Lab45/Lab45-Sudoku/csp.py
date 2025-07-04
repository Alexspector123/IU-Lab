# CLASS DESCRIPTION FOR CONSTRAINT SATISFACTION PROBLEM (CSP)

from util import *

class csp:

    # INITIALIZING THE CSP
    def __init__(self, domain=digits, grid=""):
        """
        Unitlist consists of the 27 lists of peers
        Units is a dictionary consisting of the keys and the corresponding lists of peers
        Peers is a dictionary consisting of the 81 keys and the corresponding set of 27 peers
        Constraints denote the various all-different constraints between the variables
        """

        self.variables = [row + str(col) for row in 'ABCDEFGHI' for col in range(1, 10)]
        self.digits = "123456789"
        self.units = self.getUnits()
        self.peers = self.getPeers()
        self.values = self.getDict(grid)

    def getUnits(self):
        """
        Defines the 27 units (rows, columns, and 3x3 subgrids).
        Each unit is a list of variables.
        """
        units = []
        units += [[row + str(col) for col in range(1, 10)] for row in 'ABCDEFGHI']
        units += [[chr(65 + row) + str(col) for row in range(9)] for col in range(1, 10)]
        units += [[chr(65 + r) + str(c) for r in range(i, i+3) for c in range(j, j+3)]
                  for i in range(0, 9, 3) for j in range(1, 10, 3)]
        return units


    def getPeers(self):
        """
        Returns a dictionary mapping each variable to its peers (other variables in the same row, column, or 3x3 box).
        """
        peers = {var: set() for var in self.variables}
        for unit in self.units:
            for v in unit:
                peers[v] |= set(unit) - {v}
        return peers

    def getDict(self, grid=""):
        """
        Getting the string as input and returning the corresponding dictionary
        """
        i = 0
        values = dict()
        for cell in self.variables:
            if grid[i] != '0':
                values[cell] = grid[i]
            else:
                values[cell] = digits
            i = i + 1
        return values