from pygame import * 
font.init()
font= font.Font(None,36)
window=display.set_mode((1000,700)) 
display.set_caption('тенис') 
clock=time.Clock() 
fon=transform.scale(image.load('fon.jpg'),(1000,700))
lose1=font.render('Проиграл игрок 1',True,(255,255,255))
lose2=font.render('Проиграл игрок 2',True,(255,255,255))
ballx = 6
bally = 6


class drg(sprite.Sprite):
    def __init__(self,hero_image,hero_x,hero_y,size_x,size_y,hero_speed):
        super().__init__()
        self.image=transform.scale(image.load(hero_image),(size_x,size_y))
        self.rect=self.image.get_rect()
        self.rect.x=hero_x
        self.rect.y=hero_y

        self.speed=hero_speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(drg):
    def control1(self):
        control = key.get_pressed()
        if control[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if control[K_s] and self.rect.y < 600:
            self.rect.y += self.speed
    def control2(self):
        control = key.get_pressed()
        if control[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if control[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed
game = True
Finish = False
clock = time.Clock()
pl1 = Player('rocet.png',20,300,20,100,15)
pl2 = Player('rocet.png',950,300,20,100,15)
ball= Player('ball.jpg',500,300,40,50,0)

while  game:
    for e in event.get():
        if e.type == QUIT:
            game = Fals
    if Finish !=True:
        window.blit(fon,(0,0))
        pl1.reset()
        pl2.reset()
        ball.reset()
        pl1.control1()
        pl2.control2()
        ball.rect.x +=ballx
        ball.rect.y -=bally
        if ball.rect.y <0 or ball.rect.y> 650:
            bally *= -1
        if ball.rect.x <0:
            Finish = True
            window.blit(lose1,(400,300))
        if ball.rect.x > 1000:
            Finish = True
            window.blit(lose2,(400,300))
        if sprite.collide_rect(pl1,ball) or sprite.collide_rect(pl2,ball):
            bally *= 1
            ballx *= -1
        display.update()
    clock.tick(60)
