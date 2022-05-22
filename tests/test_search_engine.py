from app.search_engine import SearchEngine

OPAQUE_IMAGE = 'images/yellow_opaque_alpha_800_600.png'

QUERY1 = 'name yellow, width = 800, height > 0, landscape, red = 255, blue > 100, green < 100, bytes < 900000'
QUERY1_PARSED = [
                ['name','yellow'], 
                ['width', '=', '800'],
                ['height', '>', '0'],
                ['landscape'],
                ['red','=','255'],
                ['blue','>','100'],
                ['green','<','100'],
                ['bytes','<','900000'],
                ]


def test_parse_query():
    """
    GIVEN SearchEngine is instantiated
    WHEN the parse_query method is called with a comma seperated list
    THEN then a list of split strings is returned
    """
    
    sm = SearchEngine
    parsed = sm.parse_query(QUERY1)
    assert parsed == QUERY1_PARSED