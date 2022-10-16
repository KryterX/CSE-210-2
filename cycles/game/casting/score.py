from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    """
    def __init__(self,position, player):
        super().__init__()
        self._name = player
        self._points = 0
        self.add_points(0)
        self.set_position(position)


    def add_points(self, points):
        """Adds the given points to the score's total points.
        """
        self._points += points
        self.set_text(f"{self._name}: {self._points}")
