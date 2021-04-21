import tkinter as tk
import math
from tkinter import *


class MainWindow:
    # The first method that gets run when MainWindow class in instantiated
    def __init__(self):
        # Settig up the main window, and fixing the geometry
        self.root = Tk()
        self.root.title("Machine's Project")
        self.root.geometry("600x750")
        # Allowing frame window to change
        # it's size according to user's need
        self.root.resizable(True, True)
        self.root.configure(bg="black")

        # This function will run the method, that builds the first window outlook in our main window
        self.window_one()

    def window_one(self):
        # The next command will clean the window if there are any widgets present
        self.clean_window(self.root)

        # Creating the layout of the window

        # Title of the window
        self.a = Label(self.root, text="Please enter the following parameters", fg='white', font=20)
        self.a.pack(padx=7, pady=7)
        self.a.configure(bg="black")

        # The frame for inputs
        self.frame = Frame(self.root)
        self.frame.pack(padx=7, pady=7)
        self.frame.configure(bg="black")

        # Param1 label and text box
        self.param_1_label = Label(self.frame, text=" Terminal Voltage (Vt) ", fg='white')
        self.param_1_label.configure(bg="black")

        self.input_param_1 = Text(self.frame, height=2,
                                  width=25,
                                  bg="light yellow")

        # Param2 label and text box
        self.param_2_label = Label(self.frame, text=" Direct Axis Reluctance (Xd) ", fg="white")
        self.param_2_label.configure(bg="black")
        self.input_param_2 = Text(self.frame, height=2,
                                  width=25,
                                  bg="light yellow")

        # Param3 label and text box
        self.param_3_label = Label(self.frame, text=" Quadrature Axis Reluctance (Xq) ", fg='white')
        self.param_3_label.configure(bg="black")

        self.input_param_3 = Text(self.frame, height=2,
                                  width=25,
                                  bg="light yellow")

        # Param4 label and text box
        self.param_4_label = Label(self.frame, text=" Armature Resistance (Ra) ", fg='white')
        self.param_4_label.configure(bg="black")

        self.input_param_4 = Text(self.frame, height=2,
                                  width=25,
                                  bg="light yellow")

        # Param5 label and text box
        self.param_5_label = Label(self.frame, text=" Power Factor (cosɸ) ", fg='white')
        self.param_5_label.configure(bg="black")

        self.input_param_5 = Text(self.frame, height=2,
                                  width=25,
                                  bg="light yellow")

        # Param6 label and text box
        self.param_6_label = Label(self.frame, text=" Armature Current (Ia) ", fg='white')
        self.param_6_label.configure(bg="black")

        self.input_param_6 = Text(self.frame, height=2,
                                  width=25,
                                  bg="light yellow")

        # Frame for the submit button
        self.frame1 = Frame(self.root)
        self.frame1.pack(padx=7, pady=7)
        self.Display = Button(self.frame1, height=2,
                              width=20,
                              text="Submit", fg="white",
                              command=lambda: self.take_input())  # The take input method shows the entered parameters in the output box
        self.Display.configure(bg="purple")
        self.frame1.configure(bg="black")

        # Frame for the submitted params

        self.frame2 = Frame(self.root)
        self.frame2.pack(padx=7, pady=7)
        self.frame2.configure(bg="black")
        self.output_label = Label(self.frame2, text="Recheck Paramaters  ", fg="white")
        self.output_label.configure(bg="black")
        self.Output = Text(self.frame2, height=7,
                           width=40,
                           bg="light cyan")

        # Frame for the next window button

        self.frame3 = Frame(self.root)
        self.frame3.pack(padx=7, pady=7)
        self.frame3.configure(bg="black")
        self.next_button = Button(self.frame3, height=2,
                                  width=20,
                                  text="Next", fg="white",
                                  command=lambda: self.window_two())  # This button will clear destroy all the widgets of window one  and create the layout for window two.
        self.next_button.configure(bg="purple")

        # Setting the geometry of different widgets
        self.param_1_label.grid(row=0, column=0, pady=10)
        self.input_param_1.grid(row=0, column=1, pady=10)

        self.param_2_label.grid(row=1, column=0, pady=10)
        self.input_param_2.grid(row=1, column=1, pady=10)

        self.param_3_label.grid(row=2, column=0, pady=10)
        self.input_param_3.grid(row=2, column=1, pady=10)

        self.param_4_label.grid(row=3, column=0, pady=10)
        self.input_param_4.grid(row=3, column=1, pady=10)

        self.param_5_label.grid(row=4, column=0, pady=10)
        self.input_param_5.grid(row=4, column=1, pady=10)

        self.param_6_label.grid(row=5, column=0, pady=10)
        self.input_param_6.grid(row=5, column=1, pady=10)

        self.Display.pack(padx=7, pady=7)

        self.output_label.grid(row=0, column=0, pady=10)
        self.Output.grid(row=0, column=1, pady=10)
        self.next_button.pack(padx=7, pady=7)
        self.root.mainloop()

    # The method below shows the entered parameters in the output text box
    def take_input(self):
        # The display message
        self.input = "Terminal Voltage (Vt) = " + self.input_param_1.get("1.0", "end-1c")
        self.input = self.input + "\n" + "Direct Axis Reluctance (Xd) = " + self.input_param_2.get("1.0", "end-1c")
        self.input = self.input + "\n" + "Quadrature Axis Reluctance (Xq) = " + self.input_param_3.get("1.0", "end-1c")
        self.input = self.input + "\n" + "Armature Resistance (Ra) = " + self.input_param_4.get("1.0", "end-1c")
        self.input = self.input + "\n" + "Power Factor (cosɸ) = " + self.input_param_5.get("1.0", "end-1c")
        self.input = self.input + "\n" + "Armature Current (Ia) = " + self.input_param_6.get("1.0", "end-1c")
        # Function displays the message
        self.Output.insert(END, self.input)
        p1 = self.input_param_1.get("1.0", "end-1c")
        p2 = self.input_param_2.get("1.0", "end-1c")
        p3 = self.input_param_3.get("1.0", "end-1c")
        p4 = self.input_param_4.get("1.0", "end-1c")
        p5 = self.input_param_5.get("1.0", "end-1c")
        p6 = self.input_param_6.get("1.0", "end-1c")
        
       
        
        file_object = open("test1.txt","w")
        L = [p1+"\n",p2+"\n",p3+"\n",p4+"\n",p5+"\n",p6+"\n"]
        file_object.writelines(L)
        file_object.close()

        # The diff parameters will be stored safely by  the method below
        self.save_param_values()

    def save_param_values(self):
        file_object = open("test1.txt","r")


        output  = file_object.readlines()
        a,b,c,d,e,f = output
        self.param1 = float(a[:-1])
        self.param2 = float(b[:-1])
        self.param3 = float(c[:-1])
        self.param4 = float(d[:-1])
        self.param5 = float(e[:-1])
        self.param6 = float(f[:-1])

        
        file_object.close()
        

    # cleans the window of any widgets
    def clean_window(self, wid):
        
        self.widget_list = wid.winfo_children()
        for item in self.widget_list:
            if item.winfo_children():
                self.widget_list.extend(item.winfo_children())

        for widget in self.widget_list:
            widget.destroy()

    # Backend and Gui code for motor will be written here
    def motor_output(self):
        power_factor_angle = math.acos(self.param5)

        internal_power_angle = math.atan(((self.param1 * math.sin(power_factor_angle)) + ((-self.param6) * self.param3))/
                                         (((self.param1) * math.cos(power_factor_angle)) + ((-self.param6) * self.param4)))

        power_angle = power_factor_angle - internal_power_angle
        current_power_factor = math.cos(power_angle)

        Ef_ = (((((self.param1) * math.sin(power_factor_angle)) + ((-self.param6) * self.param3))**2) +
        ((((self.param1 )* math.cos(power_factor_angle)) + ((-self.param6) * self.param4))**2))**(0.5)

        Id = (-self.param6) * math.sin(internal_power_angle)

        Ef = Ef_ - Id*(self.param2 - self.param3)

        k = Ef/4*(self.param1)*self.param2
        m = (1/self.param3) - (1/self.param2)

        maxm_angle = math.acos((-k + (k**2 + 0.5*(m**2))**(0.5)) / m)

        maxm_reluctance_power = ((((self.param1)) ** 2) / 2) * m
        maxm_power_output = ((Ef*(self.param1))/self.param2)*math.sin(maxm_angle) + (maxm_reluctance_power)*math.sin(2 * maxm_angle)
        self.window_output(current_power_factor,power_angle,maxm_power_output,maxm_angle,maxm_reluctance_power,Ef)


    # Backend and Gui code for generator will be written here
    def generator_output(self):
        print(self.param5)
        power_factor_angle = math.acos(self.param5)

        internal_power_angle = math.atan((((self.param1) * math.sin(power_factor_angle)) + (self.param6 * self.param3))/
                                         (((self.param1) * math.cos(power_factor_angle)) + (self.param6 * self.param4)))

        power_angle = power_factor_angle - internal_power_angle
        current_power_factor = math.cos(power_angle)

        Ef_ = (((((self.param1) * math.sin(power_factor_angle)) + (self.param6 * self.param3))**2) +
        (((self.param1 * math.cos(power_factor_angle)) + (self.param6 * self.param4))**2))**(0.5)

        Id = self.param6 * math.sin(internal_power_angle)

        Ef = Ef_ + Id*(self.param2 - self.param3)

        k = Ef/4*self.param1*self.param2
        m = (1/self.param3) - (1/self.param2)

        maxm_angle = math.acos((-k + (k**2 + 0.5*(m**2))**(0.5)) / m)

        maxm_reluctance_power = (((self.param1) ** 2) / 2) * m
        maxm_power_output = ((Ef*self.param1)/self.param2)*math.sin(maxm_angle) + (maxm_reluctance_power)*math.sin(2 * maxm_angle)

        self.window_output(current_power_factor,power_angle,maxm_power_output,maxm_angle,maxm_reluctance_power,Ef)


    def window_output(self,current_power_factor,power_angle,maxm_power_output,maxm_angle,maxm_reluctance_power,Ef):
        #The next command will clean the window if there are any widgets present
        self.clean_window(self.root)
        
        #Creating the layout of the window
        
        #Title of the window
        self.o = Label(self.root, text ="Results",fg='white',font=20) 
        self.o.pack(padx=7,pady=7)
        self.o.configure(bg="black")
        
        #The frame for inputs
        self.o_frame = Frame(self.root)
        self.o_frame.pack(padx=7,pady=7)
        self.o_frame.configure(bg="black")


        #Param1 label and text box    
        self.cpf = Label(self.o_frame, text ="Current Power Factor and Power Angle      ",fg='white')
        self.cpf.configure(bg="black")

        self.o_cpf = Text(self.o_frame, height = 3,
                        width = 35,
                        bg = "light yellow")
        self.o_cpf.insert(END,"{} and {}".format(current_power_factor,power_angle*180/3.14))

        #Param2 label and text box  
        self.maxpower = Label(self.o_frame, text ="Maximum Power Output and corresponding Power Angle    ",fg="white")
        self.maxpower.configure(bg="black")
        self.o_maxpower = Text(self.o_frame, height = 3,
                        width = 35,
                        bg = "light yellow")
        self.o_maxpower.insert(END,"{} and {}".format(maxm_power_output,maxm_angle*180/3.14))
        #Param3 label and text box  
        self.maxreluctancepower = Label(self.o_frame, text ="Maximum Reluctance Power    ",fg="white")
        self.maxreluctancepower.configure(bg="black")
        self.o_maxreluctancepower = Text(self.o_frame, height = 3,
                        width = 35,
                        bg = "light yellow")
        self.o_maxreluctancepower.insert(END,"{}".format(maxm_reluctance_power))

        #Param4 label and text box  
        self.ef = Label(self.o_frame, text ="Induced EMF     ",fg="white")
        self.ef.configure(bg="black")
        self.o_ef = Text(self.o_frame, height = 3,
                        width = 35,
                        bg = "light yellow")
        self.o_ef.insert(END,"{}".format(Ef))

        #Setting the geometry of different widgets
        self.cpf.grid(row=0,column=0,pady=10)
        self.o_cpf.grid(row=0,column=1,pady=10)
        self.maxpower.grid(row=1,column=0,pady=10)

        self.o_maxpower.grid(row=1,column=1,pady=10)
        self.maxreluctancepower.grid(row=2,column=0,pady=10)
        self.o_maxreluctancepower.grid(row=2,column=1,pady=10)
        self.ef.grid(row=3,column=0,pady=10)

        self.o_ef.grid(row=3,column=1,pady=10)

        self.go_back_button_1 = Button(self.root,height = 2,
                        width = 10, 
                        text ="Go Back",
                        command = lambda:self.window_two())

        self.go_back_button_1.configure(bg='light blue')
        self.go_back_button_1.pack(pady=30)
        
        



    def window_two(self):
        self.clean_window(self.root)

        self.title_label = Label(self.root, text="Choose Your Machine", font=20, fg='white')
        self.title_label.configure(bg='black')
        self.title_label.pack(pady=50)

        self.motor_button = Button(self.root, height=2,
                                   width=20,
                                   text="Motor", fg="white",
                                   command=lambda: self.motor_output())

        self.generator_button = Button(self.root, height=2,
                                       width=20,
                                       text="Generator", fg="white",
                                       command=lambda: self.generator_output())

        self.go_back_button = Button(self.root, height=2,
                                     width=10,
                                     text="Go Back",
                                     command=lambda: self.window_one())

        self.motor_button.configure(bg='purple')
        self.motor_button.pack(pady=5)

        self.generator_button.configure(bg='purple')
        self.generator_button.pack(pady=5)

        self.go_back_button.configure(bg='light blue')
        self.go_back_button.pack(pady=30)


start = MainWindow()
