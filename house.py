import random

class Town:
    def __init__(self, width, height, colors):
        self.LoL = []
        self.colors = colors
        self.width = width
        self.height = height

        row = []
        for x in range(width):
            for y in range(height):
                row.append(Home("WHITE", xy=(x, y)))
            self.LoL.append(row)
            row = []
    
    def __repr__(self):
        return str(self.LoL)

    def randomFill(self, emptyPercent = 20):

        for x in range(self.width):
            for y in range(self.height):
                #RANDOMLY ASSIGN COLOR OR EMPTY TO HOME 
                self.LoL[x][y].setColor(random.choices(self.colors)[0])
                self.LoL[x][y].makeFull()

                if random.randint(0,100) <= emptyPercent:
                    print("Made Empty")
                    self.LoL[x][y].makeEmpty()
        



class Home:
    def __init__(self, color, full=False, xy=(-1,-1)):
        self.color = color
        self.full = full
        self.xy = xy
    
    def __repr__(self):
        if self.full: 
            return self.color
        else:
            return "EMPTY"
        
    
    #Getters and setters
    def getColor(self):
        return self.color
    
    def isFull(self):
        return self.full
    
    def getPos(self):
        return self.xy

    def setColor(self, color):
        self.color = color
    
    def makeFull(self):
        self.full = True
    
    def makeEmpty(self):
        self.full = False




def main():
    WIDTH = 10
    HEIGHT = 10

    newTown = Town(WIDTH, HEIGHT, ["RED", "BLUE"])
    newTown.randomFill()
    print(newTown)

main()