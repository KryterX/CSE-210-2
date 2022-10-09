import pyray
from shared.point import Point


class KeyboardService:
    """
    Detects player input. 
    """

    def __init__(self, cell_size = 1):
        """
        Constructs a new KeyboardService using the specified cell size.
        """
        self._cell_size = cell_size

    def get_direction(self):
        """
        Gets the selected direction based on the currently pressed keys.
        """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        
        #if pyray.is_key_down(pyray.KEY_UP):
        #    dy = -1
        
        #if pyray.is_key_down(pyray.KEY_DOWN):
        #    dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction