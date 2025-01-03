class FiguresTetris:
    directions = {}

    def __init__(self):
        figsNames = ['O', 'I', 'J', 'L', 'S', 'T', 'Z']
        
        for name in figsNames:
            self.directions[name] = "figures\\" + name +".txt"
    
    def getPositions(self, type_, size, start_x, start_y):
        # Returns a list of lists with size 4 that are the coordinates of start of the figure to draw and the size
        # This list can be used directly into the draw.rect function of pygame
        positions = []
        file = open(self.directions[type_])

        #Reading the file and asigning where the rectangles are going to be drawn
        pos = [start_x, start_y, size, size]
        for line in file:#Every line
            pos[0] = start_x

            for c in line:#Every character in the line
                if (c == '*'):
                    positions.append(pos.copy())
                pos[0]+=size

            pos[1]+=size
        
        file.close()
        
        return positions

    def getPositionsMesh(self, size, width, height, start_x, start_y):
        #This works to draw a mesh of an specified size starting on certaing point
        #Returns a list of tuples, each tuple has two elements, the initial positon and the end position of the rects
        positions = []
        for i in range(start_y, start_y+height+(size), size):
            s = (start_x, i)
            e = (start_x+width, i)
            positions.append((s, e))

        for i in range(start_x, start_x+width+(size), size):
            s = (i, start_y)
            e = (i, start_y+height)
            positions.append((s, e))
        
        return positions