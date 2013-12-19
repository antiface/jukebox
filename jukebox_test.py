import unittest
import jukebox

class JukeBoxTests(unittest.TestCase):

    def test_listsongs_method_returns_results(self):
        jb = jukebox.JukeBox()
        songs = jb.list_songs()
        self.assertIsInstance(songs, list)
    
    def test_listsongs_method_returns_results(self):
        jb = jukebox.JukeBox()
        songs = jb.list_songs()
        self.assertIsInstance(songs, list)

    def test_add_song_to_jukebox(self):
        jb = jukebox.JukeBox()
        jb.add_song("Counting Stars", "3:22")
        self.assertEqual(jb.songs[-1].name, "Counting Stars")

    def test_zero_queue_size(self):
        queue = jukebox.Queue()
        self.assertEqual(len(queue.queue_list), 0)

    def test_add_songs_to_queue(self):
        queue = jukebox.Queue()
        jb = jukebox.JukeBox()
        jb.add_song("Counting Stars", "3:22")
        queue.queue_song(jb.songs[-1])
        queue.queue_song(jb.songs[-1])
        self.assertEqual(len(queue.queue_list), 2)

    def test_jukebox_has_a_queue(self):
        jb = jukebox.JukeBox()
        self.assertEqual(len(jb.queue.queue_list), 0)


    def test_queue_plays_next_song(self):
        jb = jukebox.JukeBox()
        jb.add_song("Counting Stars", "3:22")
        jb.add_song("Cashout", "4:33")
        jb.add_song("Burnout", "2:33")
        jb.queue.queue_song(jb.songs[0])
        jb.queue.queue_song(jb.songs[1])
        jb.queue.queue_song(jb.songs[2])
        jb.next_song()
        self.assertEqual(jb.songs[0].name, "Cashout")

    def test_try_next_song_with_empty_queue(self):
        jb = jukebox.JukeBox()
        jb.next_song()
        self.assertRaises(IndexError)


    def test_mp3_supports_mp3s(self):
        jb = jukebox.Mp3()
        self.assertEqual(jb.supported_media[1], 'Mp3')

