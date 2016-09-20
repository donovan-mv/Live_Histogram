import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as an

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(1,1,1)
ax.set_title("Live Histogram (16 bins)")
cap = cv.VideoCapture(0)

def anim(i):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    hist = cv.calcHist([gray],[0],None,[16],[0,256])
    y = []
    x = range(16)
    for i in hist:
        y.append(int(i[0]))
    return ax.bar(x, y, width=0.8)

animation = an.FuncAnimation(fig, anim, interval=50, blit=True)
fig.show()
cap.release()
