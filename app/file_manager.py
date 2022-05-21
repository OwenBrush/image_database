from PIL import Image
import numpy as np
import os
import pathlib

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
        
