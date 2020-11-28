class Bullet(pygame.sprite.Sprite):
    def _init_(self, tower):
        pygame.sprite.Sprite._init_(self)
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.x = tower.centerx
        self.rect.y = tower.centery
        self.v_speed = 0
        self.h_speed = 0
        self.speed = 10
        self.tower = tower

    def update(self):
        if self.tower == tower_archer:
            self.image = bullet_archer
        elif self.tower == tower_fire:
            self.image = bullet_fire
        elif self.tower == tower_freeze:
            self.image = bullet_freeze
        self.rect.y += self.v_speed
        self.rect.x += self.h_speed

class Tower(object):

    def shoot(self, enemy.x, enemy.y):
        bullet = Bullet(tower)
        rel_x, rel_y = enemy.x - bullet.rect.x, enemy.y - bullet.rect.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        bullet.image = pygame.transform.rotate(bullet.image, int(angle))
        lendth_vector = math.sqrt(rel_x*2 + rel_y*2)
            if lendth_vector != 0:
                norm_vector_x, norm_vector_y = rel_x / lendth_vector, rel_y / lendth_vector
                bullet.h_speed = int(norm_vector_x * bullet.speed)
                bullet.v_speed = int(norm_vector_y * bullet.speed)
                