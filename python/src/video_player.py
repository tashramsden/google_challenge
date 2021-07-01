"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.all_playlists = Playlist()
        self.is_playing = False
        self.is_paused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda x: x.title)
        print("Here's a list of all available videos:")
        for video in videos:
            print(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if not video:
            print("Cannot play video: Video does not exist")
            return

        if self.is_playing != False:
            print(f"Stopping video: {self.is_playing.title}")

        print(f"Playing video: {video.title}")
        self.is_playing = video
        self.is_paused = False

    def stop_video(self):
        """Stops the current video."""
        if self.is_playing == False:
            print("Cannot stop video: No video is currently playing")
            return
        else:
            print(f"Stopping video: {self.is_playing.title}")
            self.is_playing = False
            self.is_paused = True

    def play_random_video(self):
        """Plays a random video from the video library."""
        if self.is_playing != False:
            print(f"Stopping video: {self.is_playing.title}")
        video = random.choice(self._video_library.get_all_videos())
        print(f"Playing video: {video.title}")
        self.is_playing = video
        self.is_paused = False

    def pause_video(self):
        """Pauses the current video."""
        if self.is_playing == False:
            print("Cannot pause video: No video is currently playing")
            return
        elif self.is_paused == True:
            print(f"Video already paused: {self.is_playing.title}")
        else:
            print(f"Pausing video: {self.is_playing.title}")
            self.is_paused = True

    def continue_video(self):
        """Resumes playing the current video."""
        if self.is_playing == False:
            print(f"Cannot continue video: No video is currently playing")
            return
        elif self.is_paused == False:
            print(f"Cannot continue video: Video is not paused")
            return
        else:
            print(f"Continuing video: {self.is_playing.title}")
            self.is_paused = False

    def show_playing(self):
        """Displays video currently playing."""
        if self.is_playing == False:
            print("No video is currently playing")
            return
        video = self.is_playing
        if self.is_paused:
            print(f"Currently playing: {video.title} ({video.video_id}) [{' '.join(video.tags)}] - PAUSED")
        else:
            print(f"Currently playing: {video.title} ({video.video_id}) [{' '.join(video.tags)}]")

    def playlist_exists(self, playlist_name):
        """Checks whether the playlist exists, returns the playlist if it does, and False otherwise.
        Args:
            playlist_name: The playlist name.
        """
        this_playlist = False
        for playlist in self.all_playlists.playlists:
            for item in playlist:
                if item.upper() == playlist_name.upper():
                    this_playlist = playlist
        return this_playlist

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        if self.playlist_exists(playlist_name):
            print("Cannot create playlist: A playlist with the same name already exists.")
            return
        else:
            self.all_playlists.add_playlist(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")
            # print(self.all_playlists.playlists)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if self.playlist_exists(playlist_name) == False:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return

        video = self._video_library.get_video(video_id)
        if not video:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return

        already_video = False
        for playlist in self.all_playlists.playlists:
            for item in playlist:
                if video_id == item:
                    already_video = True
        if already_video:
            print(f"Cannot add video to {playlist_name}: Video already added")
            return

        self.all_playlists.add_video(playlist_name, video_id)
        print(f"Added video to {playlist_name}: {video.title}")
        # print(self.all_playlists.playlists)

    def show_all_playlists(self):
        """Display all playlists."""
        if self.all_playlists.playlists == []:
            print("No playlists exist yet")
            return
        playlist_names = []
        for playlist in self.all_playlists.playlists:
            playlist_name = playlist[0]
            playlist_names.append(playlist_name)
        playlist_names.sort()
        print(f"Showing all playlists:")
        for name in playlist_names:
            print(name)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        this_playlist = self.playlist_exists(playlist_name)
        if this_playlist == False:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            return
        list_videos = this_playlist[1:]
        print(f"Showing playlist: {playlist_name}")
        if list_videos == []:
            print(f"    No videos here yet")
        else:
            for id in list_videos:
                video = self._video_library.get_video(id)
                print(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        this_playlist = self.playlist_exists(playlist_name)
        if this_playlist == False:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
            return
        video = self._video_library.get_video(video_id)
        if not video:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
            return
        if video.video_id not in this_playlist:
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            return
        self.all_playlists.remove_video(playlist_name, video_id)
        print(f"Removed video from {playlist_name}: {video.title}")
        # print(self.all_playlists.playlists)

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        if self.playlist_exists(playlist_name) == False:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
            return
        self.all_playlists.clear_playlist(playlist_name)
        print(f"Successfully removed all videos from {playlist_name}")
        # print(self.all_playlists.playlists)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        if self.playlist_exists(playlist_name) == False:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
            return
        self.all_playlists.delete_playlist(playlist_name)
        print(f"Deleted playlist: {playlist_name}")
        # print(self.all_playlists.playlists)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.
        Args:
            search_term: The query to be used in search.
        """
        matches = []
        for video in self._video_library.get_all_videos():
            if search_term.upper() in video.title.upper():
                matches.append(video)
        if matches == []:
            print(f"No search results for {search_term}")
            return
        matches.sort(key=lambda x: x.title)
        print(f"Here are the results for {search_term}:")
        count = 1
        for video in matches:
            print(f"    {count}) {video.title} ({video.video_id}) [{' '.join(video.tags)}]")
            count += 1
        answer = input(f"Would you like to play any of the above? If yes, specify the number of the video.\n"
                       f"If your answer is not a valid number, we will assume it's a no.\n")
        try:
            try:
                video = matches[int(answer)-1]
                self.play_video(video.video_id)
            except IndexError:
                return
        except ValueError:
            return

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag .
        Args:
            video_tag: The video tag to be used in search.
        """
        matches = []
        this_video = False
        for video in self._video_library.get_all_videos():
            for tag in video.tags:
                if video_tag.upper() == tag.upper():
                    this_video = True
            if this_video:
                matches.append(video)
            this_video = False
        if matches == []:
            print(f"No search results for {video_tag}")
            return
        matches.sort(key=lambda x: x.title)
        print(f"Here are the results for {video_tag}:")
        count = 1
        for video in matches:
            print(f"    {count}) {video.title} ({video.video_id}) [{' '.join(video.tags)}]")
            count += 1
        answer = input(f"Would you like to play any of the above? If yes, specify the number of the video.\n"
                       f"If your answer is not a valid number, we will assume it's a no.\n")
        try:
            try:
                video = matches[int(answer) - 1]
                self.play_video(video.video_id)
            except IndexError:
                return
        except ValueError:
            return

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
