from pypixpile import *
from cmath import sin
from time import sleep

def createSinusoid(x, offset, frequency, amplitude):
    sinusoid = round(sin(x*frequency).real*amplitude)
    return offset+sinusoid, sinusoid

print(CLR)
for coordXMove in range(1, 10000):
    # coordXMove = 0
    length = 100
    xOffset = 5
    maxamplitude = 15

    # amplitude = 10
    # frequency = 0.1
    # yOffset = amplitude+1
    # yList1 = [createSinusoid(x+coordXMove, yOffset, frequency, amplitude) for x in range(1, length+1)]

    # amplitude = 5
    # frequency = 0.4
    # yOffset = amplitude+1
    # yList2 = [createSinusoid(x+coordXMove, yOffset, frequency, amplitude) for x in range(1, length+1)]

    # yList = [(x[0]+y[0], x[1]+y[1]) for x, y in zip(yList1, yList2)]

    
    amplitude = 10
    frequency = 0.1
    yOffset = amplitude+1
    yList = [createSinusoid(x+coordXMove, yOffset, frequency, amplitude) for x in range(1, length+1)]

    drawRectangle('-', 8, 0, xOffset+1, yOffset-amplitude, length+1, amplitude*2+1)
    for x, y in zip(range(1, length+1), yList):
        print(colorIt(f"{moveCursor(0, y[0])}|{str(-y[1]).rjust(3, ' ')}|", 15, 0))
        drawPixel('#', 9, 15, x+xOffset, y[0])
    print(moveCursor(0, 0))
    sleep(0.3)