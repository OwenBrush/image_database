from PIL import Image
import numpy as np

class FileManager():
    
    def get_average_color(self, filepath):
        """Returns averaged RGB values from given image filepath
        """
        img = Image.open(filepath)
        pixels = np.asarray(img.getdata()).astype(float)    
        return pixels.mean(axis=0)
        
        
        
