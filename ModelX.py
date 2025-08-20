import numpy
import pygame
import random
from time import *
import sys
import tkinter
from math import *
import pickle
import threading

#------Colours------#
Red = (255,0,0)
White = (255,255,255)
Blue = (0,0,255)
Black = (0,0,0)
Grey = (90,90,90)
Buttonlight = (170,170,170)
Buttondark = (100,100,100)
Colours = [Red,White,Blue,Black,Grey]
ColoursStrings = ["Red","White","Blue","Black","Grey"]
Particles = []




#------Classes------#
class Particle():
    def __init__(self,mass,Particlex,Particley,velocityx,velocityy,colour,size
                 ,volume,Particleamount
                 ,radius,thickness,angle):
        self.mass = mass
        self.Particlex = Particlex
        self.Particley = Particley
        self.velocityx = velocityx
        self.velocityy = velocityy
        self.colour = colour
        self.size = size
        self.volume = volume
        self.Particleamount = Particleamount
        self.radius = radius
        self.thickness = thickness
        self.angle = angle


 #Displays the particle graphically on the window
        def graphics(self):
            for particle in particles:
                draw_circle(screen,self.Particlex,self.Particley,self.radius,self.colour)   
            
            pygame.display.update()
            mainClock.tick(60)
                


#Determines resulting momentum after collision
            
        def collision(self):
            pass            


        def Particlemotion(self):
            self.Particlex += self.velocityx 
            self.Particley += self.Velocityy
            

#Updates to the current particle dimensions
        
        def update(self):                                
            pass

#Determines momentum at simualtion start

        def momentum(self):      
            pass
        






          
class Domain():
    def __init__(self,Domainx,Domainy):
        self.Domainx = Domainx
        self.Domainy = Domainy

        def Update():                                                   #Updates the domain if the user changes a varaible during the simulation
            pass
    

        

    
#------Functions------#

    
#timer for ending the program
def timer():
    pass

def displayresults():
    pass

def results():
    pass
    
           
#Displays to the user an end screen 
def endscreen():
    global Collisions
    global time
    running = True

    
    
    #Sets values to int so user isnt displayed with floats
    Collisions = int(Collisions)
    time = int(time)
    #The mean collisions per second
    avg_collisions = Collisions // time
    
    Results = pygame.Rect(setbuttonx-500,setbuttony-300,1000,75)
    title1 = pygame.Rect(setbuttonx-500,setbuttony-225,1000,75) 
    firstresult = pygame.Rect(setbuttonx-500,setbuttony-150,1000,75)
    title2 = pygame.Rect(setbuttonx-500,setbuttony-75,1000,75)
    secondresult = pygame.Rect(setbuttonx-500,setbuttony,1000,75)
    title3 = pygame.Rect(setbuttonx-500,setbuttony+75,1000,75)
    thirdresult = pygame.Rect(setbuttonx-500,setbuttony+150,1000,75)
    Quit = pygame.Rect(x-300,y-y,500,100)
    menu = pygame.Rect(x-x,y-y,300,100)    
        
    while running:
        screen.fill(Black)
        pygame.draw.rect(screen,White,Results)
        pygame.draw.rect(screen,Buttonlight,title1)
        pygame.draw.rect(screen,Grey,firstresult)
        pygame.draw.rect(screen,Buttonlight,title2)
        pygame.draw.rect(screen,Grey,secondresult)
        pygame.draw.rect(screen,Buttonlight,title3)
        pygame.draw.rect(screen,Grey,thirdresult)
        pygame.draw.rect(screen,Grey,Quit)
        pygame.draw.rect(screen,Grey,menu)
        
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #Used to allow user to leave screen with esc key
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if Quit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                if menu.collidepoint(event.pos):
                    main_menu()
                    
        draw_text('Results',maintext,Black,screen,setbuttonx-100,setbuttony-285)
        draw_text('Collisions Per Second',maintext,White,screen,setbuttonx-250,setbuttony-215)
        draw_text('Total Collisions',maintext,White,screen,setbuttonx-200,setbuttony-65)
        draw_text('Total Time',maintext,White,screen,setbuttonx-140,setbuttony+90)
        draw_text(str(avg_collisions//175),maintext,Black,screen,setbuttonx-50,setbuttony-140)
        draw_text(str(Collisions//175),maintext,Black,screen,setbuttonx-50,setbuttony+10)
        draw_text(str(time)+'s',maintext,Black,screen,setbuttonx-25,setbuttony+160)
        draw_text('Quit',maintext,Black,screen,x-200,setbuttony-440)
        draw_text('Return',maintext,Black,screen,x-x+50,setbuttony-460)
        draw_text('To Menu',maintext,Black,screen,x-x+50,setbuttony-410)
        

        
        
        pygame.display.update()
        mainClock.tick(60)


#Saves the variable the user has inputted and those that have been randomly generated
def save():
    #Writes to a file the variables inputted
    with open('Variables.pkl','wb') as pickle_file:
        pickle.dump(Particles, pickle_file)
    
        
    
    

#Loads a preset template if chosen
def Template():
    game()


Collisions = 0
time = 0
#Displays the particles with motion and collisions and sets domain boundary
def Display():
    global Collisions
    global time
    running = True
    #used so that the simulation can be paused using a while loop of booleans changed with inputs 
    unpaused = True
    #sets the starting time to find the total time of the simulation and variables needed to display time 
    start = perf_counter()
    totaltime = 60
    z = 0
    
    sidebar = pygame.Rect(x-450,0,x,y)
    ClassA = pygame.Rect(x-350,setbuttony-200,300,100)
    ClassB = pygame.Rect(x-350,setbuttony,300,100)
    Pause = pygame.Rect(x-430,setbuttony+150,250,100)
    Unpause = pygame.Rect(x-230,setbuttony+150,250,100)
    Reset = pygame.Rect(x-325,setbuttony+300,250,100)
    Save = pygame.Rect(x-425,setbuttony-450,250,100)
    end = pygame.Rect(x-225,setbuttony-450,250,100)
    #Used to store the starting position for reset button and results
    Startingposition = []
    
    while running:
        pygame.draw.rect(screen,Grey,sidebar)
        pygame.draw.rect(screen,White,ClassA)
        pygame.draw.rect(screen,White,ClassB)
        pygame.draw.rect(screen,White,Pause)
        pygame.draw.rect(screen,White,Unpause)
        pygame.draw.rect(screen,White,Reset)
        pygame.draw.rect(screen,White,Save)
        pygame.draw.rect(screen,White,end)
        
        draw_text('Class A',maintext,Black,screen,x-330,setbuttony-175)
        draw_text('Class B',maintext,Black,screen,x-330,setbuttony+25)
        draw_text('Pause',maintext,Black,screen,x-430,setbuttony+175)
        draw_text('Unpause',maintext,Black,screen,x-220,setbuttony+175)
        draw_text('Reset',maintext,Black,screen,x-300,setbuttony+325)
        draw_text('Save',maintext,Black,screen,x-400,setbuttony-425)
        draw_text('End',maintext,Black,screen,x-200,setbuttony-425)
                
        
        # Used to store the beginning position of a partice to reset 
        for i in range(len(Particles)):
            Startingposition.append((Particles[i].Particlex,Particles[i].Particley))
            
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #Used to allow user to leave screen with esc key
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if ClassA.collidepoint(event.pos):
                    Classa()
                if ClassB.collidepoint(event.pos):
                    Classb()
                if Unpause.collidepoint(event.pos):
                    unpaused = True
                if Pause.collidepoint(event.pos):
                    unpaused = False
                #Changes the position to beginning if pressed
                if Reset.collidepoint(event.pos):
                    for i in range(len(Particles)):
                        Particles[i].Particlex = Startingposition[i][0]
                        Particles[i].Particley = Startingposition[i][1]
                if Save.collidepoint(event.pos):
                    save()
                if end.collidepoint(event.pos):
                    end = perf_counter()
                    time = end - start
                    endscreen()
                    
                    
            
                    
        #If the user hasnt paused the simulation it runs
        while unpaused:
            screen.fill(Black)
            
            measure = perf_counter()
            current = measure - start
            
            pygame.draw.rect(screen,Grey,sidebar)
            pygame.draw.rect(screen,White,ClassA)
            pygame.draw.rect(screen,White,ClassB)
            pygame.draw.rect(screen,White,Pause)
            pygame.draw.rect(screen,White,Unpause)
            pygame.draw.rect(screen,White,Reset)
            pygame.draw.rect(screen,White,Save)
            pygame.draw.rect(screen,White,end)
            
            draw_text('Class A',maintext,Black,screen,x-330,setbuttony-175)
            draw_text('Class B',maintext,Black,screen,x-330,setbuttony+25)
            draw_text('Pause',maintext,Black,screen,x-430,setbuttony+175)
            draw_text('Unpause',maintext,Black,screen,x-220,setbuttony+175)
            draw_text('Reset',maintext,Black,screen,x-300,setbuttony+325)
            draw_text('Save',maintext,Black,screen,x-400,setbuttony-425)
            draw_text('End',maintext,Black,screen,x-200,setbuttony-425)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                #Used to allow user to leave screen with esc key
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == MOUSEBUTTONDOWN:
                    if ClassA.collidepoint(event.pos):
                        Classa()
                    if ClassB.collidepoint(event.pos):
                        Classb()
                    if Unpause.collidepoint(event.pos):
                        unpaused = True
                    if Pause.collidepoint(event.pos):
                        unpaused = False
                    if Reset.collidepoint(event.pos):
                        for i in range(len(Particles)):
                            Particles[i].Particlex = Startingposition[i][0]
                            Particles[i].Particley = Startingposition[i][1]
                        totaltime = 60
                    if Save.collidepoint(event.pos):
                        save()
                    #user ends the simualtion and the final time is recorded by finding the difference of the start and end
                    if end.collidepoint(event.pos):
                        end = perf_counter()
                        time = end - start
                        endscreen()
            #Checks the time and displays it to the user                 
            if current > z+1  :
                z += 1
                totaltime -= 1

            if totaltime == 0:
                end = perf_counter()
                time = end - start
                endscreen()
            
            
                # Stops the Particles leaving the screen reverses the velocity once the domian boundary is reached
            for i in range(len(Particles)):
                if Particles[i].Particlex >= x-450 or Particles[i].Particlex <= 0:
                    Particles[i].velocityx = -Particles[i].velocityx
                if Particles[i].Particley >= y or Particles[i].Particley <= 0:
                    Particles[i].velocityy = -Particles[i].velocityy
                    
            # Checks through another loop to check Particles against each other for collisions
                for j in range(len(Particles)):
                    if i == j:
                        pass

                    if sqrt((Particles[i].Particlex-Particles[j].Particlex)**2 +(Particles[i].Particley-Particles[j].Particley)**2)> Particles[i].radius + Particles[j].radius:
                        Particles[i].velocityx = -Particles[i].velocityx
                        Particles[j].velocityx = -Particles[j].velocityx
                        Particles[i].velocityy = -Particles[i].velocityy
                        Particles[j].velocityy = -Particles[j].velocityy
                        Collisions += 1
                                                                                                  
                #Used to update the particles on the screen and have motion   
                Particles[i].Particlex += Particles[i].velocityx 
                Particles[i].Particley += Particles[i].velocityy 
                
                draw_text(str(totaltime)+'/60',maintext,White,screen,setbuttonx+200,setbuttony+350)
                pygame.draw.circle(screen,(Particles[i].colour),(int(Particles[i].Particlex),int(Particles[i].Particley)),Particles[i].radius,Particles[i].thickness)
            pygame.display.update()
            mainClock.tick(60)
                                                                            

def Particlecreation():
    global ClassA_volume
    global ClassA_mass
    global ClassA_radius
    global ClassA_Amount
    global ClassA_colour
    global ClassB_volume
    global ClassB_mass
    global ClassB_radius
    global ClassB_Amount
    global ClassB_colour
    global Particles 

    running = True

    ClassA_volume = int(ClassA_volume)
    ClassA_mass = int(ClassA_mass)
    ClassA_radius = int(ClassA_radius)
    ClassA_Amount = int(ClassA_Amount)

    ClassB_volume = int(ClassB_volume)
    ClassB_mass = int(ClassB_mass)
    ClassB_radius = int(ClassB_radius)
    ClassB_Amount = int(ClassB_Amount)

    TotalAmount = ClassA_Amount + ClassB_Amount
        
    while running:
        screen.fill(Black)

        for i in range(0,ClassA_Amount):
            Particlex = random.randint(0,x-450)
            Particley = random.randint(0,y)
            angle = random.randint(0,360)
            velocity = random.randint(1,5)
            velocityx = (cos(radians(angle))*velocity)
            velocityy = (sin(radians(angle))*velocity)
            size = random.randint(0,ClassA_radius)
            thickness = ClassA_radius

            ParticleName = Particle(ClassA_mass,Particlex,Particley,velocityx,velocityy,ClassA_colour,size
                     ,ClassA_volume,ClassA_Amount
                     ,ClassA_radius,thickness,angle)
            
            Particles.append(ParticleName)

        for i in range(0,ClassB_Amount):
            Particlex = random.randint(0,x-450)
            Particley = random.randint(0,y)
            angle = random.randint(0,360)
            velocity = random.randint(1,5)
            velocityx = (cos(radians(angle))*velocity)
            velocityy = (sin(radians(angle))*velocity)
            size = random.randint(0,100)
            thickness = ClassB_radius 
            
            ParticleName = "Particle" + str(len(Particles)) + 'B'
            ParticleName = Particle(ClassB_mass,Particlex,Particley,velocityx,velocityy,ClassB_colour,size
                     ,ClassB_volume,ClassB_Amount
                     ,ClassB_radius,thickness,angle)
            
            Particles.append(ParticleName)            
        
        if len(Particles) == TotalAmount:
            Display()

        pygame.display.update()
        mainClock.tick(60)
            

ClassA_volume = ''
ClassA_mass = ''
ClassA_Amount = ''
ClassA_radius = ''
ClassA_colour = ''
#Allows user to input all variables needed for class a
def Classa():
    global ClassA_volume
    global ClassA_mass
    global ClassA_radius
    global ClassA_Amount
    global ClassA_colour
    global Colours
    global ColoursStrings
    # Dimensions of the rectangles used for collision points of the button and typing
    running = True
    classB = pygame.Rect(x-350,0,400,100)
    particleamount = pygame.Rect(setbuttonx-225,setbuttony-280,400,100)
    mass = pygame.Rect(setbuttonx-225,setbuttony-120,400,100)
    radius = pygame.Rect(setbuttonx-225,setbuttony+40,400,100)
    volume = pygame.Rect(setbuttonx-225,setbuttony+200,400,100)
    Colour = pygame.Rect(setbuttonx-225,setbuttony+360,400,100)
    Finish = pygame.Rect(setbuttonx+325,setbuttony,450,100)

    # Blank text to be inputted to set the variable
    particleamountinput = ''
    massinput = ''
    radiusinput = ''
    volumeinput = ''
    Colourinput = ''
    #Colors of the buttons for hovering
    regular = White
    inputting = Grey
    colour = regular
    colour1 = regular
    colour2= regular
    colour3 = regular
    colour4 = regular
    #Used for the loops for hovering
    active = False
    active1 = False
    active2 = False
    active3 = False
    active4 = False
    Completeda = False
    Completedb = False
    
    while running:
        #Resets the screen to Black when the function is run
        screen.fill((Black))
        #Creates rectangles for user to know where to input
        pygame.draw.rect(screen,White,(setbuttonx-225,setbuttony-450,500,100))
        pygame.draw.rect(screen,White,classB)
        pygame.draw.rect(screen,White,particleamount)
        pygame.draw.rect(screen, White,mass)
        pygame.draw.rect(screen,White,radius)
        pygame.draw.rect(screen,White,volume)
        pygame.draw.rect(screen,White,Colour)
        pygame.draw.rect(screen,Grey,Finish)

        #allows for user to exit program
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #Used to allow user to leave screen with esc key
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        #Allows user to traverse between class customisation on class A screen
            if event.type == MOUSEBUTTONDOWN:
                if classB.collidepoint(event.pos):
                    Classb()
        #Particle amount function to recieve input and help user acknowledge button press with colour change 
            if event.type == MOUSEBUTTONDOWN:
                if particleamount.collidepoint(event.pos):
                    active = not active
                    particleamountinput = ''
                else:
                    active = False
                colour = inputting if active else regular
            # Records user input and allows it
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN :
                        print(particleamountinput)
                        try:
                            int(particleamountinput)
                            ClassA_Amount = particleamountinput
                            particleamountinput = ''
                        except:
                            particleamountinput = 'Try again'
                            print('Wrong')
                    elif event.key == pygame.K_BACKSPACE:
                        particleamountinput = particleamountinput[:-1]
                    else:
                        particleamountinput += event.unicode
                        
        #mass input and colour change                

            if event.type == MOUSEBUTTONDOWN:
                if mass.collidepoint(event.pos):
                    active1 = not active1
                    massinput = ''
                else:
                    active1 = False
                colour1 = inputting if active1 else regular
            # Records user input and allows it
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_RETURN:
                        print(massinput)
                        try:
                            int(massinput)
                            ClassA_mass = massinput
                            massinput = ''
                        except:
                            massinput = 'Try again'
                            print('Wrong')
                        
                    elif event.key == pygame.K_BACKSPACE:
                        massinput = massinput[:-1]
                    else:
                        massinput += event.unicode

        #Radius input and button colour change
            if event.type == MOUSEBUTTONDOWN:
                if radius.collidepoint(event.pos):
                    active2 = not active2
                    radiusinput = ''
                else:
                    active2 = False
                colour2 = inputting if active2 else regular
            #Records user input 
            if event.type == pygame.KEYDOWN:
                if active2:
                    if event.key == pygame.K_RETURN:
                        print(radiusinput)
                        try:
                            int(radiusinput)
                            ClassA_radius = radiusinput
                            radiusinput = ''
                        except:
                            radiusinput = 'Try again'
                            print('Wrong')
                        
                    elif event.key == pygame.K_BACKSPACE:
                        radiusinput = radiusinput[:-1]
                    else:
                        radiusinput += event.unicode
                
            #volume input and button colour change
                        
            if event.type == MOUSEBUTTONDOWN:
                if volume.collidepoint(event.pos):
                    active3 = not active3
                    volumeinput = ''
                else:
                    active3 = False
                colour3 = inputting if active3 else regular
            #Records user input 
            if event.type == pygame.KEYDOWN:
                if active3:
                    if event.key == pygame.K_RETURN:
                        print(volumeinput)
                        try:
                            int(volumeinput)
                            ClassA_volume = volumeinput
                            volumeinput = ''
                        except:
                            volumeinput = 'Try again'
                            print('Wrong')
                        
                    elif event.key == pygame.K_BACKSPACE:
                        volumeinput = volumeinput[:-1]
                    else:
                        volumeinput += event.unicode
            
            #Particle Colour input and button colour change
                        
            if event.type == MOUSEBUTTONDOWN:
                if Colour.collidepoint(event.pos):
                    active4 = not active4
                    Colourinput = ''
                else:
                    active4 = False
                colour4 = inputting if active4 else regular
            #Records user input 
            if event.type == pygame.KEYDOWN:
                if active4:
                    if event.key == pygame.K_RETURN:
                        Check = False
                        print(Colourinput)
                        for i in range(len(Colours)):
                            if ColoursStrings[i].lower() == str(Colourinput).lower():
                                ClassA_colour = Colours[i]
                                Check = True
                        if Check == False:
                            Colourinput = 'Try Again'
                        
                    elif event.key == pygame.K_BACKSPACE:
                        Colourinput = Colourinput[:-1]
                    else:
                        Colourinput += event.unicode
            #Used to check if the user has inputted all the varaibles and giving appropriate response             
            if ClassB_volume and ClassB_radius and ClassB_mass and ClassB_Amount and len(ClassB_colour)>0:
                Completedb = True

            if ClassA_volume and ClassA_radius and ClassA_mass and ClassA_Amount and len(ClassA_colour)>0:
                Completeda = True
                
                        
            if event.type == MOUSEBUTTONDOWN:
                if Finish.collidepoint(event.pos) and Completedb == True and Completeda == True:
                    Particlecreation()
                if Finish.collidepoint(event.pos) and Completeda == True and Completedb == False:
                    Classb()
                    
        inputsurface = maintext.render(particleamountinput, True, colour)
        inputsurface1 = maintext.render(massinput, True, colour1)
        inputsurface2 = maintext.render(radiusinput, True, colour2)
        inputsurface3 = maintext.render(volumeinput,True,colour3)
        inputsurface4 = maintext.render(Colourinput,True,colour4)
        #Extends textbox width if input exceeds   
        width = max(500, inputsurface.get_width()+10)
        width1 = max(500, inputsurface1.get_width()+10)
        width2 = max(500, inputsurface2.get_width()+10)
        width3 = max(500, inputsurface3.get_width()+10)
        width4 = max(500, inputsurface4.get_width()+10)
        #applies width dunction to textboxes
        particleamount.w = width
        mass.w = width1
        radius.w = width2
        volume.w = width3
        Colour.w = width4
        #Displays text
        screen.blit(inputsurface, (particleamount.x+5, particleamount.y+5))
        screen.blit(inputsurface1, (mass.x+5, mass.y+5))
        screen.blit(inputsurface2, (radius.x+5, radius.y+5))
        screen.blit(inputsurface3, (volume.x+5, volume.y+5))
        screen.blit(inputsurface4, (Colour.x+5, Colour.y+5))
        #Display the button has been presssed with a border
        
        pygame.draw.rect(screen, colour1, mass, 5)
        pygame.draw.rect(screen, colour, particleamount, 5)
        pygame.draw.rect(screen, colour2, radius, 5)
        pygame.draw.rect(screen,colour3, volume,5)
        pygame.draw.rect(screen,colour4,Colour,5)
        #Display text so user understands each button
        
        draw_text('Particle amount', maintext,White,screen,setbuttonx-180,setbuttony-330)
        draw_text('Class A', secondarytitle, Titlecolour, screen, 20,20)
        draw_text('Variables', Button , Black, screen, setbuttonx-120,setbuttony-430)
        draw_text('Mass',maintext,White,screen,setbuttonx-70,setbuttony-175)
        draw_text('Radius',maintext,White,screen,setbuttonx-60,setbuttony-10)
        draw_text('To Class B', maintext, Black,screen, x-300,20)
        draw_text('Volume', maintext, White,screen,setbuttonx-60,setbuttony+150)
        draw_text('Particle Colour', maintext,White,screen,setbuttonx-180,setbuttony+310)
        draw_text('Finish',maintext,Black,screen,setbuttonx+440,setbuttony+30)
                                                                
            
        pygame.display.update()
        mainClock.tick(60)
        
#Allows user to input variables for class b
ClassB_volume = ''
ClassB_mass = ''
ClassB_Amount = ''
ClassB_radius = ''
ClassB_colour = ''
def Classb():
    global ClassB_volume
    global ClassB_mass
    global ClassB_radius
    global ClassB_Amount
    global ClassB_colour
    global Colours
    global ColoursStrings
    
    # Dimensions of the rectangles used for collision points of the button and typing
    running = True
    classA = pygame.Rect(x-350,0,400,100)
    particleamount = pygame.Rect(setbuttonx-225,setbuttony-280,400,100)
    mass = pygame.Rect(setbuttonx-225,setbuttony-120,400,100)
    radius = pygame.Rect(setbuttonx-225,setbuttony+40,400,100)
    volume = pygame.Rect(setbuttonx-225,setbuttony+200,400,100)
    Colour = pygame.Rect(setbuttonx-225,setbuttony+360,400,100)
    Finish = pygame.Rect(setbuttonx+325,setbuttony,450,100)
    

    # Blank text to be inputted to set the variable
    particleamountinput = ''
    massinput = ''
    radiusinput = ''
    volumeinput = ''
    Colourinput = ''
    # Colors of the buttons for hovering
    regular = White
    inputting = Grey
    colour = regular
    colour1 = regular
    colour2= regular
    colour3 = regular
    colour4 = regular
    #Used for the loops for hovering
    active = False
    active1 = False
    active2 = False
    active3 = False
    active4 = False
    Completedb = False
    Completeda = False
    
    while running:
        screen.fill((Black))
        #Creates rectangles for user to know where to input
        pygame.draw.rect(screen,White,(setbuttonx-225,setbuttony-450,500,100))
        pygame.draw.rect(screen,White,classA)
        pygame.draw.rect(screen,White,particleamount)
        pygame.draw.rect(screen,White,mass)
        pygame.draw.rect(screen,White,radius)
        pygame.draw.rect(screen,White,volume)
        pygame.draw.rect(screen,White,Colour)
        pygame.draw.rect(screen,Grey,Finish)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game()
            if event.type == MOUSEBUTTONDOWN:
                if classA.collidepoint(event.pos):
                    Classa()
        #Particle amount
            if event.type == MOUSEBUTTONDOWN:
                if particleamount.collidepoint(event.pos):
                    active = not active
                    particleamountinput = ''
                else:
                    active = False
                colour = inputting if active else regular
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(particleamountinput)
                        try:
                            int(particleamountinput)
                            ClassB_Amount = particleamountinput
                            particleamountinput = ''
                        except:
                            particleamountinput = 'Try again'
                            print('Wrong')
                        
                    elif event.key == pygame.K_BACKSPACE:
                        particleamountinput = particleamountinput[:-1]
                    else:
                        particleamountinput += event.unicode
        #mass                


            if event.type == MOUSEBUTTONDOWN:
                if mass.collidepoint(event.pos):
                    active1 = not active1
                    massinput = ''
                else:
                    active1 = False
                colour1 = inputting if active1 else regular
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_RETURN:
                        print(massinput)
                        try:
                            int(massinput)
                            ClassB_mass = massinput
                            massinput = ''
                        except:
                            massinput = 'Try again'
                            print('Wrong')
                
                    elif event.key == pygame.K_BACKSPACE:
                        massinput = massinput[:-1]
                    else:
                        massinput += event.unicode

            #radius
            if event.type == MOUSEBUTTONDOWN:
                if radius.collidepoint(event.pos):
                    active2 = not active2
                    radiusinput = ''
                else:
                    active2 = False
                colour2 = inputting if active2 else regular
            if event.type == pygame.KEYDOWN:
                if active2:
                    if event.key == pygame.K_RETURN:
                        print(radiusinput)
                        try:
                            int(radiusinput)
                            ClassB_radius = radiusinput
                            radiusinput = ''
                        except:
                            radiusinput = 'Try again'
                            print('Wrong')
                        
                    elif event.key == pygame.K_BACKSPACE:
                        radiusinput = radiusinput[:-1]
                    else:
                        radiusinput += event.unicode
             #volume
            if event.type == MOUSEBUTTONDOWN:
                if volume.collidepoint(event.pos):
                    active3 = not active3
                    volumeinput = ''
                else:
                    active3 = False
                colour3 = inputting if active3 else regular
            #Records user input 
            if event.type == pygame.KEYDOWN:
                if active3:
                    if event.key == pygame.K_RETURN:
                        print(volumeinput)
                        try:
                            int(volumeinput)
                            ClassB_volume = volumeinput
                            volumeinput = ''
                        except:
                            volumeinput = 'Try again'
                            print('Wrong')
                        
                    elif event.key == pygame.K_BACKSPACE:
                        volumeinput = volumeinput[:-1]
                    else:
                        volumeinput += event.unicode
            #Particle Colour input and button colour change
                        
            if event.type == MOUSEBUTTONDOWN:
                if Colour.collidepoint(event.pos):
                    active4 = not active4
                    Colourinput = ''
                else:
                    active4 = False
                colour4 = inputting if active4 else regular
            #Records user input 
            if event.type == pygame.KEYDOWN:
                if active4:
                    if event.key == pygame.K_RETURN:
                        Check = False
                        print(Colourinput)
                        for i in range(len(Colours)):
                            if ColoursStrings[i].lower() == str(Colourinput).lower():
                                ClassB_colour = Colours[i]
                                Check = True
                        if Check == False:
                            Colourinput = 'Try Again'
        
                    elif event.key == pygame.K_BACKSPACE:
                        Colourinput = Colourinput[:-1]
                    else:
                        Colourinput += event.unicode
            if ClassB_volume and ClassB_radius and ClassB_mass and ClassB_Amount and len(ClassB_colour)>0:
                Completedb = True

            if ClassA_volume and ClassA_radius and ClassA_mass and ClassA_Amount and len(ClassA_colour)>0:
                Completeda = True
                
                        
            if event.type == MOUSEBUTTONDOWN:
                if Finish.collidepoint(event.pos) and Completedb == True and Completeda == True:
                    Particlecreation()

                if Finish.collidepoint(event.pos) and Completedb == True and Completeda == False:
                    Classa()
                    
            

                
        inputsurface = maintext.render(particleamountinput, True, colour)
        inputsurface1 = maintext.render(massinput, True, colour1)
        inputsurface2 = maintext.render(radiusinput, True, colour2)
        inputsurface3 = maintext.render(volumeinput,True,colour3)
        inputsurface4 = maintext.render(Colourinput,True,colour4)
        
        width = max(500, inputsurface.get_width()+10)
        width1 = max(500, inputsurface1.get_width()+10)
        width2 = max(500, inputsurface2.get_width()+10)
        width3 = max(500, inputsurface3.get_width()+10)
        width4 = max(500, inputsurface4.get_width()+10)
        
        particleamount.w = width
        mass.w = width1
        radius.w = width2
        volume.w = width3
        Colour.w = width4
        
        
        screen.blit(inputsurface, (particleamount.x+5, particleamount.y+5))
        screen.blit(inputsurface1, (mass.x+5, mass.y+5))
        screen.blit(inputsurface2, (radius.x+5, radius.y+5))
        screen.blit(inputsurface3, (volume.x+5, volume.y+5))
        screen.blit(inputsurface4, (Colour.x+5, Colour.y+5))
        
        #Display the button has been presssed with a border
        pygame.draw.rect(screen, colour1, mass, 5)
        pygame.draw.rect(screen, colour, particleamount, 5)
        pygame.draw.rect(screen, colour2, radius, 5)
        pygame.draw.rect(screen,colour3, volume,5)
        pygame.draw.rect(screen,colour4,Colour,5)
        
        #Display text so user understands each button
        draw_text('Particle amount', maintext,White,screen,setbuttonx-180,setbuttony-330)
        draw_text('Class B', secondarytitle, Titlecolour, screen, 20,20)
        draw_text('Variables', Button , Black, screen, setbuttonx-120,setbuttony-430)
        draw_text('Mass',maintext,White,screen,setbuttonx-70,setbuttony-175)
        draw_text('Radius',maintext,White,screen,setbuttonx-60,setbuttony-10)
        draw_text('To Class A', maintext, Black,screen, x-300,20)
        draw_text('Volume', maintext, White,screen,setbuttonx-60,setbuttony+150)
        draw_text('Particle Colour', maintext,White,screen,setbuttonx-180,setbuttony+310)
        draw_text('Finish',maintext,Black,screen,setbuttonx+440,setbuttony+30)


        
            
            
        pygame.display.update()
        mainClock.tick(60)

    

#------Opening Window & Graphics------#
        
#Sets timer for framerate        
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

#setting window and name/icon
pygame.display.set_caption('MODELX')
Width,Height = (1600,920)
screen = pygame.display.set_mode((1600,920),0,32)
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

#setting font settings
font = pygame.font.SysFont(None, 200)
Button = pygame.font.SysFont(None,100)
maintext = pygame.font.SysFont(None,75)
secondarytitle = pygame.font.SysFont(None,150)
#used for setting the size/location of text and buttons
x, y = screen.get_size()
setbuttonx = x//2      #800
setbuttony = y//2      #450

# reusable function for text objects
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

Titlecolour = White
Textcolour = Black

# A variable to check for  status later
click = False

Titlecolour = White
Textcolour = Black
# Main Menu function that holds the buttons and page switching
def main_menu():
    global click
    while True:
         
        screen.fill(Black)
        draw_text('ModelX', font, Titlecolour, screen, 0, 0)
 
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_1 = pygame.Rect(setbuttonx-200, setbuttony-200, 400, 100)
        button_2 = pygame.Rect(setbuttonx-200, setbuttony, 400, 100)
        button_3 = pygame.Rect(setbuttonx-200, setbuttony+200, 400, 100)

        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
             if click:
                 load()
        if button_3.collidepoint((mx,my)):
            if click:
                quit()
       #Creates dimensions of buttons 
        pygame.draw.rect(screen, (255, 255, 255), button_1)
        pygame.draw.rect(screen, (255, 255, 255), button_2)
        pygame.draw.rect(screen, (255, 255, 255), button_3)
        
 
        #writing text on top of button
        draw_text('Play', Button, Textcolour, screen, setbuttonx-100, setbuttony-185)
        draw_text('Load', Button, (Textcolour), screen , setbuttonx-100,setbuttony+15)
        draw_text('Quit', Button, Textcolour, screen , setbuttonx-100,setbuttony+215)

        #Allows user to exit
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #quit program with escape key
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            #Checks for mouse inputs to run functions
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 

def game():
    global ClassA_volume
    global ClassA_mass
    global ClassA_Amount
    global ClassA_colour
    global ClassA_radius
    global ClassB_volume
    global ClassB_mass
    global ClassB_Amount
    global ClassB_radius
    global ClassB_colour
    running = True
    classA = pygame.Rect(setbuttonx-200,setbuttony-200,500,125)
    classB = pygame.Rect(setbuttonx-200,setbuttony+100,500,125)
    
    while running:
        screen.fill((0,0,0))       
        draw_text('Simulation', font, Titlecolour, screen, 0, 0)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if classA.collidepoint(event.pos):
                    ClassA_volume = ''
                    ClassA_mass = ''
                    ClassA_Amount = ''
                    ClassA_radius = ''
                    ClassA_colour = ''
                    Classa()
                if classB.collidepoint(event.pos):
                    ClassB_volume = ''
                    ClassB_mass = ''
                    ClassB_Amount = ''
                    ClassB_radius = ''
                    ClassB_colour = ''
                    Classb()
    
        #draws rectangles     
        pygame.draw.rect(screen,White,classA)
        pygame.draw.rect(screen,White,classB)
        #Draw text for buttons  
        draw_text('Class A', Button,Textcolour,screen,setbuttonx-75,setbuttony-175)
        draw_text('Class B', Button,Textcolour,screen,setbuttonx-75,setbuttony+125)
        pygame.display.update()
        mainClock.tick(60)


#Loads previous variables if saved
def load():
    global Particles
    #Reads the variables that were previously saved and loads them
    with open('Variables.pkl','rb') as pickle_file:
        Particles = pickle.load(pickle_file)
        Display()
#if quit button pressed program quits
def quit():
    pygame.quit()


    
main_menu()

