import pygame

LIGHT_BLUE = (0, 204, 204)
BLUE = (0, 0, 204)
VERY_LIGHT_BLUE = (204, 255, 255)
BLACK = (0, 0, 0)

class Background:
    def __init__(self, width, height):
        self.surface = pygame.Surface((width, height))
        self.width = width
        self.height = height
        self.labyrinth_width = 400
        self.labyrinth_height = 400
        self.labyrinth_x = 50
        self.labyrinth_y = 200
        self.labyrinth_border_thickness = 5
        self.switch = False
        self.k = 0
        self.probability = "1"
        self.font_size = 40
        self.text = f"Verovatnoće prelaska: {self.probability}"
        self.font = pygame.font.SysFont('Arial', self.font_size)
        self.labyrinth = [
            [1, 1, 1, 1, 1, 1, 1],  
            [1, 0, 0, 0, 0, 0, 1],  
            [1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]   
        ]
        self.draw()

    def draw(self):
        self.surface.fill(LIGHT_BLUE)
        pygame.draw.rect(self.surface, BLACK, (self.labyrinth_x, self.labyrinth_y, self.labyrinth_width, self.labyrinth_height), self.labyrinth_border_thickness)
        pygame.draw.line(self.surface, BLACK, (0, 0), (self.width,0), self.labyrinth_border_thickness)
        pygame.draw.line(self.surface, BLACK, (0, 0), (0,self.height), self.labyrinth_border_thickness)
        pygame.draw.line(self.surface, BLACK, (self.width, 0), (self.width, self.height), self.labyrinth_border_thickness)
        pygame.draw.line(self.surface, BLACK, (0, self.height), (self.width, self.height), self.labyrinth_border_thickness)
        pygame.draw.rect(self.surface, VERY_LIGHT_BLUE, (self.labyrinth_x, self.labyrinth_y // 2 - self.font_size - 5, self.labyrinth_width, self.labyrinth_y // 2))
        pygame.draw.rect(self.surface, BLACK, (self.labyrinth_x, self.labyrinth_y // 2 - self.font_size - 5, self.labyrinth_width, self.labyrinth_y // 2), self.labyrinth_border_thickness)
        self.walls()

    def display(self, screen):
        screen.blit(self.surface, (0, 0))

    def walls(self):
        self.switch = not self.switch
        pygame.draw.rect(self.surface, BLUE,(self.labyrinth_x + self.labyrinth_border_thickness, self.labyrinth_y + self.labyrinth_border_thickness, self.labyrinth_width - 2 * self.labyrinth_border_thickness, self.labyrinth_height - 2 * self.labyrinth_border_thickness))
        if self.switch:
            pygame.draw.line(self.surface, BLACK, (50, 333.3), (212.3,333.3), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (287.6, 333.3), (345.6,333.3), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (420, 333.3), (449,333.3), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (50, 466.6), (79,466.6), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (154.3, 466.6), (212.3,466.6), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (287.6, 466.6), (345.6,466.6), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (420, 466.6), (449,466.6), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (183.3, 200), (183.3,229), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (183.3, 304.3), (183.3,362.3), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (183.3, 437.6), (183.3,599), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (316.6, 200), (316.6,229), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (316.6, 304.3), (316.6,362.3), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (316.6, 437.6), (316.6,599), self.labyrinth_border_thickness)
        else:
            pygame.draw.line(self.surface, BLACK, (183.3, 200), (183.3,599), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (316.6, 200), (316.6,599), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (50, 333.3), (449,333.3), self.labyrinth_border_thickness)
            pygame.draw.line(self.surface, BLACK, (50, 466.6), (449,466.6), self.labyrinth_border_thickness)

    def get_labyrinth(self):
        return self.labyrinth
    
    def get_switch(self):
        return self.switch

    def calculate_probability(self, player):
        if self.switch:
            self.k = 0
            position_x = player.get_position_x()
            position_y = player.get_position_y()
            if self.labyrinth[position_y][position_x - 1] == 0:
                self.k += 1
            if self.labyrinth[position_y][position_x + 1] == 0:
                self.k += 1
            if self.labyrinth[position_y - 1][position_x] == 0:
                self.k += 1
            if self.labyrinth[position_y + 1][position_x] == 0:
                self.k += 1
            self.probability = f"1/{self.k + 1}"
            self.text = f"Verovatnoće prelaska: {self.probability}"
        else:
            self.k = 0
            self.probability = "1"
            self.text = f"Verovatnoća prelaska: {self.probability}"

    def write_text(self, screen):
        rendered_text1 = self.font.render(f"k: {self.k}", True, BLACK)
        rendered_text2 = self.font.render(self.text, True, BLACK)
        text_rect1 = rendered_text1.get_rect()
        text_rect2 = rendered_text2.get_rect()
        text_rect1.center = (self.width // 2, self.labyrinth_y // 2 - self.font_size // 2)
        text_rect2.center = (self.width // 2, self.labyrinth_y // 2 + self.font_size // 2)
        screen.blit(rendered_text1, text_rect1)
        screen.blit(rendered_text2, text_rect2)

            
            

