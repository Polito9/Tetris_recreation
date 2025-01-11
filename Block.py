import FiguresTetris as fg
import Colors

class Block:
    type_ = 'O'
    pos_x = 0
    pos_y = 0
    max_pos_x = 0
    max_pos_y = 0
    min_pos_y = 0
    min_pos_y = 0
    size = 0
    rotation = 0
    color = Colors.WHITE
    in_ground = False
    freezed = False

    def __init__(self, type_, pos_x, pos_y, min_pos_x, max_pos_x, min_pos_y, max_pos_y, size):
        self.type_ = type_
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_pos_x = max_pos_x
        self.min_pos_x = min_pos_x
        self.max_pos_y = max_pos_y
        self.min_pos_y = min_pos_y
        self.size = size
        self.color = Colors.REFERENCE[type_] #References the color according to the type of piece

    def setRotation(self, rotation):
        if(not self.freezed):
            if(rotation>=4):
                self.rotation = 0
            else:
                self.rotation = rotation
            
            self.setPos_x(self.pos_x)
            self.setPos_y(self.pos_y)

            self.in_ground = False
            

    #Detection of exit of the grid 
    def setPos_x(self, pos_x):
        if(not self.freezed):
            right_part = 0
            down_part = 0
            #Simulating the borders of the figure
            fig = fg.FiguresTetris()
            pos = fig.getPositions(self.type_, self.size, pos_x, self.pos_y, self.rotation)
            for p in pos:
                right_part = max([right_part, p[0]+p[2]])
                down_part = max([down_part, p[1]+p[2]])

            #Checking if the figure will exceed the allowed dimensions
            if(pos_x < self.min_pos_x):
                self.pos_x = self.min_pos_x
                #print("It touched the left")
            elif(right_part > self.max_pos_x):
                self.pos_x = self.max_pos_x - (right_part-pos_x)
                #print("It touched the right")
            else:
                self.pos_x = pos_x
            
            self.in_ground = False
    
    def setPos_y(self, pos_y):
        if(not self.freezed):
            down_part = 0
            
            #Simulating the borders of the figure
            fig = fg.FiguresTetris()
            pos = fig.getPositions(self.type_, self.size, self.pos_x, pos_y, self.rotation)
            for p in pos:
                down_part = max([down_part, p[1]+p[2]])
            
            #print("DOWN PART: ", down_part)
            #print("POS_X: ", pos_y)

            #Checing if the figure will exceed the allowed dimensions
            if(down_part>=self.max_pos_y):
                self.pos_y = self.max_pos_y - (down_part -pos_y)
                self.in_ground = True
            else:
                self.pos_y = pos_y
                self.in_ground = False