#importing tkinter
import tkinter as tk
from tkinter import *


class MainWindow:
    #The first method that gets run when MainWindow class in instantiated
    def __init__(self):
        #Settig up the main window, and fixing the geometry
        self.root = Tk()
        self.root.title("Machine's Project")
        self.root.geometry("500x500")
        # Allowing frame window to change
        # it's size according to user's need
        self.root.resizable(True, True)
        self.root.configure(bg="black")
        
        #This function will run the method, that builds the first window outlook in our main window
        self.window_one()
        
    def window_one(self):
        #The next command will clean the window if there are any widgets present
        self.clean_window(self.root)
        
        #Creating the layout of the window
        
        #Title of the window
        self.a = Label(self.root, text ="Please enter the following parameters",fg='white',font=20) 
        self.a.pack(padx=7,pady=7)
        self.a.configure(bg="black")
        
        #The frame for inputs
        self.frame = Frame(self.root)
        self.frame.pack(padx=7,pady=7)
        self.frame.configure(bg="black")


        #Param1 label and text box    
        self.param_1_label = Label(self.frame, text ="Enter Parameter1    ",fg='white')
        self.param_1_label.configure(bg="black")

        self.input_param_1 = Text(self.frame, height = 3,
                        width = 35,
                        bg = "light yellow")

        #Param2 label and text box  
        self.param_2_label = Label(self.frame, text ="Enter Parameter2    ",fg="white")
        self.param_2_label.configure(bg="black")
        self.input_param_2 = Text(self.frame, height = 3,
                        width = 35,
                        bg = "light yellow")

        
        #Frame for the submit button
        self.frame1 = Frame(self.root)
        self.frame1.pack(padx=7,pady=7)
        self.Display = Button(self.frame1, height = 2,
                        width = 20, 
                        text ="Show",fg="white",
                        command = lambda:self.take_input())  #The take input method shows the entered parameters in the output box
        self.Display.configure(bg="purple")
        self.frame1.configure(bg="black")

        #Frame for the submitted params
    
        self.frame2 = Frame(self.root)
        self.frame2.pack(padx=7,pady=7)
        self.frame2.configure(bg="black")
        self.output_label = Label(self.frame2, text ="Recheck Params  ",fg="white")
        self.output_label.configure(bg="black")  
        self.Output = Text(self.frame2, height = 4, 
                    width = 35, 
                    bg = "light cyan")

        #Frame for the next window button

        self.frame3 = Frame(self.root)
        self.frame3.pack(padx=7,pady=7)
        self.frame3.configure(bg="black")
        self.next_button = Button(self.frame3,height = 2,
                        width = 20, 
                        text ="Next",fg="white",
                        command = lambda:self.window_two()) #This button will clear destroy all the widgets of window one  and create the layout for window two.
        self.next_button.configure(bg="purple")        

        #Setting the geometry of different widgets
        self.param_1_label.grid(row=0,column=0,pady=10)
        self.input_param_1.grid(row=0,column=1,pady=10)
        self.param_2_label.grid(row=1,column=0,pady=10)

        self.input_param_2.grid(row=1,column=1,pady=10)

        self.Display.pack(padx=7,pady=7)

        self.output_label.grid(row=0,column=0,pady=10)
        self.Output.grid(row=0,column=1,pady=10)
        self.next_button.pack(padx=7,pady=7)
        self.root.mainloop()
    
    #The method below shows the entered parameters in the output text box
    def take_input(self):
        #The display message
        self.input = "Parameter1 = " + self.input_param_1.get("1.0", "end-1c")
        self.input = self.input+"\n"+"Parameter2 = "+ self.input_param_2.get("1.0", "end-1c")
        #Function displays the message
        self.Output.insert(END,self.input)
        
        #The diff parameters will be stored safely by  the method below
        self.save_param_values()
        #print(self.param1,self.param2)

    def save_param_values(self):
        self.param1 = self.input_param_1.get("1.0", "end-1c")
        self.param2 = self.input_param_2.get("1.0", "end-1c")

        

    

    
        
    #cleans the window of any widgets
    def clean_window(self,wid):
        self. widget_list = wid.winfo_children()
        for item in self.widget_list :
            if item.winfo_children() :
                self.widget_list.extend(item.winfo_children())
        
        for widget in self.widget_list:
            widget.destroy()
    
    
    #Backend and Gui code for motor will be written here
    def motor_output(self):
        pass
    #Backend and Gui code for generator will be written here
    def generator_output(self):
        pass

    def window_two(self):
        self.clean_window(self.root)
        
        self.title_label = Label(self.root,text="Choose Your Machine",font=20,fg='white')
        self.title_label.configure(bg='black')
        self.title_label.pack(pady=50)

        self.motor_button = Button(self.root,height = 2,
                        width = 20, 
                        text ="Motor",fg="white",
                        command = lambda:self.motor_output())

        self.generator_button = Button(self.root,height = 2,
                        width = 20, 
                        text ="Generator",fg="white",
                        command = lambda:self.generator_output())

        self.go_back_button = Button(self.root,height = 2,
                        width = 10, 
                        text ="Go Back",
                        command = lambda:self.window_one())


        self.motor_button.configure(bg='purple')
        self.motor_button.pack(pady=5)

        self.generator_button.configure(bg='purple')
        self.generator_button.pack(pady=5)

        self.go_back_button.configure(bg='light blue')
        self.go_back_button.pack(pady=30)

        




start = MainWindow()
