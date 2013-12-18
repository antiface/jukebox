import unittest
import jukebox

class JukeboxTests(unittest.TestCase):

    def test_listsongs_method_returns_results(self):
        jb = jukebox.Jukebox()
        songs = jb.listsongs()
        self.assertIsInstance(songs, list)
    
    def test_listsongs_method_returns_results(self):
        jb = jukebox.Jukebox()
        songs = jb.listsongs()
        self.assertIsInstance(songs, list)

    def test_add_song_to_jukebox(self):
        jb = jukebox.Jukebox()
        jb.addsong("Counting Stars", "3:22")
        self.assertEqual(jb.songs[-1].name, "Counting Stars")

    def test_zero_queue_size(self):
        queue = jukebox.Queue()
        self.assertEqual(len(queue.queuelist), 0)

    def test_add_songs_to_queue(self):
        queue = jukebox.Queue()
        jb = jukebox.Jukebox()
        jb.addsong("Counting Stars", "3:22")
        queue.queuesong(jb.songs[-1])
        queue.queuesong(jb.songs[-1])
        self.assertEqual(len(queue.queuelist), 2)

    def test_jukebox_has_a_queue(self):
        jb = jukebox.Jukebox()
        self.assertEqual(len(jb.queue.queuelist), 0)


    def test_queue_plays_next_song(self):
        jb = jukebox.Jukebox()
        jb.addsong("Counting Stars", "3:22")
        jb.addsong("Cashout", "4:33")
        jb.addsong("Burnout", "2:33")
        jb.queue.queuesong(jb.songs[0])
        jb.queue.queuesong(jb.songs[1])
        jb.queue.queuesong(jb.songs[2])
        jb.nextsong()
        self.assertEqual(jb.songs[0].name, "Cashout")

    def test_try_next_song_with_empty_queue(self):
        jb = jukebox.Jukebox()
        jb.nextsong()
        self.assertRaises(IndexError)


    def test_mp3_supports_mp3s(self):
        jb = jukebox.Mp3()
        self.assertEqual(jb.supported_media[1], 'Mp3')

