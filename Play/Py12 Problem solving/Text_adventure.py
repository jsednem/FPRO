"""


Write a Python text-based game that, depending on the users' choices, branches into different scenarios. Think of the old Dungeons and Dragons game, but digital. Or the old Zork games. I know, I know, who cares about text-based games when modern game graphics are bordering on reality. Well, not everyone fits the same mold!

The only oddity, on developing a text-based game dynamic, will be how the user answers the questions. If a particular answer is given, the user will be branched to a separate section.

Write a script using input() and print() for I/O.

All the questions have only 3 options (A,B,C,a,b,c), except for ones that you need to pick up something with a yes or no answer (Y,N,y,n).

Below is a flowchart to make the branching a little easier to understand.

Now you have all the texts and options according to the flow:
Module 	Text 	Action 	Text
Intro 	After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you. 	Question 	
i1 	A. Grab a nearby rock and throw it at the orc 	goto rock 	
i2 	B. Lie down and wait to be mauled 	Game Over 	Welp, that was quick. You died!
i3 	C. Run 	goto run 	
Rock 	The orc is stunned, but regains control. He begins running towards you again. 	Question 	
k1 	A. Run 	goto run 	
k2 	B. Throw another rock 	Game Over 	The rock flew well over the orcs head. You missed. You died!
k3 	C. Run towards a nearby cave 	goto cave 	
CAVE (Y/N) 	Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N? 	Question 	
CAVE 	What do you do next? 	Question 	
c1 	A. Hide in silence 	Game Over 	I think orcs can see very well in the dark, right? You died!
c2 	B. Fight 	WITH SWORD: Victory 	As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!
		WITHOUT SWORD: Game Over 	You're defenseless. You died!
c3 	C. Run 	goto run 	The orc turns around and sees you running.
RUN 	You run as quickly as possible. 	Question 	
r1 	A. Hide behind boulder 	Game Over 	You're easily spotted. You died!
r2 	B. Trapped, so you fight 	Game Over 	You're no match for an orc. You died!
r3 	C. Run towards an abandoned town 	goto town 	
TOWN (Y/N) 	You notice a purple flower near your foot. Do you pick it up? Y/N 	Question 	
Y 	You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived! 	Victory 	
N 	Maybe you should have picked up the flower. You died! 	Game Over 	
Adapted from: Derek Shidler blog 
"""

def intro():
    print('After a drunken night out with friends, you awaken in a thick,',
          'dank forest. A slobbering orc is running towards you.')
    print('A. Grab a nearby rock and throw it at the orc')
    print('B. Lie down and wait to be mauled')
    print('C. Run')
    nex = input()
    if nex.lower() == 'a':
        option_rock()
    elif nex.lower() == 'b':
        print('Welp, that was quick. You died!')
    elif nex.lower() == 'c':
        option_run()
        
    
def option_rock():
    print('The orc is stunned, but regains control. He begins running towards you again.')
    print('A. Run')
    print('B. Throw another rock')
    print('C. Run towards a nearby cave')
    nex = input()
    if nex.lower() == 'a':
        option_run()
    elif nex.lower() == 'b':
        print('The rock flew well over the orcs head. You missed. You died!')
    elif nex.lower() == 'c':
        option_cave()
    

def option_cave():
    print('Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?')
    sword = input()
    print('What do you do next?')
    print('A. Hide in silence')
    print('B. Fight')
    print('C. Run')
    nex = input()
    if nex.lower() == 'a':
        print('I think orcs can see very well in the dark, right? You died!')
    elif nex.lower() == 'b':
        if sword.lower() == 'y':
            print('As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!')
        else:
            print("You're defenseless. You died!")
    elif nex.lower() == 'c':
        print('The orc turns around and sees you running.')
        option_run()
    
        
def option_run():
    print('You run as quickly as possible.')
    print('A. Hide behind boulder')
    print('B. Trapped, so you fight')
    print('C. Run towards an abandoned town')
    nex = input()
    if nex.lower() == 'a':
        print("You're easily spotted. You died!")
    elif nex.lower() == 'b':
        print("You're no match for an orc. You died!")
    elif nex.lower() == 'c':
        option_town()
    
    
def option_town():
    print('You notice a purple flower near your foot. Do you pick it up? Y/N')
    flower = input()
    if flower.lower() == 'y':
        print('You quickly hold out the purple flower. The orc was looking',
              'for love. This got weird, but you survived!')
    else:
        print('Maybe you should have picked up the flower. You died!')
   
intro()
