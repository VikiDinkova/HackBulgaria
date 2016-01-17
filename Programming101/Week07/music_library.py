import json


class Song:
    def __init__(self, title, artist, album, lenght):
        self.title = title
        self.artist = artist
        self.album = album
        self._lenght = lenght

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self._lenght)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.title, self.artist, self.album, self._lenght))

    def __repr__(self):
        "Song('{}','{}','{}','{}')", format(self.title, self.artist, self.album, self._lenght)

    def lenght_to_seconds(self, duration):
        duration_list = duration.split(":")
        if len(duration_list) == 3:
            return int(duration_list[2]) + int(duration_list[1]) * 60 + int(duration_list[0]) * 3600
        elif len(duration_list) == 2:
            return int(duration_list[1]) + int(duration_list[0]) * 60

    def length(self, **duration_type):
        if "seconds" in duration_type.keys():
            return self.lenght_to_seconds(self._lenght)
        elif "minutes" in duration_type.keys():
            return self.minutes.lenght_to_seconds(self._lenght) // 60
        elif "hours" in duration_type.keys():
            return self.lenght_to_seconds(self._lenght) // 3600
        else:
            return self.lenght


class Playlist:
    def __init__(self, name, repeat=False, suffle=False):
        self.name = name
        self.repeat = repeat
        self.suffle = suffle
        self.songs = []
        self.song_index = 0

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def add_songs(self, songs):
        self.songs += songs

    def get_songs(self):
        return self.songs

    def total_lenght(self):
        duration = 0
        for song in self.songs:
            duration += song.lenght(seconds=True)
        if duration < 3600:
            return "{}:{}".format(
                duration // 60,
                duration % 60
            )
        return "{}:{}:{}".format(
            duration // 3600,
            (duration % 3600) // 60,
            duration % 60
        )

    def artists(self):
        artists_list = {}
        for song in self.songs:
            if song.artists not in artists_list.keys():
                artists_list[song.artists] = 0
            artists_list[song.artists] += 0
        return artists_list

    def next_song(self):
        if self.song_index >= len(self.songs) and self.repeat:
            self.song_index = 0
        song = self.song[self.song_index]
        self.song_index += 1
        return song

    def pprint_playlist(self):
        pass

    def get_dict(self):
        song_dict = []
        for song in self.songs:
            song_dict.append(song.__dict__)

        result = {
            "name": self.name,
            "repeat": self.repeat,
            "suffle": self.suffle,
            "song_index": self.song_index,
            "songs": song_dict,
        }

        return result

    def load_from_dict(self, data_dict):
        play_list = Playlist("Name")
        songs = data_dict.pop('songs')
        play_list.__dict__ = data_dict

        for song in songs:
            new_song = Song()
            new_song.__dict__ = song
            play_list.add_song(new_song)

        return play_list

    def save_to_json(self, file_name):
        with open(file_name, 'w') as f:
            json.dumps(self.get_dict(), f, indent=4)

    def load_from_json(self, file_name):
        with open(file_name, 'r') as f:
            data_dict = json.load(f)
