import unittest
import inspect
from datetime import time
from song import Song
from podcast import Podcast
from playlist import PlayList
from audio_library import AudioLibrary
import os


class TestAudioLibrary(unittest.TestCase):
    """
    Test class for AudioPlayer
    Authors: Anmol Anand(A01174846), Felix Ruttan(A01070306), 
    Nicholas Janus(A01179897)
    """

    def setUp(self):
        """called before every test method"""
        self.logAudioPlayer()
        self.library = AudioLibrary()
        self.song1 = Song('Crazy', 'Gnarls Barkley','St. Elsewhere', '3:02', os.path.join(os.getcwd(), 'music') , "crazy.mp3")
        self.podcast1 = Podcast('Startalk', "Neil deGrasse Tyson", "56:02", os.path.join(os.getcwd(), 'podcasts'), "startalk.mp3", "2020", "18", 12)
        self.playlist1 = PlayList('study time', "playlist for my study sessions")
        self.library.add_playlist(self.playlist1)
        self.library.add_podcast(self.podcast1)
        self.library.add_song(self.song1)
    
    def tearDown(self):
        """called after every test method"""
        self.logAudioPlayer()

    def test_init(self):
        """C-1: tests the constructor"""

        self.library1 = AudioLibrary()

        self.assertEqual(len(self.library1.get_playlist_list()), 0)
        self.assertEqual(len(self.library1.get_podcast_list()), 0)
        self.assertEqual(len(self.library1.get_song_list()), 0)

    def test_add_song(self):
        """A-1: tests the test_song method"""
        self.library.add_song(self.song1)

        self.assertIn(self.song1, self.library.get_song_list())
    
        with self.assertRaises(ValueError):
            self.library.add_song(2)

    def test_add_podcast(self):
        """A-2: tests the add_podcast method"""
        self.library.add_podcast(self.podcast1)

        self.assertIn(self.podcast1, self.library.get_podcast_list())

        with self.assertRaises(ValueError):
            self.library.add_podcast(2)
    
    def test_add_playlist(self):
        """A-3: tests the add_playlist method"""
        self.library.add_playlist(self.playlist1)

        self.assertIn(self.playlist1, self.library.get_playlist_list())

        with self.assertRaises(ValueError):
            self.library.add_playlist(2)

    def test_remove_song(self):
        """R-1: tests the remove_song method"""
        self.library.remove_song(self.song1)

        self.assertNotIn(self.song1, self.library.get_song_list())

        with self.assertRaises(ValueError):
            self.library.remove_song(2)
    
    def test_remove_podcast(self):
        """R-2: tests the remove_podcast method"""
        self.library.remove_podcast(self.podcast1)

        self.assertNotIn(self.podcast1, self.library.get_podcast_list())
        
        with self.assertRaises(ValueError):
            self.library.remove_podcast(2)
    
    def test_remove_playlist(self):
        self.library.remove_playlist(self.playlist1)

        self.assertNotIn(self.playlist1, self.library.get_playlist_list())

        with self.assertRaises(ValueError):
            self.library.remove_playlist(2)

    def test_get_song_list(self):
        """G-1: tests the get_song_list method"""
        expected_output = [self.song1]

        self.assertEqual(self.library.get_song_list(), expected_output)
    
    def test_get_podcast_list(self):
        """G-2: tests the get_podcast_list method"""
        expected_output = [self.podcast1]

        self.assertEqual(self.library.get_podcast_list(), expected_output)

    def test_get_playlist_list(self):
        """G-3: tests the get_playlist_list method"""
        expected_output = [self.playlist1]

        self.assertEqual(self.library.get_playlist_list(), expected_output)
    
    def test_number_of_songs(self):
        """N-1: tests the number_of_songs method"""

        self.assertEqual(self.library.number_of_songs(), 1)
    
    def test_number_of_podcasts(self):
        """N-2: tests the number_of_podcasts method"""
        self.podcast2 = Podcast('BCIT speaks', "Anmol", "58:05", "podcasts/", "bcit_speaks.mp3", "2", "2020", 10)
        self.library.add_podcast(self.podcast2)

        self.assertEqual(self.library.number_of_podcasts(), 2)
    
    def test_number_of_playlists(self):
        """N-3: test the number_of_playlists method"""
        self.playlist2 = PlayList('Workout', 'Gym time and marathons')
        self.playlist3 = PlayList('Transit', 'Help me pass time in SkyTrain')
        self.library.add_playlist(self.playlist2)
        self.library.add_playlist(self.playlist3)

        self.assertEqual(self.library.number_of_playlists(), 3)

    def logAudioPlayer(self):
        """utility method to trace control flow"""
        currentTest= self.id().split('.')[-1]
        callingFunction= inspect.stack()[1][3]
        print('in %s -%s()' % (currentTest, callingFunction))


if __name__ == "__main__":
    unittest.main()
