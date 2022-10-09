from shared.point import Point
from casting.artifact import Artifact

### ADD VELOCITY
VELOCITY_ARTIFACTS = 3
###

class Director:
    """
    A person who directs the game. 
    """

    def __init__(self, keyboard_service, video_service, starting_artifacts, columns, rows, font_size, cell_size):
        """
        Constructs a new Director using the specified keyboard and video services.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        ### ADD SCORE and other variables
        self._score = 0
        
        self._starting_artifacts = starting_artifacts
        self._columns = columns
        self._rows = rows
        self._font_size = font_size
        self._cell_size = cell_size
        ###
        
    def start_game(self, cast):
        """
        Starts the game using the given cast. Runs the main game loop.
        """
        ### STARTING CONDITIONS
        for n in range(self._starting_artifacts):
            artifact = Artifact(self._columns, self._rows, self._cell_size, self._font_size)
            cast.add_actor("artifacts", artifact)
        ###
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """
        Gets directional input from the keyboard and applies it to the robot.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)

        ### Velocity for Artifacts
        artifacts = cast.get_actors("artifacts")
        velocity_artifacts = Point(0, VELOCITY_ARTIFACTS)

        for artifact in artifacts:
            artifact.set_velocity(velocity_artifacts)
        ###

    def _do_updates(self, cast):
        """
        Updates the robot's position and resolves any collisions with artifacts.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        ### Move artifacts
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
        ###

        ### Remove hit artifacts create new Artifacts        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position_bottom()):
                self._add_score(artifact.get_points())
                cast.remove_actor("artifacts", artifact)
                
                ### ADD new artifact when one get removed
                new_artifact = Artifact(self._columns, self._rows, self._cell_size, self._font_size)
                new_artifact.set_position(Point(new_artifact.get_position().get_x(), max_y))
                cast.add_actor("artifacts", new_artifact)
        ###

        banner.set_text("Score: " + str(self._score))    
       
    def _do_outputs(self, cast):
        """
        Draws the actors on the screen.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    ### ADD SET SCORE
    def _add_score(self, score):
        self._score = self._score + score
    ###