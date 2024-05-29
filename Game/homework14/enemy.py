import random
import arcade
class Enemy (arcade.Sprite) :
    def __init__(self,w,h) :
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0,w)
        self.center_y = h + 24
        self.width = 48
        self.height = 48
        self.angle = 180
        self.speed = 4
    
    def move (self, increase_speed) :
        
        self.center_y -= (self.speed * (1 + increase_speed))
        