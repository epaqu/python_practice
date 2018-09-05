from cs1robots import *

#You can change map by modifying "maze1.wld" to other map name
load_world("worlds/maze2.wld")

################### DO NOT TOUCH ##############################
hubo = Robot(avenue=10,street=1,orientation = 'N')
ami = Robot(color="yellow",orientation = 'N')
###############################################################

hubo.set_trace("green")
ami.set_trace("red")

def turn_right(Robot):
    Robot.turn_left()
    Robot.turn_left()
    Robot.turn_left()
    
def turn_around(Robot):
    Robot.turn_left()
    Robot.turn_left()  
        
def ami_movement():
    while not ami.on_beeper():
        if ami.front_is_clear():
            ami.move()
        else:
            turn_around(ami)
            while not ami.left_is_clear():
                ami.move()
            ami.turn_left()
            ami.move()
            turn_right(ami)
            while ami.front_is_clear():
                ami.move()
            turn_around(ami)

def hubo_movement():
    while not hubo.on_beeper():
        if hubo.front_is_clear():
            hubo.move()
        else:
            turn_around(hubo)
            while not hubo.right_is_clear():
                hubo.move()
            turn_right(hubo)
            hubo.move()
            hubo.turn_left()
            while hubo.front_is_clear():
                hubo.move()
            turn_around(hubo)
ami_movement()
hubo_movement()