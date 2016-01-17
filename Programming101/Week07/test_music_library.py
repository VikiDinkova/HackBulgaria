import unittest
from music_library import Song
from music_library import Playlist


class TestSong(unittest.TestCase):
    def setUp(self):
        self.title = "nana"
        self.artist = "Viki"
        self.album = "Na"
        self._length = "3:00"
        self.song = Song(self.title, self.artist, self.album, self._length)
        self.song2 = Song("lq", "Viktoria", "lqlq", "4:30")
        self.song3 = Song(self.title, self.artist, self.album, self._length)

    def test_init(self):
        self.assertEqual(self.title, self.song.title)

    def test_hash(self):
        self.assertEqual(
            hash((self.title, self.artist, self.album, self._length)),
            hash(self.song)
        )

    def test_eq(self):
        self.assertTrue(self.song == self.song3)
        self.assertFalse(self.song == self.song2)

    def test_lenght_to_seconds(self):
        self.assertEqual(180, self.song.lenght_to_seconds("3:00"))
        self.assertEqual(11456, self.song.lenght_to_seconds("3:10:56"))

    def test_lenght_seconds(self):
        self.assertEqual(180, self.song.length(seconds=True))

    def test_lenght_minutes(self):
        pass

    def test_lenght_hour(self):
        pass

    def test_lenght_empty(self):
        pass


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.title = "nana"
        self.artist = "Viki"
        self.album = "Na"
        self._length = "3:00"
        self.song = Song(self.title, self.artist, self.album, self._length)
        self.song2 = Song("lq", "Viktoria", "lqlq", "4:30")
        self.song3 = Song(self.title, self.artist, self.album, self._length)
        self.play_list = Playlist("random playlist")
        self.songs = [self.song, self.song2]

    def test_add_song(self):
        self.play_list.add_song(self.song)
        self.assertIn(self.song, self.play_list.get_song())

    def test_remove_song(self):
        self.play_list.remove_song(self.song)
        self.assertNotIn(self.song, self.play_list.get_song())

    def test_add_songs(self):
        self.play_list.add_songs(self.songs)
        self.assertIn(self.song, self.play_list.get_song())
        self.assertIn(self.song2, self.play_list.get_song())

    def test_total_length(self):
        pass

    def test_artist(self):
        pass

    def test_next_song(self):
        self.play_list.add_songs(self.songs)
        self.assertIn(self.play_list.next_song(), self.songs)

    def test_next_song_many_times(self):
        self.play_list.add_songs(self.songs)
        self.assertEqual(self.play_list.next_song, self.song)
        self.assertEqual(self.play_list.next_song, self.song2)

    def test_next_song_many_times_repeat_on(self):
        pass

    def test_next_song_suffle_on(self):
        self.play_list = Playlist("random playlist", repeat=True)

        self.play_list.add_songs(self.songs)
        self.assertEqual(self.play_list.next_song, self.song)
        self.assertEqual(self.play_list.next_song, self.song2)

    def test_json_dumps(self):
        pass

    if __name__ == '__main__':
        unittest.main()
