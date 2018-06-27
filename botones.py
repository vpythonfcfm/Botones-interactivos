from vpython import *
r=10
b=box(pos=vector(r,0,0),make_trail=True)
arrow(axis=vector(1,0,0),color=vector(1,0,0))
arrow(axis=vector(0,1,0),color=vector(0,1,0))
arrow(axis=vector(0,0,1),color=vector(0,0,1))
om=0.5

running = True


# función del botón de pausa
def Run(b):
    global running
    running = not running
    if running:
        b.text = "Pause"
    else:
        b.text = "Run"

# Creación del botón

button(text="Pause", pos=scene.title_anchor, bind=Run)

# ----------------- #

# función del botón velocidad

def setspeed(s):
    wt.text = '{:1.2f}'.format(s.value)
    
sl = slider(min=0.3, max=3, value=0.5, length=220, bind=setspeed, right=15)

wt = wtext(text='{:1.2f}'.format(sl.value))

scene.append_to_caption(' radianes/s\n')

scene.append_to_caption('       ')


t=100
dt=1/t
ang=0
while True:

    rate(t)
    if running:
        b.pos=vector(r*cos(ang),r*sin(ang),0)
        b.rotate(angle=sl.value*dt,axis=vector(0,0,1),origin=b.pos)
        ang=ang+sl.value*dt
