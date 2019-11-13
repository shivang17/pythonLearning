# QUESTION 9
# Counting the growth rings of a tree is a good way to tell the age of a tree. Each growth ring counts as one year. Use a Canvas widget to draw how growth rings of a 5-year-old tree might look. Then user create_text() method, number each growth ring starting from the center and working outward with the age in years associated with that ring.

from tkinter import *

root = Tk()


width = 400

height = 400
center_X=width/2
center_Y=height/2


age=5
gap=(center_X/age)-1
distance=gap

canvas = Canvas(root, width=width, height=height)

for i in range(1,age+1):

    canvas.create_oval(center_X-distance, center_Y-distance, center_X+distance, center_Y+distance)
    canvas.create_text(center_X, center_Y-distance+10, text='{} year'.format(i))
    distance+=gap

canvas.pack()


mainloop()

