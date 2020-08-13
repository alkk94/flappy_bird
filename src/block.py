class Block:
    def __init__(self, image):
        self.image = image

    def draw(self, screen, position):
        if self.image:
            screen.blit(self.image, position)
