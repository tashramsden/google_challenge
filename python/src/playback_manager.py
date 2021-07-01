"""A playback manager class."""


class PlaybackManager:
    """A class used to represent a playback manager"""
    def __init__(self):
        self.current_video = None
        self.is_paused = None

    def video_is_playing(self, video):
        self.current_video = video
        self.is_paused = False

    def video_paused(self):
        self.is_paused = True

    def video_stopped(self):
        self.current_video = None
        self.is_paused = None
