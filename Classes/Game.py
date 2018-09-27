import tkinter as tk
import playsound
from gtts import gTTS
import os
from Player import *
from Ship import *
from Table import *
from Window import *


class Game:
    turn = 1
    winner = 0
    window = None
    table1 = None
    table2 = None
    player1 = None
    player2 = None
    currentPlayer = 1
    gameStatus = 1
    gameRound = 0
    messages = {
        'score': ['Easy.', 'You just got lucky.'],
        'fault': ['I was aiming for the water anyway.', 'Haha, not even close.'],
        'ship': ['I\'ve just sank your ship. Are you even trying?', 'You sank my ship! How dare you?']
    }

    def __init__(self, root, numberOfShips, rows):
        self.root = root
        self.numberOfShips = numberOfShips
        self.rows = rows
        # Start process
        self.start_game()

    def gttsSay(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save("temp.mp3")
        playsound.playsound("temp.mp3")
        os.remove("temp.mp3")

    def start_game(self):
        self.window = Window(self)
        self.rows = 10
        table1 = self.draw_table(1, self.rows, 0, 0)
        table2 = self.draw_table(2, self.rows, 0, 40)
        self.player = {
            1: Player(self, 1, 'Player1', table1, False, self.numberOfShips, self.rows),
            2: Player(self, 2, 'Player2', table2, True, self.numberOfShips, self.rows)
        }
        self.window.message1.set("%s is placing her/his ships. " % self.player[self.currentPlayer].name)
        self.window.message2.set(self.player[self.currentPlayer].get_ship_message()[0])
        self.window.message3.set(self.player[self.currentPlayer].get_ship_message()[1])
        self.window.message4.set(self.player[self.currentPlayer].get_ship_message()[2])
        self.window.message5.set(value=self.player[self.currentPlayer].get_ship_message()[3])

        self.root.after(
            1200, lambda: self.gttsSay('Place your ships'))

        # def auto_fill(self):
        # self.buttonFired(self.currentPlayer, 4,4)
        # self.buttonFired(self.currentPlayer, 5,3)
        # self.buttonFired(self.currentPlayer, 6,6)

    def auto_fill_both(self):
        self.player[1].auto_fill()
        self.player[2].auto_fill()
        self.gameStatus = 3

    def clear_ships(self):
        table = self.draw_table(1, self.rows, 0, 0)
        self.player[self.currentPlayer] = Player(
            self.currentPlayer, 'player1', table, False, self.numberOfShips, self.rows)

    def draw_table(self, id, side, shiftX, shiftY):
        table = {}
        for x in range(1, side + 1):
            table[x] = {}
            for y in range(1, side + 1):
                table[x][y] = Button(
                    master=self.root,
                    bg="azure2",
                    command=lambda row=x,
                    column=y: self.buttonFired(
                        id,
                        row,
                        column))
                table[x][y].grid(row=shiftX + y, column=shiftY + x)
        return table

    def shut(self):
        # playsound.playsound('Cannon+5.wav', True)
        row = random.randint(1, self.rows)
        column = random.randint(1, self.rows)
        self.buttonFired(self.currentPlayer, row, column)

    def cheatActivate(self):
        for x in range(1, 10):
            for y in range(1, 10):
                target = self.player[2].shipCoordinates.matrix[x][y]
                if str(target).isdigit() is True:
                    self.player[2].table[x][y]["bg"] = "blue"

    def computerCheat(self):
        self.player[2].robot = False

    def start_battle(self):
        self.window.buttonCreateShips.destroy()
        self.window.buttonClearShips.destroy()
        self.window.buttonCheat.grid(row=9, column=20)
        self.window.buttonComputerCheat.grid(row=11, column=20)
        self.gameStatus = 2
        self.currentPlayer = 2
        self.window.message1.set('Let the Battle begin!')
        self.window.message2.set(
            '%s has ships (destroyed/all:)' %
            self.player[1].name)
        self.window.message3.set('%s/%s' % (0, self.numberOfShips))
        self.window.message4.set(
            '%s has ships (destroyed/all:)' %
            self.player[2].name)
        self.window.message5.set('%s/%s' % (0, self.numberOfShips))
        self.root.after(
            1000, lambda: self.window.message1.set('Player1 is shooting'))

    def buttonFired(self, id, row, column):
        if id == self.currentPlayer:
            if self.gameStatus == 2:
                self.window.run_animate(0)
                playsound.playsound(
                    '/home/toybox/codecool/python-projects/4th-TW-week/ship-killer/Sounds/Torpedo+Explosion.wav', True)
                # playsound.playsound('Torpedo+Explosion.wav', True)
                messageId = self.player[self.currentPlayer].get_shot(row, column)
                message = self.messages[messageId][self.currentPlayer - 1]
                if messageId == 'score' or messageId == 'ship':
                    playsound.playsound(
                        '/home/toybox/codecool/python-projects/4th-TW-week/ship-killer/Sounds/Explosion+9.wav', True)
                    # playsound.playsound('Explosion+9.wav', True)
                self.window.message7.set(message)
                self.gttsSay(message)

                robot = self.player[self.currentPlayer].robot

                self.window.message1.set('%s is shooting' %
                                         self.player[self.currentPlayer].name)
                self.window.message3.set(
                    '%s/%s' %
                    (self.player[1].destroyedShips, self.numberOfShips))
                self.window.message5.set(
                    '%s/%s' %
                    (self.player[2].destroyedShips, self.numberOfShips))
                if self.player[2].destroyedShips == self.numberOfShips:
                    self.winner = 1
                    self.window.message1.set(
                        '%s won the game!!!' %
                        self.player[1].name)
                    self.gttsSay('Nyertél, de csak mert hagytam magam!')
                if self.player[1].destroyedShips == self.numberOfShips:
                    self.winner = 2
                    self.window.message1.set(
                        '%s won the game!!!' %
                        self.player[2].name)
                    self.gttsSay('Ismét a jobbik győzött!')
                if self.currentPlayer == 1:
                    self.currentPlayer = 2
                else:
                    self.currentPlayer = 1
                self.window.message6.set('%s fired x: %s, y:%s' %
                                         (self.player[self.currentPlayer].name, row, column))
                if robot is True and self.winner == 0:
                    self.root.after(3000, lambda: self.shut())

            if self.gameStatus == 1:
                newMessage = self.player[id].place_ships(row, column)
                if newMessage == 'next':
                    if self.currentPlayer == 1:
                        self.currentPlayer = 2
                        self.window.message1.set('Player2 please place your ships')
                        if self.player[self.currentPlayer].robot is True:
                            self.player[2].auto_fill()
                            self.start_battle()
                        else:
                            self.window.message2.set(newMessage[0])
                            self.window.message3.set(newMessage[1])
                            self.window.message4.set(newMessage[2])
                            self.window.message5.set(newMessage[3])
                    else:
                        self.start_battle()

                else:
                    self.window.message2.set(newMessage[0])
                    self.window.message3.set(newMessage[1])
                    self.window.message4.set(newMessage[2])
                    self.window.message5.set(newMessage[3])


def main(numberOfShips, rows, width, height):  # run mianloop
    root = tk.Tk()
    root.geometry("%sx%s" % (width, height))
    app = Game(root, numberOfShips, rows)
    root.mainloop()


if __name__ == '__main__':
    main(4, 10, 1200, 900)
