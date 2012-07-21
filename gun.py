import pygame, math

class Bullet:
    position = pygame.Rect(0, 0, 0, 0)
    velocity = pygame.Rect(0, 0, 0, 0)
    
    alive = 1
    
    def __init__(self, px, py, vx, vy):
        self.position = pygame.Rect(px, py, 0, 0)
        self.velocity = pygame.Rect(vx, vy, 0, 0)
    
    def update(self, dt):
        self.position = self.position.move(float(self.velocity.x) * dt, float(self.velocity.y) * dt)
        
        self.alive = self.position.x < 810 and self.position.x > -10 and self.position.y > -10 and self.position.y < 610
        
    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color("white"), [self.position.x, self.position.y], 3)

class Gun:
    bullets = []
    position = pygame.Rect(0, 0, 0, 0)
    bulletSpeed = 1000
    moveSpeed = 250.0
    img = pygame.image.load("life.png")
    
    def update(self, dt):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:      
            self.position = self.position.move(-self.moveSpeed * dt, 0)
        if keystate[pygame.K_d]:
            self.position = self.position.move(self.moveSpeed * dt, 0)
        if keystate[pygame.K_w]:      
            self.position = self.position.move(0, -self.moveSpeed * dt)
        if keystate[pygame.K_s]:
            self.position = self.position.move(0, self.moveSpeed * dt)
    
        for i in range(len(self.bullets)):
            self.bullets[i].update(dt)
    
    def draw(self, surface):
        surface.blit(self.img, self.position)
        
        removeList = []
        
        for i in range(len(self.bullets)):
            if self.bullets[i].alive:
                self.bullets[i].draw(surface)
            else:
                removeList.append(self.bullets[i])
                
        for i in range(len(removeList)):
            self.bullets.remove(removeList[i])
            
    def fire(self):
        mousePos = pygame.mouse.get_pos()
        
        dx = mousePos[0] - self.position.x
        dy = mousePos[1] - self.position.y
        
        if math.fabs(dx) > 0 or math.fabs(dy) > 0:
            magnitude = math.sqrt((dx*dx) + (dy*dy))
                
            dx_norm = dx / magnitude
            dy_norm = dy / magnitude
            
            self.bullets.append(Bullet(self.position.x, self.position.y, dx_norm * self.bulletSpeed, dy_norm * self.bulletSpeed))