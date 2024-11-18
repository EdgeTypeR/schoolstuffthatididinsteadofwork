import pygame
import numpy as np
import math
import time

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinny Donut")

# Colors
BLACK = (0, 0, 0)

# Donut parameters
A, B = 0, 0  # Rotation angles
R1, R2 = 10, 20  # Radii of the torus
K1, K2 = 100, 50  # Projection constants

def render_donut(A, B):
    screen.fill(BLACK)  # Clear screen

    cos_A = math.cos(A)
    sin_A = math.sin(A)
    cos_B = math.cos(B)
    sin_B = math.sin(B)

    for theta in np.arange(0, 2 * math.pi, 0.07):  # Circle around donut shape
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)

        for phi in np.arange(0, 2 * math.pi, 0.02):  # Circle around tube
            cos_phi = math.cos(phi)
            sin_phi = math.sin(phi)

            # 3D coordinates
            circle_x = R2 + R1 * cos_theta
            circle_y = R1 * sin_theta

            x = circle_x * (cos_B * cos_phi + sin_A * sin_B * sin_phi) - circle_y * cos_A * sin_B
            y = circle_x * (sin_B * cos_phi - sin_A * cos_B * sin_phi) + circle_y * cos_A * cos_B
            z = K2 + cos_A * circle_x * sin_phi + circle_y * sin_A
            ooz = 1 / z

            # Projected 2D coordinates
            xp = int(WIDTH / 2 + K1 * ooz * x)
            yp = int(HEIGHT / 2 - K1 * ooz * y)

            # Brightness (intensity based on distance)
            luminance_index = int(8 * ((cos_phi * cos_theta * sin_B - cos_A * cos_theta * sin_phi - sin_A * sin_theta + cos_B * (cos_A * sin_theta - cos_theta * sin_A * sin_phi)) + 1))
            luminance_index = max(0, min(11, luminance_index))  # Clamp between 0 and 11

            # Plot donut point with safe RGB values
            red = min(255, luminance_index * 20)
            green = min(255, luminance_index * 15)
            blue = min(255, luminance_index * 25)
            color = (red, green, blue)
            
            # Ensure the coordinates are within screen bounds
            if 0 <= xp < WIDTH and 0 <= yp < HEIGHT:
                screen.set_at((xp, yp), color)

    pygame.display.flip()  # Update display

# Main loop
running = True
clock = pygame.time.Clock()

try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update rotation angles
        A += 0.04
        B += 0.03

        # Render the spinning donut
        render_donut(A, B)

        # Cap the frame rate
        clock.tick(30)

finally:
    pygame.quit()




