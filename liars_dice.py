'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Katie Chiu
Liar's Dice Game
Version 1.0
Last updated 12 November 2018
Game that allows you to bet on the amount of dice among players. You can only see your own dice and bet or call based on what you see. Similar to poker but with dice not cards.
'''

from tkinter import *
from tkinter import ttk
import random


class App:
    def restart(self, event):  # leaves combobox blank
        event.widget.master.focus_set()

    def __init__(self):
        self.diceleft = 15
        self.players = 3
        self.bids = 0
        self.lastdiceval = 1
        self.lastamount = 0
        self.playercall = "You"
        self.lastplayer = 0
        self.p1dice = 5
        self.p2dice = 5
        self.userdice = 5

        self.content = Frame(root)

        self.dice = Label(self.content, text="Your dice")  # Shows user their dice
        self.all = Label(self.content, text="Dice 1 - \nDice 2 - \nDice 3 - \nDice 4 - \nDice 5 - ")

        self.left = Label(self.content, text="Dice left: " + str(self.diceleft))  # shows the amount of dice left
        self.playersleft = Label(self.content,
                                 text="Players left: " + str(self.players))  # shows amount of players left
        self.last = Label(self.content, text="Last Action:\n")
        self.others = Label(self.content, text="")

        self.choosevalue = StringVar()
        self.choosevalue.set("")
        self.box = ttk.Combobox(self.content, state=DISABLED, width=12,
                                textvariable=self.choosevalue)  # User can choose what to bet
        self.box["values"] = ["1", "2", "3", "4", "5", "6"]
        self.box.bind("<<ComboboxSelected>>")
        self.box.bind("<FocusIn>", self.restart)
        self.diceamount = Label(self.content, text="Dice value")

        self.roll = Button(self.content, text="Roll", width=6, command=self.play)  # allows user to roll the dice

        self.actions = Label(self.content, text="Actions")  # shows user each action in buttons
        self.exact = Button(self.content, text="Exact", width=6, state=DISABLED, command=self.userexact)
        self.call = Button(self.content, text="Call", width=6, state=DISABLED, command=self.usercall)

        self.bet = Button(self.content, width=6, text="Bet", state=DISABLED,
                          command=self.userbet)  # gives user options to bet
        self.spinval = StringVar()
        self.spinval.set("")
        self.num = ttk.Combobox(self.content, width=12, textvariable=self.spinval,
                           state=DISABLED)
        lists=[]
        for x in range(15):
            x=x+1
            lists.append(x)
        self.num["values"] = lists
        self.num.bind("<<ComboboxSelected>>")
        self.num.bind("<FocusIn>", self.restart)
        self.dicelabel = Label(self.content, text="Amount of dice")

        self.grip_frame = Frame(root)
        self.size = ttk.Sizegrip(self.grip_frame)

        self.menubar = Menu(root)  # menubar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)  # creates option in menubar
        self.filemenu.add_command(label="Restart", command=self.again)  # options in file
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar2 = Menu(root)  # 2nd menu for "help"
        self.helpmenu = Menu(self.menubar2, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)  # creates option in menubar
        self.helpmenu.add_command(label="About", command=self.about)  # option in help
        root.config(menu=self.menubar)
        self.gridall()

    def gridall(self):
        self.content.grid(column=0, row=0)  # grids all widgets
        self.actions.grid(column=5, row=5, padx=60)
        self.exact.grid(column=5, row=7)
        self.call.grid(column=5, row=9)
        self.roll.grid(column=5, row=11, pady=10)
        self.bet.grid(column=0, row=11, pady=10)
        self.num.grid(column=0, row=7)
        self.box.grid(column=0, row=9, sticky=S, pady=(27, 0))
        self.dice.grid(column=10, row=5)
        self.all.grid(column=10, row=7, rowspan=3)
        self.left.grid(column=0, row=13, sticky=W)
        self.playersleft.grid(column=0, row=15, sticky=W)
        self.last.grid(column=5, row=13, padx=20)
        self.others.grid(column=5, row=15)
        self.dicelabel.grid(column=0, row=5, sticky=S, pady=(15, 0))
        self.diceamount.grid(column=0, row=9, sticky=N, pady=(5, 0))

        self.size.grid(column=999, row=999, sticky=(NSEW))
        self.grip_frame.grid(column=999, row=999)

        root.columnconfigure(0, weight=1)  # weight for rows and columns
        root.rowconfigure(0, weight=1)
        root.minsize(400, 250)
        self.grip_frame.columnconfigure(999, weight=1)
        self.grip_frame.rowconfigure(999, weight=1)

    def play(self):
        self.lastamount = 0
        self.values = []  # randomly assigns numbers to dice
        self.p1 = []
        self.p2 = []
        self.bids = 0
        self.others.config(text="Everyone rolled")
        for x in range(int(self.userdice)):  # dice for user
            uservalue = random.randrange(1, 7)
            self.values.append(str(uservalue))
        if self.userdice == 5:
            self.all.config(
                text="Dice 1 - " + self.values[0] + "\nDice 2 - " + self.values[1] + "\nDice 3 - " + self.values[
                    2] + "\nDice 4 - " + self.values[3] + "\nDice 5 - " + self.values[4])
        elif self.userdice == 4:
            self.all.config(
                text="Dice 1 - " + self.values[0] + "\nDice 2 - " + self.values[1] + "\nDice 3 - " + self.values[
                    2] + "\nDice 4 - " + self.values[3])
        elif self.userdice == 3:
            self.all.config(
                text="Dice 1 - " + self.values[0] + "\nDice 2 - " + self.values[1] + "\nDice 3 - " + self.values[2])
        elif self.userdice == 2:
            self.all.config(text="Dice 1 - " + self.values[0] + "\nDice 2 - " + self.values[1])
        elif self.userdice == 1:
            self.all.config(text="Dice 1 - " + self.values[0])

        for y in range(int(self.p1dice)):  # dice for player 1
            p1 = random.randrange(1, 7)
            self.p1.append(str(p1))

        for z in range(int(self.p2dice)):  # dice for player 2
            p2 = random.randrange(1, 7)
            self.p2.append(str(p2))
        self.roll.config(state=DISABLED)

        print(self.p1)
        print(self.p2)

        if self.lastplayer == 0:
            root.after(3000, self.p1action)
        elif self.lastplayer == 1:
            root.after(3000, self.p2action)
        elif self.lastplayer == 2:
            if self.playercall == "Player 2":
                root.after(3000, self.others.config(text="Your turn"))
                self.bet.config(state=NORMAL)
                self.box.config(state="readonly")
                self.num.config(state="readonly")
            else:
                self.exact.config(state=DISABLED)
                self.call.config(state=DISABLED)
                self.others.config(text="Your turn")
                self.bet.config(state=NORMAL)
                self.box.config(state="readonly")
                self.num.config(state="readonly")

    def p1action(self):
        self.exact.config(state=DISABLED)
        self.call.config(state=DISABLED)
        self.others.config(state=DISABLED)
        self.bet.config(state=DISABLED)
        self.box.config(state=DISABLED)
        self.num.config(state=DISABLED)
        self.others.config(text="")
        if self.p1dice<=0 and self.p2dice<=0:
            self.wins()
        elif self.p1dice == -1:
            self.p2action()
        else:
            if self.lastplayer == 0:
                if self.bids == 0:
                    self.action1 = 1
                elif int(self.lastamount) == int(self.diceleft):
                    self.action1 = random.randrange(2, 4)
                else:
                    self.action1 = random.randrange(1, 4)

                if self.action1 == 1:
                    diceval1 = random.randrange(int(self.lastdiceval), 7)
                    if int(self.lastamount) == int(self.diceleft):
                        amount1 = random.randrange(int(self.lastamount), int(self.diceleft))
                    else:
                        amount1 = random.randrange((int(self.lastamount) + 1), (int(self.diceleft) + 1))
                    if amount1 == 1:
                        self.last.config(text="Last Action:\nPlayer 1 bid " + str(amount1) + " " + str(diceval1))
                    else:
                        self.last.config(text="Last Action:\nPlayer 1 bid " + str(amount1) + " " + str(diceval1) + "'s")
                    self.lastdiceval = diceval1
                    self.lastamount = amount1
                    self.bids = 1
                    self.playercall = "Player 1"
                    self.lastplayer = 1
                    root.after(3000, self.p2action)
                elif self.action1 == 2:
                    self.last.config(text="Last Action:\nPlayer 1 called")
                    self.bids = 0
                    self.lastplayer = 1
                    self.lastamount = 0
                    root.after(3000, self.calls)
                else:
                    self.last.config(text="Last Action:\nPlayer 1 called exact")
                    self.bids = 0
                    self.lastplayer = 1
                    self.lastamount = 0
                    root.after(3000, self.playerexact)
            elif self.lastplayer == 1:
                self.p2action()
            else:
                self.others.config(text="Your turn")
                self.bet.config(state=NORMAL)
                self.box.config(state="readonly")
                self.num.config(state="readonly")
                if self.bids==1:
                    self.exact.config(NORMAL)
                    self.call.config(NORMAL)

    def p2action(self):
        self.exact.config(state=DISABLED)
        self.call.config(state=DISABLED)
        self.others.config(state=DISABLED)
        self.bet.config(state=DISABLED)
        self.box.config(state=DISABLED)
        self.num.config(state=DISABLED)
        self.others.config(text="")
        if self.p2dice<=0 and self.p1dice<=0:
            self.wins()
        elif self.p2dice == -1:
            self.others.config(text="Your turn")
            self.bet.config(state=NORMAL)
            self.box.config(state="readonly")
            self.num.config(state="readonly")
            if self.bids==1:
                self.exact.config(state=NORMAL)
                self.call.config(state=NORMAL)
                self.bet.config(state=NORMAL)
        else:
            if self.lastplayer == 1:
                if self.bids == 0:
                    self.action2 = 1
                elif int(self.lastamount) == int(self.diceleft):
                    self.action2 = random.randrange(2, 4)
                else:
                    self.action2 = random.randrange(1, 4)

                if self.action2 == 1:
                    diceval2 = random.randrange(int(self.lastdiceval), 7)
                    if int(self.lastamount) == int(self.diceleft):
                        amount2 = random.randrange(int(self.lastamount), int(self.diceleft))
                    else:
                        amount2 = random.randrange((int(self.lastamount) + 1), (int(self.diceleft) + 1))
                    if amount2 == 1:
                        self.last.config(text="Last Action:\nPlayer 2 bid " + str(amount2) + " " + str(diceval2))
                    else:
                        self.last.config(text="Last Action:\nPlayer 2 bid " + str(amount2) + " " + str(diceval2) + "'s")
                    self.lastdiceval = diceval2
                    self.lastamount = amount2
                    self.bids = 1
                    self.playercall = "Player 2"
                    self.lastplayer = 2
                    self.others.config(text="Your turn")
                    self.bet.config(state=NORMAL)
                    self.box.config(state=NORMAL)
                    self.num.config(state=NORMAL)
                    if amount2!=15 and diceval2!=6:
                        self.bet.config(state=NORMAL)
                        self.box.config(state="readonly")
                        self.num.config(state="readonly")
                elif self.action2 == 2:
                    self.last.config(text="Last Action:\nPlayer 2 called")
                    self.bids = 0
                    self.lastplayer = 2
                    self.lastamount = 0
                    root.after(3000, self.calls)
                else:
                    self.last.config(text="Last Action:\nPlayer 2 called exact")
                    self.bids = 0
                    self.lastplayer = 2
                    self.lastamount = 0
                    root.after(3000, self.playerexact)
                if self.bids == 1:
                    self.exact.config(state=NORMAL)  # only leaves actions as normal
                    self.call.config(state=NORMAL)
            elif self.lastplayer == 0 and self.p1dice!=-1:
                self.p1action()

    def usercall(self):
        self.others.config(text="")
        self.lastplayer=0
        find = self.values.count(str(self.lastdiceval))
        find1 = self.p1.count(str(self.lastdiceval))
        find2 = self.p2.count(str(self.lastdiceval))
        total = find + find1 + find2
        print(total)
        self.bids = 0
        if total >= self.lastamount:
            self.last.config(text=str(self.playercall) + " lost a dice")
            self.diceleft = self.diceleft - 1
            self.left.config(text="Dice left: " + str(self.diceleft))
            self.lastplayer=0
            self.last.config(text="You lost a dice")
            self.userdice = (int(self.userdice) - int(1))
        else:
            self.last.config(text=str(self.playercall) + " lost a dice")
            self.diceleft = (int(self.diceleft) - int(1))
            if self.playercall == "Player 1":
                self.p1dice = (int(self.p1dice) - int(1))
            elif self.playercall == "Player 2":
                self.p2dice = (int(self.p2dice) - int(1))

        lists=[]
        for x in range(self.diceleft):
            x=x+1
            lists.append(x)
        self.num["values"]=lists

        if self.p1dice == 0 and self.p2dice == 0:
            self.wins()
        elif self.p1dice == 0:
            self.players=(int(self.players)-int(1))
            self.p1dice=-1
            root.after(2000, self.last.config(text="Player 1 has no more dice"))
        elif self.p2dice == 0:
            self.p2dice=-1
            self.players=(int(self.players)-int(1))
            root.after(2000, self.last.config(text="Player 2 has no more dice"))
        elif self.userdice == 0:
            root.after(2000, self.last.config(text="You lost all your dice"))
            self.lost()

        self.lastamount = 0
        self.box.config(state=DISABLED)
        self.num.config(state=DISABLED)
        self.call.config(state=DISABLED)
        self.exact.config(state=DISABLED)
        self.bet.config(state=DISABLED)
        self.left.config(text="Dice left: " + str(self.diceleft))
        self.playersleft.config(text="Players left: "+str(self.players))
        root.after(3000, self.play)

    def betwrong(self):
        self.box.config(state=NORMAL)
        self.num.config(state=NORMAL)
        self.bet.config(state=NORMAL)
        self.others.config(text="Error\nNeed input")
        
    def userbet(self):
        self.box.config(state=DISABLED)
        self.num.config(state=DISABLED)
        self.bet.config(state=DISABLED)
        self.others.config(text="")
        self.useramount = (self.spinval.get())
        self.userdiceval = (self.choosevalue.get())
        lists=[self.useramount,self.userdiceval]
        print(lists)
        if str(self.useramount)=="" or str(self.userdiceval)=="":
            self.betwrong()
        elif (str(self.useramount) <= str(self.lastamount)) and (str(self.userdiceval) <= str(self.lastdiceval)):
            self.box.config(state=NORMAL)
            self.num.config(state=NORMAL)
            self.bet.config(state=NORMAL)
            self.others.config(text="Error\nNeed a higher value")
            self.choosevalue.set("")
            self.spinval.set("")
        else:
            if self.useramount == "1":
                self.last.config(text="You bet " + str(self.useramount) + " " + str(self.userdiceval))
                self.lastdiceval = self.userdiceval
                self.lastamount = self.useramount
                self.bids = 1
                self.playercall = "You"
                self.lastplayer = 0
                self.choosevalue.set("")
                self.spinval.set("")
                root.after(3000, self.p1action)
            else:
                self.last.config(text="You bet " + str(self.useramount) + " " + str(self.userdiceval) + "'s")
                self.lastdiceval = self.userdiceval
                self.lastamount = self.useramount
                self.bids = 1
                self.playercall = "You"
                self.lastplayer = 0
                self.choosevalue.set("")
                self.spinval.set("")
                root.after(3000, self.p1action)

    def userexact(self):
        self.lastplayer = 0
        self.playerexact()

    def playerexact(self):
        self.others.config(text="")
        self.bids = 0
        find = self.values.count(str(self.lastdiceval))
        find1 = self.p1.count(str(self.lastdiceval))
        find2 = self.p2.count(str(self.lastdiceval))
        total = find + find1 + find2
        if total == self.lastamount:
            self.last.config(text=str(self.playercall) + " lost a dice")
            self.diceleft = (int(self.diceleft) - int(1))
            if self.playercall == "Player 1":
                self.p1dice = (int(self.p1dice) - int(1))
            elif self.playercall == "Player 2":
                self.p2dice = (int(self.p2dice) - int(1))
            elif self.playercall == "You":
                self.userdice = (int(self.userdice) - int(1))
        else:
            if self.lastplayer == 0:
                self.last.config(text="You lost a dice")
                self.userdice = (int(self.userdice) - 1)
            else:
                self.last.config(text="Player " + str(self.lastplayer) + " lost a dice")
            self.diceleft = (int(self.diceleft) - int(1))
            if self.lastplayer == 1:
                self.p1dice = (int(self.p1dice) - int(1))
            elif self.lastplayer == 2:
                self.p2dice = (int(self.p2dice) - int(1))

        lists=[]
        for x in range(self.diceleft):
            x=x+1
            lists.append(x)
        self.num["values"]=lists

        if self.p1dice==0 and self.p2dice==0:
            self.wins()
        elif self.p1dice == 0:
            self.players=(int(self.players)-int(1))
            self.p1dice=-1
            root.after(2000, self.last.config(text="Player 1 has no more dice"))
        elif self.p2dice == 0:
            self.p2dice=-1
            self.players=(int(self.players)-int(1))
            root.after(2000, self.last.config(text="Player 2 has no more dice"))
        elif self.userdice == 0:
            root.after(2000, self.last.config(text="You lost all your dice"))
            self.lost()
        self.lastamount = 0
        self.box.config(state=DISABLED)
        self.num.config(state=DISABLED)
        self.call.config(state=DISABLED)
        self.exact.config(state=DISABLED)
        self.bet.config(state=DISABLED)
        self.left.config(text="Dice left: " + str(self.diceleft))
        self.playersleft.config(text="Players left: "+str(self.players))
        root.after(3000, self.play)

    def calls(self):
        find = self.values.count(str(self.lastdiceval))
        find1 = self.p1.count(str(self.lastdiceval))
        find2 = self.p2.count(str(self.lastdiceval))
        total = find + find1 + find2
        print(total)
        self.bids = 0
        if total <= self.lastamount:
            if self.lastplayer == 0:
                self.last.config(text="You lost a dice")
                self.userdice = (int(self.userdice) - int(1))
            else:
                self.last.config(text="Player " + str(self.lastplayer) + " lost a dice")
            self.diceleft = (int(self.diceleft) - int(1))
            if self.lastplayer == 1:
                self.p1dice = (int(self.p1dice) - int(1))
            elif str(self.lastplayer) == "2":
                self.p2dice = (int(self.p2dice) - int(1))
        else:
            self.last.config(text=str(self.playercall) + " lost a dice")
            self.diceleft = (int(self.diceleft) - int(1))
            if self.playercall == "Player 1":
                self.p1dice = (int(self.p1dice) - int(1))
            elif self.playercall == "Player 2":
                self.p2dice = (int(self.p2dice) - int(1))
            elif self.playercall == "You":
                self.userdice = (int(self.userdice) - int(1))

        lists=[]
        for x in range(self.diceleft):
            x=x+1
            lists.append(x)
        self.num["values"]=lists

        if self.p1dice == 0 and self.p2dice == 0:
            self.wins()
        elif self.p1dice == 0:
            self.players=(int(self.players)-int(1))
            self.p1dice=-1
            root.after(2000, self.last.config(text="Player 1 has no more dice"))
        elif self.p2dice == 0:
            self.p2dice=-1
            self.players=(int(self.players)-int(1))
            root.after(2000, self.last.config(text="Player 2 has no more dice"))
        elif self.userdice == 0:
            root.after(2000, self.last.config(text="You lost all your dice"))
            self.lost()

        self.lastamount = 0
        self.box.config(state=DISABLED)
        self.num.config(state=DISABLED)
        self.call.config(state=DISABLED)
        self.exact.config(state=DISABLED)
        self.bet.config(state=DISABLED)
        self.left.config(text="Dice left: " + str(self.diceleft))
        self.playersleft.config(text="Players left: "+str(self.players))
        root.after(3000, self.play)

    def lost(self):
        self.top2 = Toplevel(root, padx=15, pady=15)
        self.top2.title("You lost!")
        label = Label(self.top2, text="You have lost the game!")
        label.pack()
        button1=Button(self.top2,text="Play Again",command=self.combine2)
        button1.pack()
        button = Button(self.top2, text="Close", command=root.destroy)
        button.pack()
        self.top2.geometry("215x110")
        self.top2.resizable(width=False, height=False)

    def wins(self):
        self.top = Toplevel(root, padx=15, pady=15)
        self.top.title("You win!")
        label = Label(self.top, text="You have won the game!")
        label.pack()
        button1=Button(self.top,text="Play Again",command=self.combine)
        button1.pack()
        button = Button(self.top, text="Close", command=root.destroy)
        button.pack()
        self.top.geometry("215x110")
        self.top.resizable(width=False, height=False)

    def combine(self):
        self.top.destroy()
        App()

    def combine2(self):
        self.top2.destroy()
        App()

    def again(self):
        App()

    def about(self):
        top = Toplevel(root)
        top.title("How to Play")
        label = Label(top,
                      text="How to Play\n\nBids - Each player has 5 dice.  You can see your own dice but not each other's.\nEach player bids the amount of dice a single face value has.\nEach bid must be higher than the previous one in number or face value.\nEx: Five 2's --> Six 2's OR Five 3's\n\nCall - You may only challenge the bid given from the previous player.\nIf the bid is equal to or less than the actual amount,\nthe challenger loses and the bidder wins.\nBut if they bid more than the actual amount, the bidder lose.\n\nExact - You may only call exact on the bid given from the previous player.\nIf there is exactly what was bid, the challenger wins.\nIf there is not, the bidder wins and the challenger loses.\n\nWhoever loses each call or exact loses a dice\n\nObjective: Be the last player with dice\n")
        label.pack()
        button = Button(top, text="Close", command=top.destroy)
        button.pack()
        top.geometry("500x350")
        top.resizable(width=False, height=False)


root = Tk()
app = App()
root.title("Liar's Dice")
root.mainloop()
root.destroy()
