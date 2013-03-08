import pygame
from pygame.locals import *

 
class Babytop:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
	self.cow = None
	self.allSprites = None
 
    def on_init(self):
        pygame.init()
	pygame.display.set_caption('Basic Pygame program')
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
	self.cow = Cow()
	self.allSprites = pygame.sprite.Group(cow)
        self._running = True
	''' Asuming your frames have a 16x16 size '''
	explosion_images = load_sliced_sprites(16, 16, 'explosions-sprite.png'
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
	background = pygame.Surface(_display_surf.get_size())
	background = background.convert()
	background.fill((250, 250, 250))

	# Display some text
	font = pygame.font.Font(None, 36)
	text = font.render("Hello There", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)

	# Display some sprites
	self.allSprites.clear(_display_surf, background)
	self.allSprites.update()
	self.allSprites.draw(_display_surf)

	# Blit everything to the _display_surf
	_display_surf.blit(background, (0, 0))
	pygame.display.flip()
        pass
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
	clock = pygame.time.Clock()
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            clock.tick(30)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    babytop = Babytop()
    babytop.on_execute()
