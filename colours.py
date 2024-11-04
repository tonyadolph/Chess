
from termcolor import colored
from enum import Enum

class Color(Enum):
    BLACK = '\033[97;40m'  # White foreground, black background
    WHITE = '\033[30;47m'  # Black foreground, white background
    LIGHT_TILE = '\033[30;103m'  # Black foreground, light brown background
    DARK_TILE = '\033[30;43m'  # Black foreground, dark brown background
    RESET = '\033[0m'  # Reset to default