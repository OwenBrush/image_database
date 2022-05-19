from app.file_manager import FileManager

RED_IMAGE = 'images/red_64_96.png'
WHITE_IMAGE = 'images/white_9_1000.png'
BLACK_WHITE_IMAGE = 'images/black_white_2_1.png'

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
    
    assert tuple(red) == (255, 0, 0)
    assert tuple(white) == (255, 255, 255)
    assert tuple(gray) == (127.5, 127.5, 127.5)
    