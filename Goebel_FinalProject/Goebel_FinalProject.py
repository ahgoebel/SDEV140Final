'''
BMI Calculator
Austin Goebel
A program that calculate your BMI and lets you know if you are considered obese.
Version 1
7/27/22
'''


from tkinter import *
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):
    """Scale Image Retrieval"""

    def __init__(self):
        EasyFrame.__init__(self, title = "BMI Calculator")
        self.setResizable(False)
        imageLabel = self.addLabel(text = "",
                                   row = 0, column = 0,
                                   sticky = "NSEW")
        textLabel = self.addLabel(text = "You may want to consider diet and exercise.",
                                  row = 1, column = 0,
                                  sticky = "NSEW")
        
       
        self.image = PhotoImage(file = "scale.gif")
        imageLabel["image"] = self.image

        
        font = Font(family = "Verdana", size = 20, slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "blue"


#if __name__ == "__main__":
    #ImageDemo().mainloop()




class ImageDemo2(EasyFrame):
    """Squirrel Image Retrieval"""

    

    def __init__(self):

        
        
        EasyFrame.__init__(self, title = "BMI Calculator")
        self.setResizable(False)
        imageLabel = self.addLabel(text = "",
                                   row = 0, column = 0,
                                   sticky = "NSEW")
        textLabel = self.addLabel(text = "You're not overweight, keep eating!",
                                  row = 1, column = 0,
                                  sticky = "NSEW")
        
        self.image = PhotoImage(file = "squirrel.gif")
        imageLabel["image"] = self.image

        font = Font(family = "Verdana", size = 20, slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "blue"

#if __name__ == "__main__":
 #   ImageDemo2().mainloop()

class TextAreaDemo(EasyFrame):
    """Layout of the window"""
    
    def __init__(self):

        
        EasyFrame.__init__(self, "BMI Calculator")
        self.addLabel(text = "Name", row = 0, column = 0)
        self.addLabel(text = "Height (in Inches)", row = 1, column = 0)
        self.addLabel(text = "Weight (in pounds)", row = 2, column = 0)
        self.height = self.addIntegerField(value = 0, row = 1, column = 1)
        self.name = self.addTextField(text=" ", row = 0, column = 1)
        self.weight = self.addIntegerField(value = 0, row = 2, column = 1)
        

        self.compute = self.addButton(text = "Compute", row = 4, column = 0,
                                      columnspan = 2,
                                      command = self.compute)
        self.clear = self.addButton(text = "Clear", row = 5, column = 0,
                                      columnspan = 2,
                                      command = self.clear)
        self.exit = self.addButton(text = "Exit", row = 6, column = 0,
                                      columnspan = 2,
                                      command = self.exit)
        
    def compute(self):
        #Calculates BMI from user input
        height = self.height.getNumber()
        weight = self.weight.getNumber()
        name = self.name.getText()
        
        BMI = int((weight / (height * height)) * 703)
        string = str(BMI)
        self.result = self.prompterBox(title="Result", promptString = name + " your BMI is: " + string )

        

        


        if BMI > 30:
            ImageDemo().mainloop()
           
        else:
            ImageDemo2().mainloop()

    def clear(self):
        
        self.name.setText("")
        self.height.setNumber(0)
        self.weight.setNumber(0)
        


    def exit(self):
        exit()

def main():
    TextAreaDemo().mainloop()

if __name__ == "__main__":
    main()
    

