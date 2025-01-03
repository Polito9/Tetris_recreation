class Block:
    type_ = 'O'
    pos_x = 0
    pos_y = 0
    left_part = 0
    down_part = 0
    right_part = 0
    max_pos_x = 0
    max_pos_y = 0
    size = 0
    
    def __init__(self, type_, pos_x, pos_y, max_pos_x, max_pos_y, size):
        self.type_ = type_
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_pos_x = max_pos_x
        self.max_pos_y = max_pos_y
        self.size = size
        if(type_ == 'O' or type_ == 'L' or type_ == 'T' or type_ == 'S'):
            self.left_part = size*2
        elif(type_ == 'I' or type_ == 'J' or type_ == 'Z'):
            self.left_part = size
    
    def setPos_x(self, pos_x):
        if(pos_x > self.max_pos_x-self.left_part):
            self.pos_x = self.max_pos_x-self.left_part
            print("It has leaved the zone")
        else:
            self.pos_x = pos_x
            print(pos_x)

    def setPos_y(self, pos_y):
        if(pos_y> self.max_pos_y):
            self.pos_y = self.max_pos_y
            print("It has leaved the zone")
        else:
            self.pos_y = pos_y