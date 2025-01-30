import FiguresTetris as fg
import math
import random as rd

class RandomFigures:
    figs = fg.FiguresTetris()
    def __init__(self):
        pass

    def initialize_queue(self, queue, size):
        
        for i in range(0, size):
            #Generating randomly the piece accordin to a uniform distribution
            queue[i] = self.figs.figsNames[math.floor(rd.uniform(0, 7))]
            if(i!=0):
                #Detecting if there is 2 consecutive repeated pieces
                while(queue[i-1] == queue[i]):
                    queue[i] = self.figs.figsNames[math.floor(rd.uniform(0, 7))]

    def generate_next_piece(self, queue, size):
        #Mcving the pieces one position in the queue
        for i in range(1, size):
            queue[i-1] = queue[i]
        #Generating the new piece in the last position
        queue[size-1] = self.figs.figsNames[math.floor(rd.uniform(0, 7))]
        #Detecting that the piece is no repeated, if it is, it generates again
        while(queue[size-1] == queue[size-2]):
            queue[size-1] = self.figs.figsNames[math.floor(rd.uniform(0, 7))]

        