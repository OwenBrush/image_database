import os
from file_manager import FileManager

INSTRUCTIONS = """
                    IMAGE REPOSITORY

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
    
    *Example:
        SEARCH: height = 800, bytes < 10000, landscape, red > 0
"""

def display_search_console():
    os.system('clear')
    print(INSTRUCTIONS)
    query = input("SEARCH:")

    
def display_search_results():
    pass

if __name__ == '__main__':
    display_search_console()