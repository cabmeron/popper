from pygame import sprite
from pygame import image
from pygame import error
from pygame import Rect, Surface, RLEACCEL

class SpriteSheet:

    def __init__(self, filename):
        """ Load Sheet """
        try:
            self.sheet = image.load(filename)
        except error as e:
            print(f'Unable to load sprite from: {filename}')
            raise SystemExit(e)
    
    def image_at(self, rectangle, colorkey = None):
        """ Load Image from a specific Rectangle"""
        rect = Rect(rectangle)
        image = Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)

        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        
        return image
    
    def images_at(self, rects, colorkey = None):
        """ Loads multple images from rect, returning as list"""
        return [self.image_at(rect, colorkey) for rect in rects]