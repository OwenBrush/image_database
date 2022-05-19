from PIL import Image
import numpy as np
from os import listdir

class FileManager():
    
    def get_average_color(self, filepath:str) -> tuple:
        """Returns averaged RGB values from given image filepath
        """
        img = Image.open(filepath)
        pixels = np.asarray(img.getdata()).astype(float)    
        return tuple(pixels.mean(axis=0))

