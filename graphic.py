import pygame

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 2000
screen_height = 2000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Image Sprite")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load the pixel image
pixel_car0 = pygame.image.load(r"C:\Users\SSD\Downloads\race_car_0.png")
pixel_car1 = pygame.image.load(r"C:\Users\SSD\Downloads\race_car_1.jpg")
pixel_car2 = pygame.image.load(r"C:\Users\SSD\Downloads\race_car_2.png")
pixel_car3 = pygame.image.load(r"C:\Users\SSD\Downloads\race_car_3.png")
pixel_highway_image = pygame.image.load(r"C:\Users\SSD\Downloads\pixelroad.PNG")


# Define the Sprite class for the car0
class Car0(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pixel_car0
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 4, screen_height // 2)
        self.rect.clamp_ip(screen.get_rect())  # Ensure car stays within screen boundaries

    def update(self):
        # Implement movement or any other logic here
        pass


# Define the Sprite class for the car
class Car1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pixel_car1
        self.rect = self.image.get_rect()
        self.rect.center = (2 * screen_width // 4, screen_height // 2)  # Adjust position as needed
        self.rect.clamp_ip(screen.get_rect())  # Ensure car stays within screen boundaries

    def update(self):
        # Implement movement or any other logic here
        pass


class Car2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pixel_car2
        self.rect = self.image.get_rect()
        self.rect.center = (3 * screen_width // 4, screen_height // 2)  # Adjust position as needed
        self.rect.clamp_ip(screen.get_rect())  # Ensure car stays within screen boundaries

    def update(self):
        # Implement movement or any other logic here
        pass


class Car3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pixel_car3
        self.rect = self.image.get_rect()
        self.rect.center = (4 * screen_width // 5, screen_height // 2)  # Adjust position as needed
        self.rect.clamp_ip(screen.get_rect())  # Ensure car stays within screen boundaries

    def update(self):
        # Implement movement or any other logic here
        pass


# Define the Sprite class for the highway
class Highway(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pixel_highway_image
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.rect.clamp_ip(screen.get_rect())  # Ensure car stays within screen boundaries

    def update(self):
        # Implement any necessary updates here
        pass

# Create instances of all car, and highway sprites
car0 = Car0()
car1 = Car1()
car2 = Car2()
car3 = Car3()
highway = Highway()

# Create sprite groups
all_sprites = pygame.sprite.Group()
vehicles = pygame.sprite.Group()  # Combine cars into one group
highways = pygame.sprite.Group()


# Add sprites to respective groups
vehicles.add(*[car0, car1, car2, car3])  # Add all car to the vehicles group
all_sprites.add(car0, car1, car2, car3, highway)
highways.add(highway)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Render
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Update
    all_sprites.update()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
