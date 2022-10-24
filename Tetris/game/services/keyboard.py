from pyray import *
import pyray
class KeyboardService:

    def __init__(self):
        self._keys = {}
        
        self._keys['left'] = pyray.KEY_LEFT
        self._keys['right'] = pyray.KEY_RIGHT
        self._keys['down'] = pyray.KEY_DOWN
        self._keys['space'] = pyray.KEY_SPACE
        self._keys['enter'] = pyray.KEY_ENTER

    def is_key_up(self, key):
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_pressed(self, key):
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_pressed(pyray_key)

    def is_key_down(self, key):
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)