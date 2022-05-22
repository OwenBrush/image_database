from app.search_engine import SearchEngine
from app.file_manager import FileManager
import os

YELLOW_IMAGE = 'yellow_opaque_alpha_800_600.png'

QUERY1 = 'name yellow, width = 800, height > 0, landscape, red = 255, blue < 100, green > 100, bytes < 900000'
QUERY1_PARSED = [
                ['name','yellow'], 
                ['width', '=', '800'],
                ['height', '>', '0'],
                ['landscape'],
                ['red','=','255'],
                ['blue','<','100'],
                ['green','>','100'],
                ['bytes','<','900000'],
                ]


def test_parse_query():
    """
    GIVEN SearchEngine is instantiated
    WHEN the parse_query method is called with a comma seperated list
    THEN then a list of split strings is returned
    """
    sm = SearchEngine()
    parsed = sm.parse_query(QUERY1)
    assert parsed == QUERY1_PARSED
    
def test_apply_filters():
    """
    GIVEN SearchEngine is instantiated and FileManager has loaded the test images
    WHEN apply_filters method is called with the dataframe from FileManager
    THEN a dataframe with applied filters is returned
    """
    se = SearchEngine()
    fm = FileManager()
    df = fm.as_dataframe()
    
    # ['name', 'width', 'height', 'portrait', 'square', 'landscape', 'transparent','opaque', 'red' ,'green' ,'blue' ,'bytes']
    
    assert se.apply_filters(df, 'name yellow')['name'].str.contains(YELLOW_IMAGE).all()
    assert se.apply_filters(df,'width < 800')['width'].max() < 800
    assert se.apply_filters(df,'height = 600')['width'].min() == 600
    assert se.apply_filters(df,'red = 255')['red'].min() == 255
    assert se.apply_filters(df,'green > 0')['green'].min() > 0
    assert se.apply_filters(df,'blue < 255')['blue'].max() < 255
    assert se.apply_filters(df,'bytes > 1000')['bytes'].min() > 1000
    assert (se.apply_filters(df,'portrait')['portrait'] == True).all()
    assert (se.apply_filters(df,'square')['square'] == True).all()
    assert (se.apply_filters(df,'landscape')['landscape'] == True).all()
    assert (se.apply_filters(df,'transparent')['transparent'] == True).all()
    assert (se.apply_filters(df,'opaque')['opaque'] == True).all()