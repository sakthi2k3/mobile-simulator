import pgzrun
from random import randint as rd
WIDTH = 500
HEIGHT = 400

Cowboy = Actor("char1")
Cowboy.frame = 1
Cowboy.pos = (WIDTH//2,HEIGHT//2)
Cowboy_speed = 4

bullets_right = []
bullets_left = []
bullet_speed = 6

goblins_left = []
goblins_right = []
goblin_speed = 2
goblin_count = 1

kill_pt =[]
coin_pt = []

Border = Actor("wall")

Numbers = {"1":Actor("no1"),"2":Actor("no2"),"3":Actor("no3"),"4":Actor("no4"),"5":Actor("no5")}
for i in range(1,6):
    Numbers["{}".format(i)].pos = (WIDTH//2,HEIGHT//2)


Coin = Actor("coin")
Coin.x = rd(-900, -300)
Coin.y = 50
Pos_x = rd(40,WIDTH-50)
Pos_y = rd(40,HEIGHT-50)


Org = [(222, 179, 115),(237, 182, 100),(230, 161, 96),(237, 143, 71),(224, 111, 58)]
Score = 0
Level = 1
Best = 0

Right = True
Game_over = True
Done = True

Title = Actor("title")
Title.pos = (WIDTH//2 , 100)
Enter = Actor("enter")
Enter.pos = (WIDTH//2 , 250)
Over = Actor("over")
Over.pos = (WIDTH//2 , 100)
Sc = Actor("score")
Sc.pos = (WIDTH - 85, 45)
Ins = Actor("inst")
Ins.pos = (WIDTH//2 , 370)
Bs = Actor("best")
Bs.pos = (WIDTH - 85, 64)

def draw():
    global goblins_left,goblins_right
    if Game_over:
        goblins_left.clear()
        goblins_right.clear()
        screen.clear()
        screen.blit("screen",(0,0))
        Title.draw()
        Enter.draw()
        Ins.draw()
        Sc.pos = (WIDTH - 85, 45)
        Bs.pos = (WIDTH - 85, 64)

    elif not Game_over and Done:
        screen.fill(Org[Level - 1])
        Border.draw()
        display()
        Sc.draw()
        Bs.draw()
        Numbers["{}".format(Level)].draw()
        Cowboy.draw()
        Coin.draw()
        draw_bullet(bullets_right)
        draw_bullet(bullets_left)
        for pt in kill_pt:
            pt.draw()
        for pt in coin_pt:
            pt.draw()
        for goblin in goblins_left:
            goblin.draw()
        for goblin in goblins_right:
            goblin.draw()


def update():
    if not Game_over and Done:
        get_best()
        cowboy_movement()
        boundary_cowboy()
        move_bullet_right()
        move_bullet_left()
        cowboy_collision()
        kill()
        check_level()
        check_goblin_count()
        coin_collision()
        if goblin_count > 1:
            coin_move()

        for goblin in goblins_left:
            animate_goblin_left(goblin)
            goblin_movement_left(goblin)
            goblin_collision_left(goblin)
        for goblin in goblins_right:
            animate_goblin_right(goblin)
            goblin_movement_right(goblin)
            goblin_collision_right(goblin)

        while len(goblins_left) < goblin_count:
            create_goblin_left()
        while len(goblins_right) < goblin_count:
            create_goblin_right()


def animate_cowboy_left():
    if True:
        Cowboy.image = "char{}".format(Cowboy.frame)
    Cowboy.frame += 1
    if Cowboy.frame > 50:
        Cowboy.frame = 1

def animate_cowboy_right():
    if True:
        Cowboy.image = "ichar{}".format(Cowboy.frame)
    Cowboy.frame += 1
    if Cowboy.frame > 50:
        Cowboy.frame = 1

def cowboy_movement():
    global Right
    if keyboard.right:
        animate_cowboy_right()
        Cowboy.x += Cowboy_speed
        Right = True

    elif keyboard.left:
        animate_cowboy_left()
        Cowboy.x -= Cowboy_speed
        Right = False

    elif keyboard.down:
        if Right:
            animate_cowboy_right()
        else:
            animate_cowboy_left()
        Cowboy.y += Cowboy_speed

    elif keyboard.up:
        if Right:
            animate_cowboy_right()
        else:
            animate_cowboy_left()
        Cowboy.y -= Cowboy_speed

    else:
        if Right:
            Cowboy.image = "ichar{}".format(1)
        if not Right:
            Cowboy.image = "char{}".format(1)

def boundary_cowboy():

    if Cowboy.right > WIDTH:
        Cowboy.right = WIDTH
    elif Cowboy.left < 0:
        Cowboy.left = 0
    elif Cowboy.top < 30:
        Cowboy.top = 30
    elif Cowboy.bottom > HEIGHT - 30:
        Cowboy.bottom = HEIGHT - 30

def cowboy_collision():
    global Done
    for goblin in goblins_right:
        if goblin.colliderect(Cowboy):
            Done = False
            gameover_screen()
    for goblin in goblins_left:
        if goblin.colliderect(Cowboy):
            Done = False
            gameover_screen()


def on_key_down(key):
    global Game_over,Done
    if key == key.SPACE and Done and not Game_over:
        if Right:
            sounds.gun.play()
            create_bullet(bullets_right)
        else:
            sounds.gun.play()
            create_bullet(bullets_left)
    if key == key.RETURN:
        if Done:
            Game_over = False
        if not Done:
            Done = True
            Game_over = True

def create_bullet(bullets):
    bullet = Actor("bullet")
    if not Right:
        bullet.x = Cowboy.x - 13
        bullet.y = Cowboy.y + 4
    else:
        bullet.x = Cowboy.x + 15
        bullet.y = Cowboy.y + 4
    bullets.append(bullet)

def draw_bullet(bullets):
    for bullet in bullets:
        bullet.draw()

def move_bullet_right():
    for bullet in bullets_right:
        bullet.x += bullet_speed
def move_bullet_left():
    for bullet in bullets_left:
        bullet.x -= bullet_speed


def animate_goblin_left(enemy):
    if True:
        enemy.image = "mon{}".format(enemy.frame)
    enemy.frame += 1
    if enemy.frame > 45:
        enemy.frame = 1
def animate_goblin_right(enemy):
    if True:
        enemy.image = "imon{}".format(enemy.frame)
    enemy.frame += 1
    if enemy.frame > 45:
        enemy.frame = 1

def goblin_movement_left(goblin):
    goblin.x += goblin_speed
def goblin_movement_right(goblin):
    goblin.x -= goblin_speed

def create_goblin_left():
    if Level == 4:
        pos = -300
    elif Level == 5:
        pos = -200
    else:
        pos = -500
    goblin = Actor("mon1")
    goblin.y = rd(40,HEIGHT - 40)
    goblin.x = rd(pos,-50)
    goblin.frame = 1
    goblins_left.append(goblin)
def create_goblin_right():
    if Level == 4:
        pos = 300
    elif Level == 5:
        pos = 200
    else:
        pos = 500
    goblin = Actor("imon1")
    goblin.y = rd(40,HEIGHT - 40)
    goblin.x = rd(WIDTH + 50,WIDTH+pos)
    goblin.frame = 1
    goblins_right.append(goblin)

def goblin_collision_right(goblin):
    if goblin.left < -50:
        goblins_right.remove(goblin)
def goblin_collision_left(goblin):
    if goblin.right > WIDTH + 50:
        goblins_left.remove(goblin)

def check_goblin_count():
    global goblin_count
    if Level == 2:
        goblin_count = 2
    if Level == 3:
        goblin_count = 3
    if Level == 4:
        goblin_count = 4
    if Level == 5:
        goblin_count = 5
    if Score > 100:
        goblin_count = 7


def kill():
    global Score
    for bullet in bullets_right:
        for enemy in goblins_left:
            if bullet.colliderect(enemy):
                create_killpt(enemy)
                clock.schedule(remove_pt, 1.0)
                goblins_left.remove(enemy)
                bullets_right.remove(bullet)
                Score += 1
    for bullet in bullets_left:
        for enemy in goblins_left:
            if bullet.colliderect(enemy):
                create_killpt(enemy)
                clock.schedule(remove_pt, 1.0)
                goblins_left.remove(enemy)
                bullets_left.remove(bullet)
                Score += 1
    for bullet in bullets_right:
        for enemy in goblins_right:
            if bullet.colliderect(enemy):
                create_killpt(enemy)
                clock.schedule(remove_pt, 1.0)
                goblins_right.remove(enemy)
                bullets_right.remove(bullet)
                Score += 1
    for bullet in bullets_left:
        for enemy in goblins_right:
            if bullet.colliderect(enemy):
                create_killpt(enemy)
                clock.schedule(remove_pt, 1.0)
                goblins_right.remove(enemy)
                bullets_left.remove(bullet)
                Score += 1

def coin_move():
    if Coin.left > - 50:
        Coin.pos = (Pos_x,Pos_y)
    else:
        Coin.x += 2

def coin_collision():
    global Pos_y,Pos_x,Score
    if Cowboy.colliderect(Coin):
        create_coinpt(Coin)
        sounds.coin.play()
        clock.schedule(remove_cpt, 1.0)
        Coin.x = rd(-900, -300)
        Coin.y = 50
        Pos_x = rd(40, WIDTH - 50)
        Pos_y = rd(40, HEIGHT - 50)
        Score += 3

def create_killpt(enemy):
    pt = Actor("kpt")
    pt.pos = enemy.pos
    kill_pt.append(pt)

def remove_pt():
    try:
        for pt in kill_pt:
            kill_pt.remove(pt)
    except RecursionError:
        pass

def create_coinpt(coin):
    pt = Actor("cpt")
    pt.pos = coin.pos
    coin_pt.append(pt)

def remove_cpt():
    try:
        for pt in coin_pt:
            coin_pt.remove(pt)
    except RecursionError:
        pass

def check_level():
    global Level,Score
    if 10 < Score < 25:
        Level = 2
    if 25 < Score < 45:
        Level = 3
    if 45 < Score < 60:
        Level = 4
    if Score > 60:
        Level = 5

def gameover_screen():
    global bullets_right,bullets_left,goblin_speed,goblin_count,goblins_left,goblins_right,kill_pt,coin_pt,Score,Level,Right

    bullets_right = []
    bullets_left = []

    goblins_left.clear()
    goblins_right.clear()

    kill_pt = []
    coin_pt = []

    Level = 1

    update_best()

    goblin_speed = 2
    goblin_count = 1

    Cowboy.pos = (WIDTH // 2, HEIGHT // 2)
    screen.clear()
    screen.fill(Org[Level - 1])
    Border.draw()

    Over.draw()
    Sc.pos = (WIDTH // 2 - 20, 200)
    Sc.draw()
    Enter.draw()

    screen.draw.text(str(Score), (WIDTH //2 + 18 , 191) ,fontsize=24, color= "black" )
    Right = False
    Coin.x = rd(-900, -300)
    Score = 0
    sounds.over.play()

def get_best():
    global Best
    f = open("HighScore.txt","r")
    Best = f.read()
    f.close()

def update_best():
    if int(Score) > int(Best):
        fp = open("HighScore.txt","w")
        fp.write(str(Score))
        fp.close()

def display():
    global Score
    screen.draw.text(str(Score), (WIDTH - 45, 37), fontsize=24, color= "black")
    screen.draw.text(str(Best), (WIDTH - 45, 56), fontsize=24, color="black")



pgzrun.go()

