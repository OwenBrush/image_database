import os
from file_manager import FileManager
from search_engine import SearchEngine

search_engine = SearchEngine()
file_manager = FileManager()

HEADER = """
    IMAGE REPOSITORY
"""

INSTRUCTIONS = """
SEARCH FILTERS:
    name X              # Filenames containing text
    width =/</> X       # Image width
    height =/</> X      # Image height
    portrait            # Height greater than width
    landscape           # Width greater than height 
    square              # Height equal to width
    transparent         # Containing any amount of transparency
    opaque              # Containing no amounnt of transparency    
    red =/</> X         # Averaged red value (between 0 and 255)
    blue =/</> X        # Averaged blue value (between 0 and 255)
    green =/</> x       # Averaged green value (between 0 and 255)
    bytes =/</> X       # file size                     
    
    *All filters should be comma seperated.
    *Multiple filters can be given, and they will all be applied to the results
    *quit terminal by entering 'quit'
    *Example:
        SEARCH: height = 600, bytes > 10000, landscape, red > 0
"""

def display_search_console(query):
    os.system('clear')
    df = file_manager.as_dataframe()
    df = search_engine.apply_filters(df, query)
    print(HEADER)
    print(df)
    print(INSTRUCTIONS)
    query = input("SEARCH:")
    if query == 'quit':
        exit()
    else:
        display_search_console(query)

    
def display_search_results():
    pass

if __name__ == '__main__':
    display_search_console('')