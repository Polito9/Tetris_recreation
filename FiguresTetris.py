class FiguresTetris:
    def __init__(self):
        pass
    
    def getPositions(self, type_, size, start_x, start_y):
        # Returns a list of list of size 4 that are the coordinates of start of the figure to draw and the size
        # This list can be used directly into the draw.rect function of pygame
        positions = []

        if(type_ == 'I'):
            pos = [start_x, start_y, size, size]
            positions.append(pos.copy())
            for i in range(3):
                pos[1]+=size
                positions.append(pos.copy())
        
        elif(type_ == 'J' or type_ == 'L'):
            pos = [start_x, start_y, size, size]
            positions.append(pos.copy())
            for i in range(2):
                pos[1]+=size
                positions.append(pos.copy())

            if(type_ == 'L'):
                pos = [start_x+size, pos[1], size, size]
            else:
                pos = [start_x-size, pos[1], size, size]
            positions.append(pos.copy())

        elif(type_ == 'Z'):
            pos = [start_x, start_y, size, size]
            positions.append(pos.copy())
            pos = [start_x+size, start_y, size, size]
            positions.append(pos.copy())
            pos = [pos[0], start_y+size, size, size]
            positions.append(pos.copy())
            pos = [pos[0]+size, pos[1], size, size]
            positions.append(pos.copy())
        elif(type_ == 'S'):
            pos = [start_x, start_y, size, size]
            positions.append(pos.copy())
            pos = [start_x+size, start_y, size, size]
            positions.append(pos.copy())
            pos = [start_x, start_y+size, size, size]
            positions.append(pos.copy())
            pos = [start_x-size, start_y+size, size, size]
            positions.append(pos.copy())
        elif(type_ == 'T'):
            pos = [start_x, start_y, size, size]
            positions.append(pos.copy())
            pos = [start_x, start_y+size, size, size]
            positions.append(pos.copy())
            pos = [start_x-size, start_y+size, size, size]
            positions.append(pos.copy())
            pos = [start_x+size, start_y+size, size, size]
            positions.append(pos.copy())
        elif(type_ == 'O'):
            pos = [start_x, start_y, size, size]
            positions.append(pos.copy())
            pos = [start_x+size, start_y+size, size, size]
            positions.append(pos.copy())
            pos = [start_x, start_y+size, size, size]
            positions.append(pos.copy())
            pos = [start_x+size, start_y, size, size]
            positions.append(pos.copy())
        else:
            try:
                1/0
            except:
                print()
                print("Oh no, an error ocurred!")
                print("Detail: No valid figure type to draw")
                exit(1)
                
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