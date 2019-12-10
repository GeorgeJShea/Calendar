'''
__________________________________________________________________
Created By: George Shea                                 ßeta
Date Created: 5/12/2019
Version: 1.0
Version Update:

Use:
this program is a simple slot machine
__________________________________________________________________
'''
from graphics import *

'''
____________________________________________________________
initilize is responsible for only getting clander backdrop set up
its a bit yucky but straight forward
____________________________________________________________
'''
def initilize():
    print("This will be a calander of sort")
    window = GraphWin("Calander", 1500, 750)
    window.setCoords(0.0, 0.0, 1500, 750)
    window.setBackground('grey24')

    rec = Rectangle(Point(0,0), Point(1500, 700)).draw(window)
    rec.setWidth(4)
    rec.setOutline('white')

    # calander is 700 pixels high each one shoudl be 140 high
    line = Line(Point(0,140), Point(1500,140)).draw(window)
    line.setWidth(2)
    line.setFill('white')

    line = Line(Point(0,280), Point(1500,280)).draw(window)
    line.setWidth(2)
    line.setFill('white')

    line = Line(Point(0,420), Point(1500,420)).draw(window)
    line.setWidth(2)
    line.setFill('white')

    line = Line(Point(0,560), Point(1500,560)).draw(window)
    line.setWidth(2)
    line.setFill('white')

    line = Line(Point(214,0), Point(214,700)).draw(window)
    line.setWidth(2)
    line.setFill('white')

    line = Line(Point(428,0), Point(428,700)).draw(window)
    line.setWidth(2)
    line.setFill('white')

    line = Line(Point(642,0), Point(642,700)).draw(window)
    line.setWidth(2)
    line.setFill('white')

    line = Line(Point(856,140), Point(856,700)).draw(window)
    line.setWidth(2)
    line.setFill('white')

    line = Line(Point(1070,140), Point(1070,700)).draw(window)
    line.setWidth(2)
    line.setFill('white')

    line = Line(Point(1284,140), Point(1284,700)).draw(window)
    line.setWidth(2)
    line.setFill('white')

    jump = 0
    for tally in range(7):
        text = Text(Point(20+jump,680), tally+1).draw(window)
        text.setSize(16)
        text.setTextColor('light cyan')
        jump = jump + 214
    jump = 0
    for tally in range(7):
        text = Text(Point(20+jump,540), tally+8).draw(window)
        text.setSize(16)
        text.setTextColor('light cyan')
        jump = jump + 214
    jump = 0
    for tally in range(7):
        text = Text(Point(20+jump,400), tally+15).draw(window)
        text.setSize(16)
        text.setTextColor('light cyan')
        jump = jump + 214
    jump = 0
    for tally in range(7):
        text = Text(Point(20+jump,260), tally+22).draw(window)
        text.setSize(16)
        text.setTextColor('light cyan')
        jump = jump + 214
    jump = 0
    for tally in range(3):
        text = Text(Point(20+jump,120), tally+29).draw(window)
        text.setSize(16)
        text.setTextColor('light cyan')
        jump = jump + 214

    text = Text(Point(87,725), "Calander").draw(window)
    text.setSize(32)
    text.setTextColor('light cyan')
    Managment(window)

def CalanderDates(calander):
    window = calander
    popup = Rectangle(Point(750,0), Point(1500,700)).draw(window)
    popup.setFill('grey24')
    popup.setWidth(2)
    popup.setOutline('white')

    # for save and exit
    boxOne = Rectangle(Point(750,650), Point(1500,700)).draw(window)
    boxOne.setWidth(2)
    boxOne.setOutline('white')

    # title
    boxTwo = Rectangle(Point(750,600), Point(1500,650)).draw(window)
    boxTwo.setWidth(2)
    boxTwo.setOutline('white')

    textTwo = Text(Point(785, 630), "Title: ").draw(window)
    textTwo.setTextColor('white')
    textTwo.setSize(14)

    # Date
    boxThree = Rectangle(Point(750,550), Point(1500,600)).draw(window)
    boxThree.setWidth(2)
    boxThree.setOutline('white')

    textThree = Text(Point(785, 575), "Date: ").draw(window)
    textThree.setTextColor('white')
    textThree.setSize(14)

    textFour = Text(Point(785, 530), "Info: ").draw(window)
    textFour.setTextColor('white')
    textFour.setSize(14)

    # exit
    exitBox = Rectangle(Point(1450,650), Point(1500,670)).draw(window)
    exitBox.setFill('red')
    exitBox.setWidth(2)
    exitBox.setOutline('white')

    saveBox = Rectangle(Point(750,650), Point(800,670)).draw(window)
    saveBox.setFill('cyan')
    saveBox.setWidth(2)
    saveBox.setOutline('white')
    textDrawn = 1
    while True:
        posit = window.getMouse()
        positX = posit.getX()
        positY = posit.getY()

        if positX >= 750 and positX <= 1500 and positY >= 0 and positY <= 600:
            r = open("managmentStorage", "r")
            contentText = r.read()
            r.close()
            textLegnth = len(contentText)
            textOffset = textLegnth * 3

            textDrawn = 2
            while True:
                infoText = Text(Point(770 + textOffset, 500), contentText).draw(window)
                infoText.setSize(12)
                infoText.setTextColor('white')
                addKey = window.getKey()
                if addKey == "space":
                    contentText = contentText + " "
                    textOffset = textOffset + 3
                    infoText.undraw()
                elif addKey == "BackSpace":
                    contentText = contentText[:-1]
                    textOffset = textOffset - 3
                    infoText.undraw()
                elif addKey == "Escape":
                    print("ignore")
                    # this will just save the file instead need to make a save case
                    contentText = infoText.getText()
                    f = open("managmentStorage", "a+")
                    f.write(contentText)
                    f.close()
                    break
                else:
                    contentText = contentText + addKey
                    textOffset = textOffset + 3
                    infoText.undraw()


        if positX >= 1450 and positX <= 1500 and positY >= 650 and positY <= 670:
            saveBox.undraw()
            exitBox.undraw()
            boxOne.undraw()
            boxTwo.undraw()
            boxThree.undraw()
            textTwo.undraw()
            textThree.undraw()
            textFour.undraw()
            popup.undraw()
            if textDrawn == 2:
                infoText.undraw()
            break
    # where you can type

'''
____________________________________________________________
managment will be responsible for clicking on calander

____________________________________________________________
'''

def Managment(calander):
    window = calander

    print("managment launched")
    while True:
        posit = window.getMouse()
        positX = posit.getX()
        positY = posit.getY()

        # each grouping is 140 high and 214 wide
        # date 1
        if positX >= 0 and positY >= 576 and positX <= 214 and positY <= 700:
            CalanderDates(window)
        else:
            print("nothing")


initilize()
