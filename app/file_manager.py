from PIL import Image
import numpy as np
import os
import pandas as pd

DEFAULT_DIR = 'images'

class FileManager():
    def __init__(self, file_directory = DEFAULT_DIR) -> None:    
        self.load_image_files(file_directory)
    
    
    def load_image_files(self, directory:str) -> None:
        """Sets FileManager.files to list of image files found in given directory"""
        files = []
        for file in os.listdir(directory):
            file_path = os.sep.join([directory, file])
            try:
                Image.open(file_path).verify()
                files.append(file_path)
            except Exception:
                pass
        self.files = files
        
        
    def get_image_dimensions(self, filepath:str) -> tuple:
        """Returns tuple with width and height from given image filepath"""
        img = Image.open(filepath)
        return (img.size)
        
        
    def is_image_portrait(self, filepath:str) -> bool:
        """Returns boolean value indicating whether image height is greater than image width"""
        img = Image.open(filepath)
        return img.size[0] < img.size[1]
        
        
    def is_image_square(self, filepath:str) -> bool:
        """Returns boolean value indicating whether image height is equal to the image width"""
        img = Image.open(filepath)
        return img.size[0] == img.size[1]
        
        
    def is_image_transparent(self, filepath:str) -> bool:
        """Returns boolean value indicating whether image contains any pixels with alpha value"""
        img = Image.open(filepath)
        channels = img.split()
        if len(channels) < 4:
            return False
        
        alpha = channels[3]
        alpha_sum = (255 - np.asarray(alpha)).sum()
        return alpha_sum > 0
        
        
    def get_average_color(self, filepath:str) -> tuple:
        """Returns averaged RGB values from given image filepath"""
        img = Image.open(filepath)
        pixels = np.asarray(img.getdata()).astype(float)    
        return tuple(pixels.mean(axis=0))
        

    def get_file_size(self, filepath:str) -> int:
        """Returns filesize in bytes from given filepath"""
        return os.path.getsize(filepath)

    def as_dataframe(self):
        df = pd.DataFrame()
        df['name'] = [f.split(os.sep)[-1] for f in self.files]
        dimensions = [self.get_image_dimensions(f) for f in self.files]
        df['width'] = [d[0] for d in dimensions]
        df['height'] = [d[1] for d in dimensions]
        df['portrait'] = [self.is_image_portrait(f) for f in self.files]
        df['square'] = [self.is_image_square(f) for f in self.files]
        df['landscape'] = ~df[['portrait','square']].any(axis=1)
        df['transparent'] = [self.is_image_transparent(f) for f in self.files]
        df['opaque'] = ~df['transparent']
        rgb = [self.get_average_color(f) for f in self.files]
        df['red'] = [v[0] for v in rgb]      
        df['green'] = [v[1] for v in rgb]
        df['blue'] = [v[2] for v in rgb]
        df['bytes'] = [self.get_file_size(f) for f in self.files]
        return df
        
        # DF_COLUMNS = ['file_name', 'width', 'height', 'portrait', 'square', 'transparency','r' ,'g' ,'b' ,'bytes']