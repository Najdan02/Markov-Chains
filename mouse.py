import pygame
from background import Background

class Mouse:
    def __init__(self, image_path, x, y, width, height, background):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.width = width
        self.height = height
        self.image_path = image_path
        self.x = x
        self.y = y
        self.position = True
        self.corection = 21.5
        self.position_x = 3
        self.position_y = 3
        background.calculate_probability(self)

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def move_left(self, background):
        self.state_left()
        labyrinth = background.get_labyrinth()
        if labyrinth[self.position_y][self.position_x -1] == 0 and background.get_switch():
            self.x = self.x - 133.3
            self.position_x = self.position_x - 2

    def move_right(self, background):
        self.state_right()
        labyrinth = background.get_labyrinth()
        if labyrinth[self.position_y][self.position_x + 1] == 0 and background.get_switch():
            self.x = self.x + 133.3
            self.position_x = self.position_x + 2

    def move_up(self, background):
        self.state_up()
        labyrinth = background.get_labyrinth()
        if labyrinth[self.position_y - 1][self.position_x] == 0 and background.get_switch():
            self.y = self.y - 133.3
            self.position_y = self.position_y - 2

    def move_down(self, background):
        self.state_down()
        labyrinth = background.get_labyrinth()
        if labyrinth[self.position_y + 1][self.position_x] == 0 and background.get_switch():
            self.y = self.y + 133.3
            self.position_y = self.position_y + 2

    def get_position_x(self):
        return self.position_x
    
    def get_position_y(self):
        return self.position_y
    
    def state_up(self):
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, 180)
        if self.position:
                self.x += self.corection
                self.position = not self.position

    def state_down(self):
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if not self.position:
                self.x -= self.corection
                self.position = not self.position

    def state_right(self):
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, 90)
        if self.position:
                self.x += self.corection
                self.position = not self.position

    def state_left(self):
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, 270)
        if not self.position:
                self.x -= self.corection
                self.position = not self.position