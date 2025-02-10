class FiguresTetris:
    directions = {}
    figsNames = ['O', 'I', 'J', 'L', 'S', 'T', 'Z']
    matrix = []
    def __init__(self):        
        for name in self.figsNames:
            self.directions[name] = "figures\\" + name +".txt"
    
    def getMatrixFromFile(self, type_):
        file = open(self.directions[type_])
        self.matrix = []
        for line in file:#Every line
            self.matrix.append(line)
        
        file.close()


    def getPositions(self, type_, size, start_x, start_y, rotation):
        # Returns a list of lists with size 4 that are the coordinates of start of the figure to draw and the size
        # This list can be used directly into the draw.rect function of pygame
        positions = []
        self.getMatrixFromFile(type_)
        #Reading the file and asigning where the rectangles are going to be drawn
        pos = [start_x, start_y, size, size]
        
        #Managing the rotation of the piece by changing how the matrix of the file is readed
        r = (len(self.matrix))
        c = (len(self.matrix[0]))-1 #Because it detects another character in every line
        #print(r, c)
        
        #The indicators of where to begin and end the loops
        begin_i, end_i = 0, 0
        begin_j, end_j = 0, 0
        increase_i = 1
        increase_j = 1

        if(rotation == 0):
            begin_i = 0
            end_i = r
            begin_j = 0
            end_j = c
        elif(rotation == 2):
            begin_i = r-1
            end_i = -1
            begin_j = c-1
            end_j = -1
            increase_i = -1
            increase_j = -1
        elif(rotation == 1):
            begin_i = 0
            end_i = c
            begin_j = r-1
            end_j = -1
            increase_j = -1
        elif(rotation == 3):
            begin_i = c-1
            end_i = -1
            increase_i = -1
            begin_j = 0
            end_j = r
        
        valid = False
        for i in range(begin_i, end_i, increase_i):
            pos[0] = start_x

            for j in range(begin_j, end_j, increase_j):
                #Changing how the matrix is read according to the orientation
                if(rotation == 0 or rotation == 2):                        
                    valid = self.matrix[i][j] == '*'
                else:
                    valid = self.matrix[j][i] == '*'

                if(valid):
                    positions.append(pos.copy())

                pos[0]+=size

            pos[1]+=size

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