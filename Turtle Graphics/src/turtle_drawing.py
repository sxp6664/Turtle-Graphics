from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

# Increase the number of iterations and circle sizes
for i in range(36):  # Increase the outer loop to draw more patterns
    for j in range(36):  # Increase the inner loop for larger patterns
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.002  # Decrease step for smoother color transition
        rt(90)
        circle(250 - j * 6, 90)  # Increase the initial radius
        lt(90)
        circle(250 - j * 6, 90)  # Increase the initial radius
        rt(180)

done()
