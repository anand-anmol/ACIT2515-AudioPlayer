import unittest
import inspect
from podcast import Podcast
from audio_file import AudioFile
from datetime import time

class TestPodcast(unittest.TestCase):
	"""
		Author: Anmol Anand (A01174846)
	"""

	def setUp(self):
		"""called before every test method"""
		self.logPoint()
		self.podcast1 = Podcast('Startalk', "Neil deGrasse Tyson", "56:02", "podcasts/", "startalk.mp3", "2020", "18", time(0, 15, 23), 12)
		self.podcast2 = Podcast('BCIT speaks', "Anmol", "58:05", "podcasts/", "bcit_speaks.mp3", "2", "2020", time(0, 15, 23), 10)
		self.podcast3 = Podcast('Podcast title', "Podcast Artist", "36:52", "podcasts/", "sample.mp3", "series", "season", time(0, 30, 55))

	def tearDown(self):
		"""called after every test method"""
		self.logPoint()

	def test_init(self):
		"""1A: tests the constructor"""
		self.assertTrue(issubclass(Podcast, AudioFile))
	
	def test_series_getter(self):
		"""2D: tests the getter for the series"""
		self.assertEqual(self.podcast1.series, "2020")
		self.assertEqual(self.podcast2.series, "2")

	def test_series_setter(self):
		"""2A: tests the setter for the series"""
		self.podcast1.series = "25"
		self.podcast2.series = "100"

		self.assertEqual(self.podcast1.series, "25")
		self.assertEqual(self.podcast2.series, "100")

	def test_season_getter(self):
		"""2J: tests the getter for the season"""
		self.assertEqual(self.podcast1.season, "18")
		self.assertEqual(self.podcast2.season, "2020")
	
	def test_season_setter(self):
		"""2B: tests the setter for the season"""
		self.podcast1.season = "25"
		self.podcast2.season = "100"

		self.assertEqual(self.podcast1.season, "25")
		self.assertEqual(self.podcast2.season, "100")

	def test_episode_number_getter(self):
		"""tests the getter for the episode number"""
		self.assertEqual(self.podcast1.episode_number, 12)
		self.assertEqual(self.podcast2.episode_number, 10)
	
	def test_episode_number_setter(self):
		"""2C: tests the setter for the episode number"""
		self.podcast1.episode_number = 25
		self.podcast2.episode_number = 100

		self.assertEqual(self.podcast1.episode_number, 25)
		self.assertEqual(self.podcast2.episode_number, 100)

	def test_get_description(self):
		"""2E: tests the get_description method of the podcast class"""
		self.assertEqual(self.podcast1.get_description(), \
			"2020: Startalk, None, Season 18 Episode 12 (56 mins)")
		self.assertEqual(self.podcast2.get_description(), \
			"2: BCIT speaks, None, Season 2020 Episode 10 (58 mins)")
		self.assertEqual(self.podcast3.get_description(), \
			"series: Podcast title, None, Season season (36 mins)")
	
	def test_get_progress(self):
		"""5B: tests the get_progress method of the podcast class"""
		self.assertEqual(self.podcast1.get_progress(), time(0,15,23))
		self.assertEqual(self.podcast2.get_progress(), time(0,15,23))
		self.assertEqual(self.podcast3.get_progress(), time(0,30,55))
	
	def test_meta_data(self):
		"""4A: tests the meta_data method of the podcast class"""
		self.assertEqual(self.podcast1.meta_data(), \
			{'title': 'Startalk', 'artist': 'Neil deGrasse Tyson',\
				'series': '2020', 'season': '18', 'episode_number': 12,\
				'episode_date': None, 'progress': time(0, 15, 23),\
				'date_added': '2020-02-13', 'runtime': time(0, 56, 2),\
				'pathname': 'podcasts/', 'filename': 'startalk.mp3', 'play_count': 0,\
				'last_played': None, 'rating': None})
		self.assertEqual(self.podcast2.meta_data(), \
			{'title': 'BCIT speaks', 'artist': 'Anmol', 'series': '2', 'season': '2020', \
				'episode_number': 10, 'episode_date': None, 'progress': time(0, 15, 23), \
				'date_added': '2020-02-13', 'runtime': time(0, 58, 5), \
				'pathname': 'podcasts/', 'filename': 'bcit_speaks.mp3', 'play_count': 0, \
				'last_played': None, 'rating': None})
		self.assertEqual(self.podcast3.meta_data(), \
			{'title': 'Podcast title', 'artist': 'Podcast Artist', 'series': 'series', \
				'season': 'season', 'episode_number': None, 'episode_date': None,\
				'progress': time(0, 30, 55), 'date_added': '2020-02-13', \
				'runtime': time(0, 36, 52), 'pathname': 'podcasts/', \
				'filename': 'sample.mp3', 'play_count': 0, 'last_played': None, 'rating': None})
	
	def test_usage_stats(self):
		self.podcast1.get_usage_stats().increment_usage_stats()
		self.podcast2.get_usage_stats().increment_usage_stats()
		self.podcast3.get_usage_stats().increment_usage_stats()

		self.assertEqual(self.podcast1.get_usage_stats().play_count, 1)
		self.assertEqual(self.podcast2.get_usage_stats().play_count, 1)
		self.assertEqual(self.podcast3.get_usage_stats().play_count, 1)

	def logPoint(self):
		"""utility method to trace control flow"""
		currentTest= self.id().split('.')[-1]
		callingFunction= inspect.stack()[1][3]
		print('in %s -%s()' % (currentTest, callingFunction))


if __name__ == "__main__":
	unittest.main()
