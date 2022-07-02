from tkinter import *

root = Tk()
root.geometry("600x700")
root.title("Percentage")

grade3_l = Label(root)
grade5_l = Label(root)
grade10_l = Label(root)

class grade3():
    def __init__(self, Social_Studies, Math, Science):
        self.Social_Studies = Social_Studies
        self.Math = Math
        self.Science = Science
    def percentage(self):
        totalmarks = self.Social_Studies + self.Math + self.Science
        x = totalmarks/300
        per = x * 100
        grade3_l["text"] = per

class grade5():
    def __init__(self, Social_Studies, Math, Science, Health, PE):
        self.Social_Studies = Social_Studies
        self.Math = Math
        self.Science = Science
        self.Health = Health
        self.PE = PE
    def percentage(self):
        totalmarks = self.Social_Studies + self.Math + self.Science + self.Health + self.PE
        x = totalmarks/500
        per = x * 100
        grade5_l["text"] = per
        
class grade10():
    def __init__(self, Social_Studies, Math, Science, Health, PE, Environmental_Science, Languistics, Art, Medical_Science, Remedial_Math):
        self.Social_Studies = Social_Studies
        self.Math = Math
        self.Science = Science
        self.Health = Health
        self.PE = PE
        self.Environmental_Science = Environmental_Science
        self.Languistics = Languistics
        self.Art = Art
        self.Medical_Science = Medical_Science
        self.Remedial_Math = Remedial_Math
    def percentage(self):
        totalmarks = self.Social_Studies + self.Math + self.Science + self.Health + self.PE + self.Environmental_Science + self.Languistics + self.Art + self.Medical_Science + self.Remedial_Math 
        x = totalmarks/1000
        per = x * 100
        grade10_l["text"] = per
        
obj3= grade3(98.5, 43.9, 100)

button3 = Button(root, text = "Grade 3", command = obj3.percentage)
button3.pack()
grade3_l.pack()

obj5 = grade5(98.5, 43.9, 100, 56.3, 82.1)
button5 = Button(root, text = "Grade 5", command = obj5.percentage)
button5.pack()
grade5_l.pack()

obj10 = grade10(98.5, 43.9, 100, 56.3, 82.1, 93.2, 36.7, 90.9, 25.9, 100)
button10 = Button(root, text = "Grade 10", command = obj10.percentage)
button10.pack()
grade10_l.pack()

root.mainloop()