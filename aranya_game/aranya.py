import sys
import pygame
from settings import Settings


def run_game():
	# Initialize pygame, settings, and screen object.	
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Aranya")

	# Set the background color.
	bg_color = (0, 0, 230)

	# Start the main game loop
	while True:

		# Watch for keyboard and mouse
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# Redraw the screen during each pass through the loop.
		screen.fill(ai_settings.bg_color)

		# Make the most recently drawn screen visible
		pygame.display.flip()

run_game()