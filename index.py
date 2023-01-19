import random
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QPushButton, QApplication, QGroupBox, QVBoxLayout, QTextBrowser

import game_window
import help_window
import main_window
import player_name_window

global language
global sound


def loadSettings():
    global language
    global sound
    settingsFile = open("settings", "r")
    tempList = settingsFile.read().split("\n")
    settingsFile.close()
    language = tempList[0].split("=")[1]
    sound = tempList[1].split("=")[1]
    return language, sound


def saveSettings():
    global language
    global sound
    settingsFile = open("settings", "w")
    settingsFile.write("language=" + language + "\n" + "sound=" + sound)
    settingsFile.close()


class Help(QtWidgets.QWidget, help_window.Ui_Form):
    referenceBox = None
    mainBox = None
    gameRulesBox = None
    settingsBox = None

    main_window_obj = None

    inBoxBackButton = None
    referenceTextArea = None
    changeLanguageButton = None
    changeSoundModeButton = None
    gameRulesTextArea = None

    settingsButton = None
    gameRulesButton = None
    referenceButton = None
    mainBackButton = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('robot.ico'))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.initialize()

    def updateStrings(self):
        global language
        global sound

        if language == "ru":
            self.referenceTextArea.setText(
                "Чтобы начать играть выберите режим игры (против компьютера или два игрока), введите имена и нажмите сохранить откроется окно игры, и 4 кнопки с помощью которых вы можете играть")
            self.gameRulesTextArea.setText(
                "Правила игры очень просты: робот <(-_-)>Виталик делает тортик произвольной величины, \nигроки по очереди кусают торт,и тот кто сьест последний кусочек , становится !!!Победителем!!!")
            self.settingsButton.setText("Настройки")
            self.gameRulesButton.setText("Правила игры")
            self.referenceButton.setText("Справка")
            self.mainBackButton.setText("Назад")
            self.inBoxBackButton.setText("Назад")
            self.changeLanguageButton.setText("Английский")
            if sound == "on":
                self.changeSoundModeButton.setText("Выкл звук")
            elif sound == "off":
                self.changeSoundModeButton.setText("Вкл звук")

        elif language == "en":
            self.referenceTextArea.setText(
                "To start playing, select the game mode (vs the computer or two players), enter the names and click save to open the game window, and 4 buttons with which you can play")
            self.gameRulesTextArea.setText(
                "The rules of the game are very simple: robot <(-_-)>Vitalik makes a cake of any size, the players take turns biting the cake,and the one who eats the last piece becomes !!!The Winner!!!")
            self.settingsButton.setText("Settings")
            self.gameRulesButton.setText("Rules")
            self.referenceButton.setText("Reference")
            self.mainBackButton.setText("Back")
            self.inBoxBackButton.setText("Back")
            self.changeLanguageButton.setText("Russian")
            if sound == "on":
                self.changeSoundModeButton.setText("Sound off")
            elif sound == "off":
                self.changeSoundModeButton.setText("Sound on")

    def initReferenceBox(self):
        self.referenceBox = QGroupBox()
        referenceBoxLayout = QVBoxLayout()

        self.referenceTextArea = QTextBrowser()

        referenceBoxLayout.addWidget(self.referenceTextArea)
        self.referenceBox.setLayout(referenceBoxLayout)
        self.verticalLayout.addWidget(self.referenceBox)

    def initMainBox(self):
        self.mainBox = QGroupBox()
        mainBoxLayout = QVBoxLayout()

        self.settingsButton = QPushButton("", self)
        self.settingsButton.clicked.connect(self.playSound)
        self.settingsButton.clicked.connect(self.showSettingsBox)

        self.gameRulesButton = QPushButton("", self)
        self.gameRulesButton.clicked.connect(self.playSound)
        self.gameRulesButton.clicked.connect(self.showGameRulesBox)

        self.referenceButton = QPushButton("", self)
        self.referenceButton.clicked.connect(self.playSound)
        self.referenceButton.clicked.connect(self.showReferenceBox)

        self.mainBackButton = QPushButton("", self)
        self.mainBackButton.clicked.connect(self.playSound)
        self.mainBackButton.clicked.connect(self.back)
        self.mainBackButton.setStyleSheet("background-color:red")

        mainBoxLayout.addWidget(self.settingsButton)
        mainBoxLayout.addWidget(self.gameRulesButton)
        mainBoxLayout.addWidget(self.referenceButton)
        mainBoxLayout.addWidget(self.mainBackButton)

        self.mainBox.setLayout(mainBoxLayout)
        self.verticalLayout.addWidget(self.mainBox)

    def initGameRulesBox(self):
        self.gameRulesBox = QGroupBox()
        gameRulesBoxLayout = QVBoxLayout()

        self.gameRulesTextArea = QTextBrowser()
        gameRulesBoxLayout.addWidget(self.gameRulesTextArea)
        self.gameRulesBox.setLayout(gameRulesBoxLayout)
        self.verticalLayout.addWidget(self.gameRulesBox)

    def initSettingsBox(self):
        global language
        global sound

        self.settingsBox = QGroupBox()
        settingsBoxLayout = QVBoxLayout()

        self.changeLanguageButton = QPushButton("", self)
        self.changeSoundModeButton = QPushButton("", self)

        def changeLanguage():
            global language
            if language == "ru":
                language = "en"
            elif language == "en":
                language = "ru"
            saveSettings()

        def changeSoundMode():
            global sound
            if sound == "on":
                sound = "off"
            elif sound == "off":
                sound = "on"
            saveSettings()

        self.changeLanguageButton.clicked.connect(changeLanguage)
        self.changeLanguageButton.clicked.connect(self.playSound)
        self.changeLanguageButton.clicked.connect(self.showSettingsBox)

        self.changeSoundModeButton.clicked.connect(changeSoundMode)
        self.changeSoundModeButton.clicked.connect(self.playSound)
        self.changeSoundModeButton.clicked.connect(self.showSettingsBox)

        settingsBoxLayout.addWidget(self.changeLanguageButton)
        settingsBoxLayout.addWidget(self.changeSoundModeButton)
        self.settingsBox.setLayout(settingsBoxLayout)
        self.verticalLayout.addWidget(self.settingsBox)

    def initialize(self):

        self.inBoxBackButton = QPushButton("", self)
        self.inBoxBackButton.setStyleSheet("background-color:red")
        self.inBoxBackButton.clicked.connect(self.playSound)
        self.inBoxBackButton.clicked.connect(self.showMainBox)

        self.initMainBox()
        self.initGameRulesBox()
        self.initReferenceBox()
        self.initSettingsBox()

        self.showMainBox()

    def showSettingsBox(self):
        self.updateStrings()
        self.gameRulesBox.setVisible(False)
        self.settingsBox.setVisible(True)
        self.mainBox.setVisible(False)
        self.referenceBox.setVisible(False)
        self.settingsBox.layout().addWidget(self.inBoxBackButton)

    def showGameRulesBox(self):
        self.updateStrings()
        self.gameRulesBox.setVisible(True)
        self.settingsBox.setVisible(False)
        self.mainBox.setVisible(False)
        self.referenceBox.setVisible(False)
        self.gameRulesBox.layout().addWidget(self.inBoxBackButton)

    def showMainBox(self):
        self.updateStrings()
        self.gameRulesBox.setVisible(False)
        self.settingsBox.setVisible(False)
        self.mainBox.setVisible(True)
        self.referenceBox.setVisible(False)
        self.gameRulesBox.layout().addWidget(self.inBoxBackButton)

    def showReferenceBox(self):
        self.updateStrings()
        self.gameRulesBox.setVisible(False)
        self.settingsBox.setVisible(False)
        self.mainBox.setVisible(False)
        self.referenceBox.setVisible(True)
        self.referenceBox.layout().addWidget(self.inBoxBackButton)

    def back(self):
        self.close()
        self.main_window_obj = MainWindow()
        self.main_window_obj.show()

    def playSound(self):
        if sound == "on":
            soundObj = QSound("sound.wav", self)
            soundObj.play()


class PlayerNameBox(QtWidgets.QDialog, player_name_window.Ui_Dialog):
    multiplayer = None
    gameWindowObj = None

    def __init__(self, flag):
        loadSettings()
        super().__init__()
        self.setWindowIcon(QIcon('robot.ico'))
        self.multiplayer = flag
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.saveButton.clicked.connect(self.save)
        self.secondPlayerNameLine.setVisible(self.multiplayer)
        self.saveButton.clicked.connect(self.playSound)
        self.updateStrings()

    def updateStrings(self):
        global language

        if language == "ru":
            self.saveButton.setText("Сохранить")
            self.firstPlayerNameLine.setPlaceholderText("Имя первого игрока")
            self.secondPlayerNameLine.setPlaceholderText("Имя второго игрока")
        elif language == "en":
            self.firstPlayerNameLine.setPlaceholderText("First player name")
            self.secondPlayerNameLine.setPlaceholderText("Second player name")
            self.saveButton.setText("Save")

    def playSound(self):
        if sound == "on":
            soundObj = QSound("sound.wav", self)
            soundObj.play()

    def save(self):
        if self.multiplayer:
            firstPlayerName = self.firstPlayerNameLine.text()
            secondPlayerName = self.secondPlayerNameLine.text()
            if firstPlayerName != "" and secondPlayerName != "":
                self.gameWindowObj = Game(self.multiplayer, firstPlayerName, secondPlayerName)
                self.gameWindowObj.show()
                self.close()
        else:
            firstPlayerName = self.firstPlayerNameLine.text()
            if firstPlayerName != "":
                self.gameWindowObj = Game(self.multiplayer, firstPlayerName, None)
                self.gameWindowObj.show()
                self.close()


class Game(QtWidgets.QWidget, game_window.Ui_Form):
    multiplayer = None
    cake = None

    buttons = []

    main_window_obj = None

    currentPlayer = None

    firstPlayerName = None
    secondPlayerName = None

    backToMainWindowButton = None

    bite = None

    takeBiteText = None
    becameText = None
    promptToEnterText = None
    cakeMakingText = None
    victoryText = None

    def __init__(self, flag, firstPlayerName, secondPlayerName):
        self.multiplayer = flag
        self.firstPlayerName = firstPlayerName
        self.secondPlayerName = secondPlayerName
        super().__init__()
        self.setWindowIcon(QIcon('robot.ico'))
        self.setupUi(self)
        self.initialize()

    def updateStrings(self):
        global language

        if language == "ru":
            self.victoryText = str(self.currentPlayer) + " победил!"
            self.takeBiteText = str(self.currentPlayer) + " откусил " + str(self.bite) + "см тортика"
            self.becameText = "Теперь тортик стал " + str(self.cake) + "см"
            self.promptToEnterText = str(self.currentPlayer) + " нажми на одну из кнопок чтобы откусить тортик"
            self.cakeMakingText = "<(-_-)>Виталик готовит тортик...Тортик получился: " + str(self.cake) + " см."
            self.backToMainWindowButton.setText("Назад в главное меню")
        elif language == "en":
            self.victoryText = str(self.currentPlayer) + " WIN!"
            self.takeBiteText = str(self.currentPlayer) + " took a bite " + str(self.bite) + "cm of the cake"
            self.becameText = "Now the cake has become " + str(self.cake) + "cm"
            self.promptToEnterText = str(self.currentPlayer) + " click on one of the buttons to take a bite of the cake"
            self.cakeMakingText = "<(-_-)>Виталик preparing a cake...The cake turned out: " + str(self.cake) + " cm."
            self.backToMainWindowButton.setText("Back to main")

    def playSound(self):
        if sound == "on":
            soundObj = QSound("sound.wav", self)
            soundObj.play()

    def backToMainWindow(self):
        self.close()
        self.main_window_obj = MainWindow()
        self.main_window_obj.show()

    def gameOver(self):
        for button in self.buttons:
            button.setDisabled(True)

    def takeBiteCake(self):
        button = QApplication.instance().sender()
        self.bite = int(button.text())
        self.updateStrings()
        if self.multiplayer:
            self.cake = self.cake - self.bite
            self.updateStrings()
            self.textBrowser.append(self.takeBiteText)
            if self.cake <= 0:
                self.textBrowser.append(self.victoryText)
                self.gameOver()
            else:
                if self.currentPlayer == self.firstPlayerName:
                    self.currentPlayer = self.secondPlayerName
                else:
                    self.currentPlayer = self.firstPlayerName
                self.textBrowser.append(self.becameText)
                self.textBrowser.append(self.promptToEnterText)

        else:
            self.cake = self.cake - self.bite
            self.textBrowser.append(self.takeBiteText)
            self.updateStrings()
            self.textBrowser.append(self.becameText)
            if self.cake <= 0:
                self.textBrowser.append(self.victoryText)
                self.gameOver()
            else:
                self.bite = random.randint(1, 4)
                self.cake = self.cake - self.bite
                self.currentPlayer = "<(-_-)>Виталик"
                self.updateStrings()
                self.textBrowser.append(self.takeBiteText)
                if self.cake <= 0:
                    self.textBrowser.append(self.victoryText)
                    self.gameOver()
                else:
                    self.currentPlayer = self.firstPlayerName
                    self.updateStrings()
                    self.textBrowser.append(self.becameText)
                    self.textBrowser.append(self.promptToEnterText)

    def initialize(self):

        self.buttons = []
        i = 1
        while i < 5:
            button = QPushButton(str(i), self)
            self.buttons.append(button)
            i += 1

        for button in self.buttons:
            button.clicked.connect(self.takeBiteCake)
            button.clicked.connect(self.playSound)
            self.horizontalBox.addWidget(button)

        self.backToMainWindowButton = QPushButton("", self)
        self.backToMainWindowButton.clicked.connect(self.backToMainWindow)
        self.backToMainWindowButton.clicked.connect(self.playSound)
        self.verticalLayout.addWidget(self.backToMainWindowButton)

        self.cake = random.randint(25, 100)
        self.currentPlayer = self.firstPlayerName
        self.updateStrings()
        self.textBrowser.append(self.cakeMakingText)
        self.textBrowser.append(self.promptToEnterText)


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    helpWindowObj = None
    playerNameBoxObj = None

    VERSION = "1.0"

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('robot.ico'))
        self.setupUi(self)
        self.onePlayerModeButton.clicked.connect(self.startOnePlayerMode)
        self.twoPlayersModeButton.clicked.connect(self.startTwoPlayersMode)
        self.helpButton.clicked.connect(self.openHelpWindow)
        self.onePlayerModeButton.clicked.connect(self.playSound)
        self.twoPlayersModeButton.clicked.connect(self.playSound)
        self.helpButton.clicked.connect(self.playSound)
        self.updateStrings()

    def updateStrings(self):
        global language

        if language == "ru":
            self.helloLabel.setText("Добро пожаловать!\nВыберите режим игры чтобы начать")
            self.helloLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.helpButton.setText("Помощь")
            self.onePlayerModeButton.setText("Против компьютера")
            self.twoPlayersModeButton.setText("Два игрока")
            self.versionLabel.setText("Версия " + self.VERSION)
            self.versionLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.setWindowTitle("Робот Виталик <(-_-)>")
        elif language == "en":
            self.helloLabel.setText("Welcome!\nSelect the game mode to start")
            self.helloLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.onePlayerModeButton.setText("One player mode")
            self.twoPlayersModeButton.setText("Two players mode")
            self.helpButton.setText("Help")
            self.versionLabel.setText("Version " + self.VERSION)
            self.versionLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.setWindowTitle("Robot Vitalic <(-_-)>")

    def playSound(self):
        if sound == "on":
            soundObj = QSound("sound.wav", self)
            soundObj.play()

    def openHelpWindow(self):
        self.helpWindowObj = Help()
        self.helpWindowObj.show()
        self.close()

    def startOnePlayerMode(self):
        self.playerNameBoxObj = PlayerNameBox(False)
        self.playerNameBoxObj.show()
        self.close()

    def startTwoPlayersMode(self):
        self.playerNameBoxObj = PlayerNameBox(True)
        self.playerNameBoxObj.show()
        self.close()


def my_excepthook(type, value, tback):
    QtWidgets.QMessageBox.critical(
        window, "Exception", str(value),
        QtWidgets.QMessageBox.Cancel
    )

    sys.__excepthook__(type, value, tback)


sys.excepthook = my_excepthook
app = QtWidgets.QApplication(sys.argv)
loadSettings()
window = MainWindow()
window.show()
sys.exit(app.exec_())
