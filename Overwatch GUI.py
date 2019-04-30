import tkinter as tk
from PIL import Image, ImageTk
from charlist import *
import itertools


class OverwatchGUI:

    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Overwatch GUI")

        self.titleLabel = tk.Label(self.mainWin, text="Overwatch Team Picker", font="10", height=5, relief="sunken")
        self.titleLabel.grid(row=0, column=6)

        self.enemyLabel1 = tk.Label(self.mainWin, relief="solid", height=10, width=10)
        self.enemyLabel1.grid(row=3, column=0)
        self.enemyLabel2 = tk.Label(self.mainWin, relief="solid", height=10, width=10)
        self.enemyLabel2.grid(row=3, column=1)
        self.enemyLabel3 = tk.Label(self.mainWin, relief="solid", height=10, width=10)
        self.enemyLabel3.grid(row=3, column=2)
        self.enemyLabel4 = tk.Label(self.mainWin, relief="solid", height=10, width=10)
        self.enemyLabel4.grid(row=3, column=3)
        self.enemyLabel5 = tk.Label(self.mainWin, relief="solid", height=10, width=10)
        self.enemyLabel5.grid(row=3, column=4)
        self.enemyLabel6 = tk.Label(self.mainWin, relief="solid", height=10, width=10)
        self.enemyLabel6.grid(row=3, column=5)
        self.enemyLabelList = [self.enemyLabel1, self.enemyLabel2, self.enemyLabel3, self.enemyLabel4, self.enemyLabel5, self.enemyLabel6]
        self.enemyLabelnum = 0
        self.inEnemyTeam = []

        self.yourLabel1 = tk.Label(self.mainWin, relief="solid", height=10, width=10)
        self.yourLabel1.grid(row=3, column=10)
        self.yourLabel2 = tk.Label(self.mainWin, relief="solid", height=10, width=10)
        self.yourLabel2.grid(row=3, column=11)
        self.yourLabel3 = tk.Label(self.mainWin, relief="solid", height=10, width=10)
        self.yourLabel3.grid(row=3, column=12)
        self.yourLabel4 = tk.Label(self.mainWin, relief="solid", height=10, width=10)
        self.yourLabel4.grid(row=3, column=13)
        self.yourLabel5 = tk.Label(self.mainWin, relief="solid", height=10, width=10)
        self.yourLabel5.grid(row=3, column=14)
        self.yourLabel6 = tk.Label(self.mainWin, relief="solid", height=10, width=10)
        self.yourLabel6.grid(row=3, column=15)

        self.runButton = tk.Button(self.mainWin, relief ="raised", text="Generate Team")
        self.runButton['command'] = self.callbackbutton
        self.runButton.grid(row=2, column=6)

        self.charaList = []
        for ch in charlist:
            name = ch.get("name")
            self.charaList.append(name)

        buttonList = ["self.AnaButton", "self.AsheButton", "self.BaptisteButton", "self.BastionButton", "self.BrigitteButton", "self.DVaButton", "self.DoomfistButton", "self.GenjiButton", "self.HanzoButton", "self.JunkratButton", "self.LucioButton", "self.McCreeButton", "self.MeiButton", "self.MercyButton", "self.MoiraButton", "self.OrisaButton", "self.PharahButton", "self.ReaperButton", "self.ReinhardtButton", "self.RoadhogButton", "self.Soldier76Button", "self.SombraButton", "self.SymmetraButton", "self.TorbjornButton", "self.TracerButton", "self.WidowmakerButton", "self.WinstonButton", "self.WreckingBallButton", "self.ZaryaButton", "self.ZenyattaButton"]
        self.photoList = ["self.1", "self.2", "self.3", "self.4", "self.5", "self.6", "self.7", "self.8", "self.9", "self.10", "self.11", "self.12", "self.13", "self.14", "self.15", "self.16", "self.17", "self.18", "self.19", "self.20", "self.21", "self.22", "self.23", "self.24", "self.25", "self.26", "self.27", "self.28", "self.29", "self.30"]
        column = 3
        i = 0
        row = 4
        for name in charaList:
            image = Image.open("OverwatchImages/"+name+".png")
            self.photoList[i] = ImageTk.PhotoImage(image)
            buttonList[i] = tk.Button(self.mainWin, image=self.photoList[i], height=150, width=100)
            # buttonList[i]["command"] = self.enemyCallback
            if column > 12:
                row = row + 1
                column = 3
            buttonList[i].grid(row=row, column=column)
            column = column + 1
            i = i + 1
        buttonList[0]["command"] = self.anaCallback
        buttonList[1]["command"] = self.asheCallback
        buttonList[7]["command"] = self.genjiCallback
        buttonList[8]["command"] = self.hanzoCallback


    def anaCallback(self):
        if self.enemyLabelnum == 0:
            self.enemyLabelList[self.enemyLabelnum].config(image=self.photoList[0], height=150, width=100)
            self.enemyLabelnum += 1
            self.inEnemyTeam.append("Ana")

        elif "Ana" not in self.inEnemyTeam:
            self.enemyLabelList[self.enemyLabelnum].config(image=self.photoList[0], height=150, width=100)
            self.enemyLabelnum += 1
            self.inEnemyTeam.append("Ana")

    def asheCallback(self):
        if self.enemyLabelnum == 0:
            self.enemyLabelList[self.enemyLabelnum].config(image=self.photoList[1], height=150, width=100)
            self.enemyLabelnum += 1
            self.inEnemyTeam.append("Ashe")

        elif "Ashe" not in self.inEnemyTeam:
            self.enemyLabelList[self.enemyLabelnum].config(image=self.photoList[1], height=150, width=100)
            self.enemyLabelnum += 1
            self.inEnemyTeam.append("Ashe")

    def genjiCallback(self):
        if self.enemyLabelnum == 0:
            self.enemyLabelList[self.enemyLabelnum].config(image=self.photoList[7], height=150, width=100)
            self.enemyLabelnum += 1
            self.inEnemyTeam.append("genji")

        elif "genji" not in self.inEnemyTeam:
            self.enemyLabelList[self.enemyLabelnum].config(image=self.photoList[7], height=150, width=100)
            self.enemyLabelnum += 1
            self.inEnemyTeam.append("genji")

    def hanzoCallback(self):
        if self.enemyLabelnum == 0:
            self.enemyLabelList[self.enemyLabelnum].config(image=self.photoList[8], height=150, width=100)
            self.enemyLabelnum += 1
            self.inEnemyTeam.append("hanzo")

        elif "hanzo" not in self.inEnemyTeam:
            self.enemyLabelList[self.enemyLabelnum].config(image=self.photoList[8 ], height=150, width=100)
            self.enemyLabelnum += 1
            self.inEnemyTeam.append("hanzo")

    def findTeam(self, eTeam, charList):
        eTeamValue = 0
        sTeam = []
        nameList = []
        teamValueList = []
        valueList = []
        for spot in eTeam:
            eTeamValue = eTeamValue + spot.get("invalue")
            for ch in charList:
                if spot.get("name") in ch:
                    newvalue = ch.get("invalue") + ch.get(spot.get("name"))
                    ch.pop("invalue")
                    ch.update({"invalue": newvalue})
        for ch in charList:
            value = ch.get("invalue")
            valueList.append(value)
        combList = list(itertools.combinations(charList, 6))
        for team in combList:
            sTeamValue = 0
            for ch in team:
                chvalue = ch.get("invalue")
                for ch2 in team:
                    if "s_" + ch2.get("name") in ch:
                        chvalue = chvalue + ch.get("s_" + ch2.get("name"))
                sTeamValue = sTeamValue + chvalue

            teamValueList.append(sTeamValue)
        tVMax = max(teamValueList)
        top = teamValueList.count(tVMax)
        # print(top)
        selectTeam = teamValueList.index(tVMax)
        sTeamO = combList[selectTeam]

        for ch in sTeamO:
            name = ch.get("name")
            nameList.append(name)
        sTeam = nameList

        for ch in eTeam:
            for ch2 in eTeam:
                if "s_" + ch2.get("name") in ch:
                    chvalue = ch.get("s_" + ch2.get("name"))
                    eTeamValue = eTeamValue + chvalue

        for ch in eTeam:
            for sch in sTeamO:
                if sch.get("name") in ch:
                    countvalue = ch.get(sch.get("name"))
                    eTeamValue = eTeamValue + countvalue

        return sTeam, sTeamValue, eTeamValue

    def callbackbutton(self):
        self.findTeam(self.inEnemyTeam, charlist)


    def run(self):
        self.mainWin.mainloop()


myGui = OverwatchGUI()
myGui.run()
