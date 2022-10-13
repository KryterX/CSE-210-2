from game.scripting.action import Action




class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.
        """

        actors = cast.get_all_actors()
        for i in actors:
            i.move_next()