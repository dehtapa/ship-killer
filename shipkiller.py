from tkinter import *
import random
import time
import math


class Main:
  def __init__(self, ships):
    self.numberOfShips = ships
    self.winner = 0
    self.start_game()
    self.end_game()

  def start_game(self):
    self.window = Window(900, 400)
    self.currentPlayer = 1
    self.gameStatus = 1
    self.gameRound = 0
    self.table = {}
    self.rows = 10
    table1 = self.draw_table(1, self.rows, 0, 0)
    table2 = self.draw_table(2, self.rows, 0, 40)
    self.player = {
      1: Player(1, 'Player1', table1, False, self.numberOfShips, self.rows),
      2: Player(2, 'Player2', table2, True, self.numberOfShips, self.rows)
    }
    self.message = StringVar(value="%s is placing her/his ships. " % self.player[self.currentPlayer].name)
    self.message2 = StringVar(value=self.player[self.currentPlayer].get_ship_message()[0])
    self.message3 = StringVar(value=self.player[self.currentPlayer].get_ship_message()[1])
    self.message4 = StringVar(value=self.player[self.currentPlayer].get_ship_message()[2])
    self.message5 = StringVar(value=self.player[self.currentPlayer].get_ship_message()[3])
    self.message6 = StringVar(value="")
    self.message7 = StringVar(value="")
    Label(self.window.root, textvariable=self.message, fg="blue", font=("Helvetica", 16)).grid(row=0, column=20)
    Label(self.window.root, textvariable=self.message2).grid(row=2, column=20)
    Label(self.window.root, textvariable=self.message3, fg="blue", font=("Helvetica", 12)).grid(row=3, column=20)
    Label(self.window.root, textvariable=self.message4).grid(row=4, column=20)
    Label(self.window.root, textvariable=self.message5, fg="blue", font=("Helvetica", 12)).grid(row=5, column=20)
    Label(self.window.root, textvariable=self.message6).grid(row=6, column=20)
    Label(self.window.root, textvariable=self.message7, fg="red", font=("Helvetica", 16)).grid(row=7, column=20)

    self.button1 = Button(self.window.root, text="Create ships automatically", command=self.player[1].auto_fill)
    self.button1.grid(row=9, column=20)
    self.button2 = Button(self.window.root, text="Clear ships", command=self.clear_ships)
    self.button2.grid(row=11, column=20)
    self.button3 = Button(self.window.root, text="Cheat", command=self.cheatActivate)
    self.button3.grid(row=13, column=20)

    #def auto_fill(self):
    #self.buttonFired(self.currentPlayer, 4,4)
    #self.buttonFired(self.currentPlayer, 5,3)
    #self.buttonFired(self.currentPlayer, 6,6)    

  def clear_ships(self):
    table = self.draw_table(1, self.rows, 0, 0)
    self.player[self.currentPlayer] = Player(self.currentPlayer, 'player1', table, False, self.numberOfShips, self.rows)
  
  def draw_table(self, id, side, shiftX, shiftY):
    table = {}
    for x in range(1,side +1):
      table[x] = {}
      for y in range(1,side+1):
        table[x][y] = Button(master=self.window.root, bg="azure2", command=lambda row=x, column=y: self.buttonFired(id, row,column))
        table[x][y].grid(row=shiftX +y,column=shiftY + x)
    return table
  
  def end_game(self):
    self.window.root.mainloop()

  def shut(self):    
    row= random.randint(1, self.rows)
    column= random.randint(1, self.rows)
    self.buttonFired(self.currentPlayer, row, column)
  
  def cheatActivate(self):    
    for x in range(1,10):
      for y in range(1,10):
        target = self.player[2].shipCoordinates.matrix[x][y]
        if str(target).isdigit() is True:
          self.player[2].table[x][y]["bg"] = "blue"

  def start_battle(self):
    self.button1.destroy()
    self.button2.destroy()
    self.gameStatus = 2
    self.currentPlayer = 2
    self.message.set('Let the Battle begin!')
    self.message2.set('%s has ships (destroyed/all:)' % self.player[1].name)
    self.message3.set('%s/%s' % (0, self.numberOfShips))
    self.message4.set('%s has ships (destroyed/all:)' % self.player[2].name)
    self.message5.set('%s/%s' % (0, self.numberOfShips))
    self.window.root.after(1000, lambda: self.message.set('Player1 is shooting'))  

  def buttonFired(self, id, row, column):
    if id == self.currentPlayer:
      if self.gameStatus == 2:
        message = self.player[self.currentPlayer].get_shot(row, column)
  
        self.message7.set(message)
        robot = self.player[self.currentPlayer].robot
        self.message.set('%s is shooting' % self.player[self.currentPlayer].name)
        self.message3.set('%s/%s' % (self.player[1].destroyedShips, self.numberOfShips))
        self.message5.set('%s/%s' % (self.player[2].destroyedShips, self.numberOfShips))
        if self.player[2].destroyedShips == self.numberOfShips:
          self.winner = 1
          self.message.set('%s won the game!!!' % self.player[1].name)
        if self.player[1].destroyedShips == self.numberOfShips:
          self.winner = 2
          self.message.set('%s won the game!!!' % self.player[2].name)
        if self.currentPlayer == 1:
            self.currentPlayer = 2
        else:
          self.currentPlayer = 1
        self.message6.set('%s fired x: %s, y:%s' % (self.player[self.currentPlayer].name, row, column))
        if robot == True and self.winner == 0:
          self.window.root.after(500, lambda: self.shut())         
      
      if self.gameStatus == 1:
        newMessage = self.player[id].place_ships(row, column)
        if newMessage == 'next':
          if self.currentPlayer == 1:
            self.currentPlayer = 2
            self.message.set('Player2 please place your ships')
            if self.player[self.currentPlayer].robot == True:
              self.player[2].auto_fill()
              self.start_battle()
            else:
              self.message2.set(newMessage[0])
              self.message3.set(newMessage[1])
              self.message4.set(newMessage[2])
              self.message5.set(newMessage[3])
          else:
            self.start_battle()

        else:
          self.message2.set(newMessage[0])
          self.message3.set(newMessage[1])
          self.message4.set(newMessage[2])
          self.message5.set(newMessage[3])
  
class Window:
  def __init__(self, x, y):
    self.root = Tk()
    self.root.title("Shipkiller")
    self.root.geometry("%sx%s" % (x,y))

class Player:
  def __init__(self, id, name, table, robot,numberOfShips, rows):
    self.maxNumberOfShips = numberOfShips
    self.rows = rows
    self.ships = {}
    self.currentShip = numberOfShips
    self.shipCoordinates = Table(rows)
    self.shots = Table(rows)
    self.id = id
    self.name = name
    self.table = table
    self.robot = robot
    self.score = 0
    self.wins = 0
    self.build_ships()
    self.destroyedShips = 0

  def build_ships(self):
    for x in range(1,self.maxNumberOfShips +1):
      self.ships[x] = Ship(x)

  def get_shot(self,row, column):
    target = self.shipCoordinates.matrix[row][column]
    message = ''
    if str(target).isdigit() is True:
      self.table[row][column]["bg"] ="red"
      self.ships[target].destroy()
      if self.ships[target].isDestroyed():
        self.destroyedShips += 1
        return 'Talált!!! Süllyedt!!!'
      return 'Talált!!!!!!!'
    else:
      self.table[row][column]["bg"] ="grey"
      return 'Nem talált!'

  def place_ships(self, row, column):
    if self.check_field_valid():
      self.shipCoordinates.update_matrix( row, column, self.currentShip)
      print('placing ships')
      if self.id is 1:
        self.table[row][column]["bg"] = "green"
      self.ships[self.currentShip].build()
      if self.ships[self.currentShip].isBuilt() == True:
        self.currentShip -= 1
      if self.currentShip <= 0:
        return 'next'
      else:
        return self.get_ship_message()

  def get_ship_message(self):
    #print('get message')
    #print(self.ships[self.currentShip].toBuild())
    contain = self.currentShip
    more = self.ships[self.currentShip].toBuild()
    return [
      'Number of blocks your ship must contains:',
      contain,
      'Remaining blocks you must place:',
      more
    ]
 
  def auto_fill(self):
    size = self.maxNumberOfShips
    for i in range(size):
      shipAlignment = random.randint(1,2)    #horizontal = 1, veritcal = 2
      row = random.randint(1,9)
      column = random.randint(1,9)
      if shipAlignment is 1:
        while row+size > 10 or not self.ifAvailable(row,column,size,shipAlignment):  #if out of bonds OR places are taken
          row = random.randint(1,9)
          column = random.randint(1,9)      
        for j in range(0,size):
          self.place_ships(row+j,column)  #use this method to place them next to eachoter - it makes them as one ship 
      else:
        while column+size > 10 or not self.ifAvailable(row,column,size,shipAlignment):  #if out of bonds OR places are taken
          row = random.randint(1,9)
          column = random.randint(1,9)      
        for j in range(0,size):
          self.place_ships(row,column+j)
      size -= 1

  def ifAvailable(self,row,column,size,alignment):
    #alignment; horizontal = 1, veritcal = 2
    available = False
    for i in range(0,size+1):
      if alignment is 1:   #check horizontal
        if self.shipCoordinates.matrix[row+i][column] == '' :
          available = True
        else:
          available = False
      else:                  #check vertical
        if self.shipCoordinates.matrix[row][column+i] == '':
          available = True
        else:
          available = False
    return available
      
  def checkNeighbours(self,row,column):    #check surrounding blocks, return true if neighbours are empty
    # available = False
    # row_limit = 9
    # if row_limit > 0:
    #   column_limit = 9
    #   for x in range(max(0,row-1),min(row+1,row_limit)):
    #     for y in range(column-1,min(column+1,column_limit)):
    #       if x != row or y != column:
    #         if self.shipCoordinates.matrix[x][y] == '' :
    #           available = False
    #         else:
    #           available = True
    # return 
    pass

  def check_field_valid(self):
    print('validity check')
    return True

class Ship:
  def __init__(self, squares):
    self.squares =  squares
    self.built = 0
    self.destroyed = 0

  def isBuilt(self):
    if self.built >= self.squares:
      return True
    else:
      return False

  def toBuild(self):
    return self.squares - self.built

  def isDestroyed(self):
    if self.destroyed >= self.squares:
      return True
    else:
      return False

  def build(self):
    print('build')
    self.built += 1


  def destroy(self):
    self.destroyed += 1  

class Table():
  def __init__(self, side):
    self.side = side
    self.matrix = {}
    self.create_matrix()
  
  def create_matrix(self):
    for x in range(1,self.side + 1):
      self.matrix[x] = {}
      for y in range(1,self.side+1):
        self.matrix[x][y] = ''

  def update_matrix(self, row, column, value):
    self.matrix[row][column] = value


game = Main(4)