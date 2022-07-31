#!/usr/bin/env python3

from eye import *


# define SPEED    360
# define ASPEED    45
# define THRES    175

SPEED = 200  # Original value: 360
ASPEED = 100 # 45
THRES = 220  # Original value: 175


DISTANCE = 25 # Original value: 360
DEGREE_TO_TURN = 90

DEGREE_TO_CURVE = int(DEGREE_TO_TURN / 2)

global scared
scared=False

def turn_left():
    VWTurn(DEGREE_TO_TURN, ASPEED)  # turn
    VWWait()


def curve_left():
    VWCurve(DISTANCE, DEGREE_TO_CURVE, SPEED)  # curve turn like a car...
    VWWait()



def turn_right():
    VWTurn(-DEGREE_TO_TURN, ASPEED)  # turn
    VWWait()


def curve_right():
    VWCurve(DISTANCE, -DEGREE_TO_CURVE, SPEED)  # curve turn like a car... 
    VWWait()

def straight():
    VWStraight(DISTANCE, SPEED)  # go one step
    VWWait()


def follow_right_wall():  
    while True:
        global scared

        light= find_light()
        if light ==True:
            scared=True
            turn_left()
            turn_left()
            return follow_right_wall()

        
        if scared == True:
            if safe_place():
                scared=False
                return 
        
        front = int(PSDGet(PSD_FRONT) > THRES)
        left = int(PSDGet(PSD_LEFT) > THRES)
        right = int(PSDGet(PSD_RIGHT) > THRES)
        # Drive right when possible, if not straight, if not left, else turn 180
        # .....
        front_half =  int(PSDGet(PSD_FRONT) > THRES/2)
        left_half = int(PSDGet(PSD_LEFT) > THRES/2)
        right_half = int(PSDGet(PSD_RIGHT) > THRES/2)
        
        
        if right == 1:
            print("RIGHT is SAFE, now turning right\n")
            curve_right()
            
            if front == 1:
                print("FRONT is SAFE, now moving forward\n")
                straight()  # front is also safe, now move forward
                
        elif front == 1:
            print("RIGHT is NOT safe, checking front\n")
            print("FRONT is SAFE, now moving forward\n")
            straight()  # right NOT safe but front is safe, now move forward

        elif left == 1:
            print("RIGHT and FRONT are NOT safe, checking left\n")
            print("LEFT is SAFE, now turning left\n")
            turn_left()  # left side is safe, now turning left
            
            if front == 1:
                print("FRONT is SAFE, now moving forward\n")
                straight()  # front is also safe, now move forward
        elif right_half == 1:
            
            if front_half ==1:
                straight()
                curve_right()
                
        elif left_half ==1:
            
            if front_half ==1:
                straight()
                curve_left()
                
        else:
            print("LEFT, FRONT and RIGHT are NOT safe, turning back on the spot\n")
            turn_left()  # all are not safe, now turning around
            turn_left()  # to achieve 180 turn around

        if left_half ==0:
            curve_right()
        if right_half ==0:
            curve_left()
        if front_half ==0:
            turn_right()
            turn_right()    
            
        
    


def safe_place():
    
    true_left = int(PSDGet(PSD_LEFT) < 1.25*THRES)
    true_right =int(PSDGet(PSD_RIGHT) <1.25*THRES)
    true_front = int(PSDGet(PSD_FRONT) <1.25*THRES)
    print('true_left')
    print(true_left)
    print('true front')
    print(true_front)
    print('true right')
    print(true_right)
    if true_left ==1 and true_right ==1 and true_front ==1:
        turn_left()  # all are not safe, now turning around
        turn_left()  # to achieve 180 turn around 
        OSWait(5000)
        
        print('it is safe now')
        return True
    return False


def get_values(img):
    #return pixel values of the image
    values=[]
    for i in range(0, 3*QQVGA_PIXELS):#3 layers
        values.append(img[i])
    return values
       
        
def find_light():
    img = CAMGet()
    LCDImage(img)
    print('finding')
   
    values=get_values(img)

    
    
    light =False
    
    for i in range(QQVGA_PIXELS):
        if values[i] ==-1 and values[i+QQVGA_PIXELS] ==-1 and values[i+2*QQVGA_PIXELS] != -1  :  
            print('the value are')
            print(values[i])
            print(values[i+QQVGA_PIXELS])
            print(values[i+2*QQVGA_PIXELS])
            light=True
            break
    if light==True:
        print('Light existed')
        return True
    else:
        return False




LCDMenu("   ","   ","","END")

CAMInit(QQVGA)
k=0
max_range =15000

while k != KEY4:
    
    follow_right_wall()
    
    k = KEYRead()
    OSWait(3000)

