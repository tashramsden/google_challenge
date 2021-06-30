"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self):
        self.playlists = []

    def add_playlist(self, playlist_name: str):
        self.playlists.append([playlist_name])

    def add_video(self, playlist_name, video_id):
        for playlist in self.playlists:
            for item in playlist:
                if item.upper() == playlist_name.upper():
                    playlist.append(video_id)

    def remove_video(self, playlist_name, video_id):
        for playlist in self.playlists:
            for item in playlist:
                if item.upper() == playlist_name.upper():
                    playlist.remove(video_id)

    def clear_playlist(self, playlist_name):
        for playlist in self.playlists:
            for item in playlist:
                if item.upper() == playlist_name.upper():
                    for item_to_remove in playlist[1:]:
                        playlist.remove(item_to_remove)

    def delete_playlist(self, playlist_name):
        for playlist in self.playlists:
            for item in playlist:
                if item.upper() == playlist_name.upper():
                    self.playlists.remove(playlist)
