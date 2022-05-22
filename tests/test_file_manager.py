from app.file_manager import FileManager
import pandas as pd
import os

IMAGE_DIR = 'images'
RED_IMAGE = 'images/red_64_96.png'
WHITE_IMAGE = 'images/white_9_1000.png'
BLACK_WHITE_IMAGE = 'images/black_white_2_1.png'
BLUE_SQUARE_IMAGE = 'images/blue_600_600.png'
TRANSPARENT_IMAGE = 'images/green_transparent_800_600.png'
OPAQUE_IMAGE = 'images/yellow_opaque_alpha_800_600.png'
TEXT_FILE = 'images/not_an_image.txt'
DF_COLUMNS = ['name', 'width', 'height', 'portrait', 'square', 'landscape', 'transparent','red' ,'green' ,'blue' ,'bytes']

def test_load_image_files():
    """
    GIVEN FileManager is instantiated
    WHEN the load_file method is called with an image directory containing non image files
    THEN the resulting file list only contains paths to valid images
    """
    fm = FileManager()
    fm.load_image_files(IMAGE_DIR)
    assert not TEXT_FILE in fm.files
    assert RED_IMAGE in fm.files
    
    
def test_get_average_color():
    """
    GIVEN FileManager is instantiated
    WHEN the get_image_color method is called with a valid filename
    THEN The averaged RGB value of the file is retured
    """
    fm = FileManager()
    
    red = fm.get_average_color(RED_IMAGE)
    white = fm.get_average_color(WHITE_IMAGE)
    gray = fm.get_average_color(BLACK_WHITE_IMAGE)
    
    assert red == (255, 0, 0)
    assert white == (255, 255, 255)
    assert gray == (127.5, 127.5, 127.5)
    
    
def test_get_image_dimensions():
    """
    GIVEN FileManager is instantiated
    WHEN the get_image_dimensions method is called with a valid filename
    THEN the width and height of the image are returned as a tuple
    """
    fm = FileManager()
    assert fm.get_image_dimensions(RED_IMAGE) == (64, 96)
    assert fm.get_image_dimensions(BLACK_WHITE_IMAGE) == (2, 1)


def test_is_image_portrait():
    """
    GIVEN FileManager is instantiated
    WHEN the is_image_portrait method is called with a valid filename
    THEN the a boolean value is returned indicating whether the image height is greater than the image width
    """
    fm = FileManager()
    assert fm.is_image_portrait(RED_IMAGE) == True
    assert fm.is_image_portrait(BLACK_WHITE_IMAGE) == False
    assert fm.is_image_portrait(BLUE_SQUARE_IMAGE) == False
    

def test_is_image_square():
    """
    GIVEN FileManager is instantiated
    WHEN the is_image_square method is called with a valid filename
    THEN the a boolean value is returned indicating whether the image height is equal to the image width
    """
    fm = FileManager()
    assert fm.is_image_square(RED_IMAGE) == False
    assert fm.is_image_square(BLACK_WHITE_IMAGE) == False
    assert fm.is_image_square(BLUE_SQUARE_IMAGE) == True


def test_is_image_transparent():
    """
    GIVEN FileManager is instantiated
    WHEN the is_image_transparent method is called with a valid filename
    THEN the a boolean value is returned indicating whether the image contains any pixels with an alpha value
    """
    fm = FileManager()
    assert fm.is_image_transparent(TRANSPARENT_IMAGE) == True
    assert fm.is_image_transparent(RED_IMAGE) == False
    assert fm.is_image_transparent(OPAQUE_IMAGE) == False


def test_get_file_size():
    """
    GIVEN FileManager is instantiated
    WHEN the get_file_size method is called with a valid filename
    THEN the a numeric value is returned indicating the size in bytes of the file
    """
    fm = FileManager()
    assert fm.get_file_size(BLACK_WHITE_IMAGE) == 471
    assert fm.get_file_size(OPAQUE_IMAGE) == 10101 


def test_as_dataframe():
    """
    GIVEN FileManager.load_image_files() has been called with a directory path containing images
    WHEN the as_dataframe method is called
    THEN the a pandas dataframe with all relevant information for each file is returned.
    """  
    fm = FileManager()
    fm.load_image_files(IMAGE_DIR)
    df = fm.as_dataframe()
    assert type(df) == pd.DataFrame
    assert all(i in df.columns for i in DF_COLUMNS)