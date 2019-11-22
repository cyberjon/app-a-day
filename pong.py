import simpleguitk as simplegui
import random

w,h =600, 400
tux_r =20
tux_w =8
pad_w=8
pad_r=80

def tux_spwan(right):
    global tux_pos, tux_vel
    tux_pos=[0,0]
    tux_vel =[0,0]
    tux_pos[0] =w/2
    tux_pos[1]= h/2

    if right:
        tux_vel[0] =random.randrange(2,4)
    else:
        tux_vel[0]= random.randrange(2,4)
    tux_vel[1] = random.randrange(1,3)


def start():
    global paddle_pos, paddle2_pos,paddel_vel,paddel2_vel
    global score1, score2

    tux_spwan(random.choice([True,False]))
    score,score2 =0,0
    paddel_vel,paddel2_vel =0,0
    paddle_pos,paddle2_pos = h/2,h/2


start()