import os 
import pygame
from pygame.locals import *
from gameobjects.vector2 import Vector2
from random import randint

RESOLUTION = (300, 600)

pygame.init()
screen 				= pygame.display.set_mode(RESOLUTION)
background 		= pygame.Surface(RESOLUTION)
textbox   		= pygame.Surface(300,300)
default_font 	= pygame.font.get_default_font()
font 					= pygame.font.SysFont(default_font, 20, False)	

background.fill((255,255,255))
screen.blit(background, (0, 0))
		
def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                  ((screen.get_width() / 2) - 100,
                  (screen.get_height() / 2) - 10,
                  200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                  ((screen.get_width() / 2) - 102,
                  (screen.get_height() / 2) - 12,
                  204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")

class AnimatedSprite(pygame.sprite.Sprite):
		def __init__(self, images, sound_fx, fps = 10):
			pygame.sprite.Sprite.__init__(self)
			self._images 			= images
      self._soundfx     = pygame.mixer.Sound(sound_fx)

			# Track the time we started, and the time between updates.
			# Then we can figure out when we have to switch the image.
			self._start 			= pygame.time.get_ticks()
			self._delay 			= 1000 / fps
			self._last_update = 0
			self._frame 			= 0
			self.image 				= self._images[self._frame]
			# Defining a default location on screen for our sprite
			w, h 							= RESOLUTION
			self.location 		= (randint(0,w),randint(0,h))
			
		def update(self, t):
			# Note that this doesn't work if it's been more that self._delay
			# time between calls to update(); we only update the image once
			# then, but it really should be updated twice.
			if t - self._last_update > self._delay:
				self._frame += 1
				# Animation Finished, choosing a new location
				if self._frame >= len(self._images):
					self._frame = 0
					w, h 							= RESOLUTION
					x, y							= self.image.get_size()
					self.location 		= (randint(0+x,w-x),randint(0+y,h-y))
										
				self.image = self._images[self._frame]
				self._last_update = t
            
		def render(self, screen):

			self.update(pygame.time.get_ticks())
      self._sound_fx.play()
			screen.blit(self.image, self.location)

def load_sliced_sprites(w, h, filename):
    '''
    Specs :
    	Master can be any height.
    	Sprites frames width must be the same width
    	Master width must be len(frames)*frame.width
    '''
    images = []
    master_image = pygame.image.load(os.path.join('resouces', filename)).convert_alpha()

    master_width, master_height = master_image.get_size()
    for i in xrange(int(master_width/w)):
    	images.append(master_image.subsurface((i*w,0,w,h)))
    return images



def run():	
		explosion_images 	= load_sliced_sprites(20, 20, 'boom.png', 'boom.wav')
		clock 						= pygame.time.Clock()
		
		sprites						= []
		sprites.append(AnimatedSprite(explosion_images, 15))
   # Loading and playing background music:

   pygame.mixer.music.load(os.path.join('resouces', 'music.mp3')
   pygame.mixer.music.play(-1, 0.0)

   # ...some more of your code goes here...

   pygame.mixer.music.stop()
		while True:
				for event in pygame.event.get():
						if event.type == QUIT:
                pygame.mixer.music.stop()
								return
						
						if event.type == MOUSEBUTTONDOWN:
								explosion = AnimatedSprite(explosion_images, 15)
								explosion.location = event.pos
								sprites.append(explosion)
				
				screen.blit(background, (0, 0))
				time_passed = clock.tick(30)

				for sprite in sprites:
					sprite.render(screen)
					
				instructions = font.render("Click to add explosions", True, (0,0,0))
				screen.blit(instructions, (0, 0))
				pygame.display.update()


if __name__ == "__main__":
				run()
