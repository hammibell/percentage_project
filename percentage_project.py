from tkinter import *

root = Tk()
root.title("Grade Percentages")
root.configure(background = "light blue")
root.geometry("500x500")

title = Label(root, text = "Grade + Percentages")
title.place(relx = 0.5, rely = 0.1, anchor = CENTER)

grade3_btn = Button(root, text = "Grade 3", padx = 20, pady = 10)
grade3_btn.place(relx = 0.5, rely = 0.2, anchor = CENTER)

grade3_percentage_label = Label(root)
grade3_percentage_label.place(relx = 0.5, rely = 0.3, anchor = CENTER)

grade4_btn = Button(root, text = "Grade 4", padx = 20, pady = 10)
grade4_btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)

grade4_percentage_label = Label(root)
grade4_percentage_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

grade5_btn = Button(root, text = "Grade 5", padx = 20, pady = 10)
grade5_btn.place(relx = 0.5, rely = 0.6, anchor = CENTER)

grade5_percentage_label = Label(root)
grade5_percentage_label.place(relx = 0.5, rely = 0.7, anchor = CENTER)

class grade3():
    def __init__(self, language_arts, math):
        self.language_arts = language_arts
        self.math = math
        
    def percentage(self):
        total_marks = self.language_arts + self.math
        total_marks_with_100 = total_marks * 100
        grade3_percentage = total_marks_with_100 / 2
        grade3_percentage_label["text"] = grade3_percentage
        
        
class grade4():
    def __init__(self, language_arts, math, science):
        self.language_arts = language_arts
        self.math = math
        self.science = science
 
    def percentage(self):
        total_marks = self.language_arts + self.math + self.science 
        total_marks_with_100 = total_marks * 100
        grade4_percentage = total_marks_with_100 / 2
        grade4_percentage_label["text"] = grade4_percentage
             
        
class grade5():
    def __init__(self, language_arts, math, science, social_studies):
        self.language_arts = language_arts
        self.math = math
        self.science = science
        self.social_studies = social_studies
             
    def percentage(self):
        total_marks = self.language_arts + self.math
        total_marks_with_100 = total_marks * 100
        grade5_percentage = total_marks_with_100 / 2
        grade5_percentage_label["text"] = grade5_percentage
             
                 
percent = grade3()
percent.grade3

percent1 = grade4()
percent.grade4

percent2 = grade5()
percent.grade5





root.mainloop()