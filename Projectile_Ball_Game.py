import pygame
import math
import random

pygame.init()
win=pygame.display.set_mode((800,600))
pygame.display.set_caption("MINI GAME")

walkRight = [pygame.image.load('R0.png'),pygame.image.load('R1.png'),
             pygame.image.load('R2.png'),pygame.image.load('R3.png'),
             pygame.image.load('R4.png'),pygame.image.load('R5.png'),
             pygame.image.load('R6.png'),pygame.image.load('R7.png'),
             pygame.image.load('R8.png'),pygame.image.load('R9.png'),
             pygame.image.load('R10.png')]
walkLeft = [pygame.image.load('L0.png'),pygame.image.load('L1.png'),
            pygame.image.load('L2.png'),pygame.image.load('L3.png'),
            pygame.image.load('L4.png'),pygame.image.load('L5.png'),
            pygame.image.load('L6.png'),pygame.image.load('L7.png'),
            pygame.image.load('L8.png'),pygame.image.load('L9.png'),
            pygame.image.load('L10.png')]
bg=[pygame.image.load('mainMenu.jpg'),pygame.image.load('board.png'),
    pygame.image.load('gothic.jpg'),pygame.image.load('cemetery.jpg'),
    pygame.image.load('apocalipsis.png'),pygame.image.load('gothic.jpg'),
    pygame.image.load('cemetery.jpg'),pygame.image.load('apocalipsis.png'),
    pygame.image.load('gothic.jpg'),pygame.image.load('cemetery.jpg'),
    pygame.image.load('apocalipsis.png')]
heart=pygame.image.load('heart.png')
# arrow=pygame.image.load('Arrow.png')

setting=pygame.image.load('setting.png')
global aud
aud=True
audio=pygame.image.load('audio.png')
noAudio=pygame.image.load('no_audio.png')
global mus
mus=True
music=pygame.image.load('music.png')
noMusic=pygame.image.load('no_music.png')

icon=pygame.image.load('game.jpg')
pygame.display.set_icon(icon)
lvlButton=[pygame.image.load('L1B.png'),pygame.image.load('L1A.png'),
           pygame.image.load('L2B.png'),pygame.image.load('L2A.png'),
           pygame.image.load('L3B.png'),pygame.image.load('L3A.png')]

funcButton=[pygame.image.load('menuB4.png'),pygame.image.load('menuAFT.png'),
            pygame.image.load('pauseB4.png'),pygame.image.load('pauseAft.png'),
            pygame.image.load('contiB4.png'),pygame.image.load('contiAft.png'),
            pygame.image.load('refreshB4.png'),pygame.image.load('refreshAft.png')]

clock=pygame.time.Clock()

bulletSound=pygame.mixer.Sound('bullet.wav')
hitSound=pygame.mixer.Sound('hit.wav')
owSound=pygame.mixer.Sound('ouch.wav')
winSound=pygame.mixer.music.load('won.mp3')

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velocity=5
        self.left=False
        self.right=False
        self.walkCount=0
        self.standing=True
        self.hitbox=(self.x+45,self.y+20,40,106)

    def draw(self,win):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            posM = pygame.mouse.get_pos()
            if posM[0] < self.x:
                self.left = True
                self.right = False
            else:
                self.right = True
                self.left = False

            if self.left:
                win.blit(walkLeft[10], (self.x, self.y))
            else:
                win.blit(walkRight[10],(self.x,self.y))
            self.hitbox = (self.x+45 , self.y+20, 40, 106)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        # resetting player position
        self.x=10
        self.y=400
        self.walkCount=0
        font3=pygame.font.SysFont('comicsans',100)
        text=font3.render('-2',1,(255,0,0))
        win.blit(text,((800/2)-(text.get_width()/2),200))
        pygame.display.update()
        i=0
        while i<300:
            pygame.time.delay(5)
            i+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i=301
                    pygame.quit()

class projectile(object):
    def __init__(self,x,y,radius,color):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.visible=False

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        if self.visible==True:
            pygame.draw.line(win, (255, 255, 255), line[0], line[1])

    @staticmethod
    def ballPath(startx, starty, power, angle, time):
        velocity_x = math.cos(angle) * power
        velocity_y = math.sin(angle) * power

        distance_x = velocity_x * time
        distance_y = (velocity_y * time) + ((-4.9 * (time) ** 2) / 2)

        newx = round(distance_x + startx)
        newy = round(starty - distance_y)

        t_max=velocity_y/4.9
        if time>t_max:
            if bullet.y - bullet.radius < man.hitbox[1] + man.hitbox[3] and bullet.y +bullet.radius > man.hitbox[1]:
                if bullet.x + bullet.radius > man.hitbox[0] and bullet.x - bullet.radius < man.hitbox[0] + man.hitbox[2]:
                    Sound(owSound)
                    man.hit()
                    global score
                    global lf
                    score -= 2
                    lf -= 1
                    newy=605

        return (newx, newy)

class enemy(object):

    def __init__(self, x, y, width, height, end, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        # This will define where our enemy starts and finishes their path.
        self.walkCount = 0
        self.velocity = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health=10
        self.visible=True
        self.moving=False
        self.type=type

    def draw(self,win):
        if self.visible:
            if self.type == 1:
                self.walkRight = [pygame.image.load('ZR1.png'), pygame.image.load('ZR2.png'),
                                  pygame.image.load('ZR3.png'), pygame.image.load('ZR4.png'),
                                  pygame.image.load('ZR5.png'), pygame.image.load('ZR6.png')]
                self.walkLeft = [pygame.image.load('ZL1.png'), pygame.image.load('ZL2.png'),
                                 pygame.image.load('ZL3.png'), pygame.image.load('ZL4.png'),
                                 pygame.image.load('ZL5.png'), pygame.image.load('ZL6.png')]
                self.stand = pygame.image.load('ZLS.png')

            elif self.type == 2:
                self.walkRight = [pygame.image.load('ZR1_2.png'), pygame.image.load('ZR2_2.png'),
                                  pygame.image.load('ZR3_2.png'), pygame.image.load('ZR4_2.png'),
                                  pygame.image.load('ZR5_2.png'), pygame.image.load('ZR6_2.png')]
                self.walkLeft = [pygame.image.load('ZL1_2.png'), pygame.image.load('ZL2_2.png'),
                                 pygame.image.load('ZL3_2.png'), pygame.image.load('ZL4_2.png'),
                                 pygame.image.load('ZL5_2.png'), pygame.image.load('ZL6_2.png')]
                self.stand = pygame.image.load('ZLS_2.png')

            elif self.type == 3:
                self.walkRight = [pygame.image.load('ZR1_3.png'), pygame.image.load('ZR2_3.png'),
                                  pygame.image.load('ZR3_3.png'), pygame.image.load('ZR4_3.png'),
                                  pygame.image.load('ZR5_3.png'), pygame.image.load('ZR6_3.png')]
                self.walkLeft = [pygame.image.load('ZL1_3.png'), pygame.image.load('ZL2_3.png'),
                                 pygame.image.load('ZL3_3.png'), pygame.image.load('ZL4_3.png'),
                                 pygame.image.load('ZL5_3.png'), pygame.image.load('ZL6_3.png')]
                self.stand = pygame.image.load('ZLS_3.png')

            if self.moving:
                self.move()

                if self.walkCount+1>=18:
                    self.walkCount=0
                if self.velocity>0:
                    win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                    self.walkCount+=1
                else:
                    win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.velocity>0:
                    win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                elif self.velocity<0:
                    win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                else:
                    win.blit(self.stand,(self.x,self.y))

            pygame.draw.rect(win, (255, 0, 0),(self.hitbox[0],self.hitbox[1]-20,50,10))
            pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 50-(5*(10-self.health)), 10))
            self.hitbox = (self.x , self.y , 64, 105)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.velocity>0:
            if self.x+ self.velocity<self.path[1]:
                self.x+=self.velocity
            else:
                self.velocity=self.velocity*-1
                self.walkCount=0
        else:
            if self.x-self.velocity>self.path[0]:
                self.x+=self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walkCount = 0


    def hit(self):
        if self.health>0:
            if self.type==1:
                self.health-=5
            elif self.type==2:
                self.health-=2
            else:
                self.health-=1
        else:
            self.visible=False

def displayHeart(x):
    if x>-1:
        for i in range (x):
            win.blit(heart,(630+40*i,10))

def pp(x):
    global pause
    global score
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # home
    if 80 > mouse[0] > 10 and 70 > mouse[1] > 10:
        win.blit(funcButton[1], (10, 10))
        if click[0] == 1:
            score=0
            chooseLVL()
    else:
        win.blit(funcButton[0], (10, 10))

    # pause
    if 160 > mouse[0] > 90 and 70 > mouse[1] > 10:
        win.blit(funcButton[3], (90, 10))
        if click[0] == 1:
            pause=True
    else:
        win.blit(funcButton[2], (90, 10))

    # refresh
    if 250 > mouse[0] > 170 and 70 > mouse[1] > 10:
        win.blit(funcButton[7], (170, 10))
        if click[0] == 1:
            score=0
            gameLoop(x-1)
    else:
        win.blit(funcButton[6], (170, 10))

def paused():
    font8 = pygame.font.SysFont('forte', 150, False, True)
    text = font8.render('pause', 1, (0, 0, 255))
    win.blit(text, ((800 / 2) - (text.get_width() / 2), (300 / 2) - (text.get_height() / 2)))

    global pause
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause=False
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 595 > mouse[0] > 200 and 400 > mouse[1] > 250:
            win.blit(funcButton[5], (200, 250))
            if click[0] == 1:
                pause=False
        else:
            win.blit(funcButton[4], (200, 250))

        onOff()

        pygame.display.update()
        clock.tick(15)

def redrawWindow(i):
    win.blit(bg[i], (0, 0))
    pp(i)
    onOff()
    global score
    global lf
    # name,size,bold,italian
    font = pygame.font.SysFont('comicsans', 30, True)
    text=font.render('Score : '+str(score),1,(0,0,0))
    win.blit(text,(390,10))
    life = font.render('Life ', 1, (255, 0, 0))
    win.blit(life, (560, 10))
    displayHeart(lf)
    man.draw(win)
    goblin.draw(win)
    bullet.draw(win)
    pygame.display.update()

def findAngle(position):
    sx=bullet.x
    sy=bullet.y

    try:
        angle=math.atan((sy-position[1])/(sx-position[0]))
    except:
        angle=math.pi/2

    if position[1]<sy and position[0]>sx:
        angle=abs(angle)
    elif position[1]<sy and position[0]<sx:
        angle=math.pi-angle
    elif position[1]>sy and position[0]<sx:
        angle=math.pi+abs(angle)
    elif position[1]>sy and position[0]>sx:
        angle=(math.pi*2)-angle

    return angle

man = player(0, 400, 128, 128)
goblin=enemy(300,420,64,105,520,1)
bullet = projectile(32, 605, 5, (255, 0, 0))

x = 0
y = 0
time = 0
power = 0
angle = 0
score=0
acc=[0,0]
arrows=[]

def quitGame():
    pygame.quit()
    quit()

def Sound(x):
    global aud
    if aud:
        x.play()
    else:
        x.stop()

def loseGame(x):
    pygame.mixer.music.load('fail.mp3')
    pygame.mixer.music.play()

    global score

    lose=True
    while lose:
        goblin.moving=False
        font4 = pygame.font.SysFont('forte', 100, True,True)
        text = font4.render('GAME OVER', 1, (255, 0, 0))
        win.blit(text, ((800/2) - (text.get_width() / 2), 150))
        font5 = pygame.font.SysFont('Times New Roman', 60, True, True)
        text_1 = font5.render('Play Again?', 1, (0, 0, 0))
        win.blit(text_1, ((800/2)- (text_1.get_width() / 2), 250))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 280 > mouse[0] > 200 and 390 > mouse[1] > 320:
            text_yes = font5.render('Yes', 1, (255, 154, 0))
            if click[0]==1:
                lose=False
                score=0
                gameLoop(x)
        else:
            text_yes = font5.render('Yes', 1, (0, 0, 0))

        if 575 > mouse[0] > 500 and 390> mouse[1] > 320:
            text_no = font5.render('No', 1, (255, 154, 0))
            if click[0]==1:
                lose=False
                score=0
                chooseLVL()
        else:
            text_no = font5.render('No', 1, (0, 0, 0))

        win.blit(text_yes, (200, 320))
        win.blit(text_no, (500, 320))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lose=False
                pygame.quit()
    clock.tick(15)

def wonGame(x):
    pygame.mixer.music.load('won.mp3')
    pygame.mixer.music.play()

    global score

    won=True
    while won:
        font6 = pygame.font.SysFont('forte', 120, True, True)
        text = font6.render('LEVEL PASS', 1, (0, 255, 0))
        win.blit(text, ((800 / 2) - (text.get_width() / 2), 150))
        font7 = pygame.font.SysFont('courier new', 60, True, True)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+1<10:
            if 800 > mouse[0] > 320 and 370 > mouse[1] > 300:
                txt = font7.render("Next Level >>", 1, (255, 154, 0))
                if click[0] == 1:
                    won=False
                    gameLoop(x + 1)

            else:
                txt = font7.render("Next Level >>", 1, (247, 95, 28))
            win.blit(txt, (320, 300))

        else:
            font5 = pygame.font.SysFont('Times New Roman', 60, True, True)
            if 375 > mouse[0] > 100 and 390 > mouse[1] > 320:
                text_play = font5.render('Play Again', 1, (255, 154, 0))
                if click[0] == 1:
                    won = False
                    score=0
                    chooseLVL()
            else:
                text_play = font5.render('Play Again', 1, (0, 0, 0))

            if 615 > mouse[0] > 500 and 390 > mouse[1] > 320:
                text_exit = font5.render('Quit', 1, (255, 0, 0))
                if click[0] == 1:
                    won = False
                    quitGame()
            else:
                text_exit = font5.render('Quit', 1, (0, 0, 0))
            win.blit(text_play, (100, 320))
            win.blit(text_exit, (500, 320))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                won=False
                pygame.quit()

    clock.tick(15)

def gameLoop(i):
    # main loop start here
    man.x=0
    goblin.x=400

    global line
    global score
    global lf
    global pause
    shoot = False
    walk = True
    lf = 3
    goblin.health = 10
    goblin.visible=True
    rand = pygame.USEREVENT + 1
    chg=False
    pause=False

    if i==1:
        goblin.moving=False
        goblin.velocity=0
        goblin.type=1

        pygame.mixer.music.load('level1.mp3')
        pygame.mixer.music.play(-1)

    elif i==2:
        goblin.moving = True
        goblin.velocity = 3
        goblin.type=1

        pygame.mixer.music.load('level2.mp3')
        pygame.mixer.music.play(-1)

    elif i==3:
        goblin.moving = False
        goblin.velocity=0
        goblin.type=1
        pygame.time.set_timer(rand,2000)
        chg=True

        pygame.mixer.music.load('level3.mp3')
        pygame.mixer.music.play(-1)

    elif i==4:
        goblin.moving=False
        goblin.velocity=0
        goblin.type=2

        pygame.mixer.music.load('level1.mp3')
        pygame.mixer.music.play(-1)

    elif i==5:
        goblin.moving = True
        goblin.velocity = 5
        goblin.type=2

        pygame.mixer.music.load('level2.mp3')
        pygame.mixer.music.play(-1)

    elif i==6:
        goblin.moving = False
        goblin.velocity=0
        goblin.type=2
        pygame.time.set_timer(rand,1500)
        chg=True

        pygame.mixer.music.load('level3.mp3')
        pygame.mixer.music.play(-1)

    elif i==7:
        goblin.moving=False
        goblin.velocity=0
        goblin.type=3

        pygame.mixer.music.load('level1.mp3')
        pygame.mixer.music.play(-1)

    elif i==8:
        goblin.moving = True
        goblin.velocity = 10
        goblin.type=3

        pygame.mixer.music.load('level2.mp3')
        pygame.mixer.music.play(-1)

    elif i==9:
        goblin.moving = False
        goblin.velocity=0
        goblin.type=3
        pygame.time.set_timer(rand,1000)
        chg=True

        pygame.mixer.music.load('level3.mp3')
        pygame.mixer.music.play(-1)

    run=True
    while run:
        clock.tick(30)

        if pause:
            paused()

        if lf<0:
            loseGame(i)

        if goblin.visible== True:
            if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] +man.hitbox[3] > goblin.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                    Sound(owSound)
                    man.hit()
                    goblin.x=400
                    score -= 2
                    lf-=1
        else:
            wonGame(i)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                if shoot == False:
                    if bullet.visible:
                        shoot=True
                        Sound(bulletSound)
                        bullet.visible = False
                    walk=True
                    x = bullet.x
                    y = bullet.y
                    time = 0
                    power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][0]) ** 2) / 8
                    angle = findAngle(position)
                    # acc[1]+=1
                    # arrows.append([math.atan2(position[1]-bullet.y,position[0]-bullet.x),bullet.x,bullet.y])
            if event.type == rand:
                if chg:
                    goblin.x=random.randint(0,700)

        if bullet.y-bullet.radius<goblin.hitbox[1]+goblin.hitbox[3] and bullet.y+bullet.radius>goblin.hitbox[1]:
            if bullet.x+bullet.radius>goblin.hitbox[0] and bullet.x-bullet.radius<goblin.hitbox[0]+goblin.hitbox[2]:
                Sound(hitSound)
                goblin.hit()
                score+=1
                bullet.y=605

        keys=pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            bullet.visible=True
            walk=False
            man.standing = True

        if walk:
            if keys[pygame.K_LEFT] and man.x>man.velocity:
                man.x-=man.velocity
                man.left=True
                man.right=False
                man.standing=False
            elif keys[pygame.K_RIGHT] and man.x<720-man.width-man.velocity:
                man.x+=man.velocity
                man.right=True
                man.left=False
                man.standing=False
            else:
                man.standing=True
                man.walkCount=0

        if shoot:
            # index=0
            if bullet.y<600-bullet.radius:
                # slow down speed, chg time to lower value
                time+=0.5
                po=projectile.ballPath(x,y,power,angle,time)
                bullet.x=po[0]
                if bullet.x>800-bullet.radius or bullet.x<bullet.radius:
                    bullet.x=-50
                bullet.y=po[1]

            else:
                shoot=False
                bullet.visible=False
                # arrows.pop(index)
            # index+=1
                # make bullet out of screen
                bullet.y=605

        position = pygame.mouse.get_pos()
        line = [(bullet.x, bullet.y), (position)]

        if bullet.visible:
            if man.left:
                bullet.x=round(man.x + 75)
                bullet.y=round(man.y + 100)
            else:
                bullet.x = round(man.x+52)
                bullet.y = round(man.y +100)

        redrawWindow(i+1)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h))
        # click[0]==left click of mouse
        if click[0]==1 and action!=None:
            action()
    else:
        pygame.draw.rect(win, ic,(x,y,w,h))
    # name,size,bold,italian
    font2=pygame.font.SysFont("freesans",40,True,True)
    txt=font2.render(msg,1,(0,0,0))
    win.blit(txt,(350,(y+(h/3))))

def onOff():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global aud
    global mus
    if 795 > mouse[0] > 735 and 595 > mouse[1] > 355:
        pygame.draw.circle(win,(0,255,255), (765,565), 30)
        pygame.draw.rect(win, (0, 255, 255), (735, 435, 60, 130))
        pygame.draw.circle(win, (0, 255, 255), (765, 435), 30)

        pygame.draw.circle(win, (200, 0, 200), (767, 505), 25)
        pygame.draw.circle(win, (200, 0, 200), (767, 440), 25)

        if 792 > mouse[0] > 742 and 530 > mouse[1] > 480:
            pygame.draw.circle(win, (255, 0, 255), (767, 505), 25)
            if click[0] == 1:
                if aud:
                    aud=False
                else:
                    aud=True

        if 792 > mouse[0] > 742 and 465 > mouse[1] > 415:
            pygame.draw.circle(win, (255, 0, 255), (767, 440), 25)
            if click[0] == 1:
                if mus:
                    mus=False
                else:
                    mus=True

        if aud:
            win.blit(audio, (747, 485))
        else:
            win.blit(noAudio, (747, 485))

        if mus:
            win.blit(music, (747, 422))
            pygame.mixer.music.unpause()
        else:
            win.blit(noMusic, (749, 422))
            pygame.mixer.music.pause()

    else:
        pygame.draw.circle(win, (0,200,200), (765,565),30)
    win.blit(setting, (735, 540))

def choose(x,y,before,after,num=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # 150 by 76
    if x + 150 > mouse[0] > x and y + 76 > mouse[1] > y:
        win.blit(after,(x,y))
        # click[0]==left click of mouse
        if click[0] == 1 and num!=None:
            gameLoop(num)
    else:
        win.blit(before,(x,y))

def chooseLVL():
    pygame.mixer.music.load('store.mp3')
    pygame.mixer.music.play(-1)
    lvl=True
    while lvl:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lvl=False
                pygame.quit()
                quit()
        win.fill((0,255,125))
        win.blit(bg[1], (30, 10))

        font9= pygame.font.SysFont('Algerian', 40, True, True)
        text = font9.render('easy', 1, (0, 0, 0))
        win.blit(text, ((110,60)))

        choose(110, 110, lvlButton[0], lvlButton[1], 1)
        choose(310, 110, lvlButton[2], lvlButton[3], 2)
        choose(510, 110, lvlButton[4], lvlButton[5], 3)

        textN = font9.render('normal', 1, (0, 0, 0))
        win.blit(textN, ((110, 195)))
        choose(110, 245, lvlButton[0], lvlButton[1], 4)
        choose(310, 245, lvlButton[2], lvlButton[3], 5)
        choose(510, 245, lvlButton[4], lvlButton[5], 6)

        textH = font9.render('hard', 1, (0, 0, 0))
        win.blit(textH, ((110, 330)))
        choose(110, 380, lvlButton[0], lvlButton[1], 7)
        choose(310, 380, lvlButton[2], lvlButton[3], 8)
        choose(510, 380, lvlButton[4], lvlButton[5], 9)


        font3 = pygame.font.SysFont("mono", 40, True, True)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 180 > mouse[0] > 10 and 600 > mouse[1] > 550:
            txt = font3.render("<< BACK", 1, (255, 154, 0))
            if click[0] == 1:
                game()
        else:
            txt = font3.render("<< BACK", 1, (247, 95, 28))

        win.blit(txt, (10, 550))
        onOff()

        pygame.display.update()
    clock.tick(15)

def game():
    pygame.mixer.music.load('main.mp3')
    pygame.mixer.music.play(-1)
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                intro=False
                pygame.quit()
                quit()

        win.blit(bg[0],(0,0))
        font1= pygame.font.SysFont("Arial", 100, True, True)
        title=font1.render('ZOMBIE HUNTER',1,(0,0,0))
        win.blit(title,(50,50))

        # green, bright green
        button("PLAY",150,250,500,100,(0,200,0),(0,255,0),chooseLVL)
        # red, bright red
        button("QUIT",150,400,500,100,(200,0,0),(255,0,0),quitGame)

        onOff()

        pygame.display.update()
    clock.tick(15)


game()
pygame.quit()
