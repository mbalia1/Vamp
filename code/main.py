from settings import *
from player import Player
from sprites import *
from random import randint
from pytmx.util_pygame import load_pygame
from groups import AllSprites




class Game():
    def __init__(self):
        #init
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Vampire Survivor')
        self.clock = pygame.time.Clock()
        self.running = True

        #groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

        #sprites
        #self.player = Player((400, 300), self.all_sprites, self.collision_sprites)
        #create random rectangles derived from the sprite class and place them at random points on the

    def setup(self):
        map = load_pygame(join("../", "data", "maps", "world.tmx"))

        for col in map.get_layer_by_name("Collisions"):
            CollisionSprite((col.x, col.y), pygame.Surface((col.width, col.height)),self.collision_sprites)

        for x,y, image in map.get_layer_by_name("Ground").tiles():
            Sprite((x * TILE_SIZE,y *TILE_SIZE), image, self.all_sprites)

        for obj in map.get_layer_by_name("Objects"):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in map.get_layer_by_name("Entities"):
            if obj.name == "Player":
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)


    def run(self):
        while self.running:
            #dt
            dt = self.clock.tick() / 1000.0

            #event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            #update

            #draw
            self.display_surface.fill(("black"))
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()
        pygame.quit()

game = Game()
game.run()



