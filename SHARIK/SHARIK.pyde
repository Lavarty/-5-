x=300
naprovlenie="right"
x1=100
def setup():
    size(600,600)
    
def draw():
    global x,naprovlenie,x1
    clear()

    fill(random(0,255),random(0,255),random(0,255))
    ellipse(300,x,x1,x1)
    
    x1+=1
    
    
    if x==600:
        naprovlenie="left"
    
    if x==0:
        naprovlenie="right"

    if mousePressed and (mouseButton == RIGHT):
        x=x+1
    
    if mousePressed and (mouseButton == LEFT):
        x=x-1
        
    if x1==200:
        x1+=1
    else:
        x1-=1

    
    
