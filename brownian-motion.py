import random
import pygame
import pymunk

# Define particle class
class Particle:
    def __init__(self, x, y, r, mass):
        self.body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, r))
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, r)
        self.shape.elasticity = 1.0
        self.shape.friction = 0.5

# Define simulation parameters
WIDTH, HEIGHT = 800, 600
PARTICLE_RADIUS = 10
PARTICLE_MASS = 1
PARTICLE_COUNT = 12
MAX_FORCE = 1
MAX_SPEED = 500
DT = 20.0 / 60.0







# Initialize simulation
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
space = pymunk.Space()
space.gravity = 0, 0



particles = []
for i in range(PARTICLE_COUNT):
    x = random.randint(PARTICLE_RADIUS, WIDTH - PARTICLE_RADIUS)
    y = random.randint(PARTICLE_RADIUS, HEIGHT - PARTICLE_RADIUS)
    particle = Particle(x, y, PARTICLE_RADIUS, PARTICLE_MASS)
    particles.append(particle)
    space.add(particle.body, particle.shape)

# Define simulation loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rectangle = pymunk.Poly(space.static_body, [(100, 100), (200, 100), (20, 150), (10, 150)])
    space.add(rectangle)
    # Apply random forces to particles
    for particle in particles:
        fx = random.uniform(-MAX_FORCE, MAX_FORCE)
        fy = random.uniform(-MAX_FORCE, MAX_FORCE)
        particle.body.apply_force_at_local_point((fx, fy))

    # Update physics and positions
    space.step(DT)
    for particle in particles:
        particle_pos = particle.body.position
        particle.shape.center = particle_pos

    # Draw particles
    screen.fill((255, 255, 255))
    for particle in particles:
        x, y = particle.body.position
        pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), PARTICLE_RADIUS)

    # Update display
    pygame.display.update()
    clock.tick(60)

# Clean up simulation
pygame.quit()
