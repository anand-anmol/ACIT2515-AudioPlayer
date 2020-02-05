"""
    Author: Anmol Anand
    ID: A01174846
    Date: 2020-01-23
    """

from song import Song

if __name__ == '__main__':
    # Creating an instance of a song
    song1 = Song('Crazy', 'Gnarls Barkley', "St. Elsewhere", '3:02', "Music/", "crazy.mp3")

    # printing its description
    print(song1.get_description())

    # playing the song
    song1.update_usage_stats()

    # printing the number of times the song has been played
    print(song1._usage.play_count)

    # change the user ratings to 3.75
    song1.user_rating = 3.75

    # print the description again
    print(song1.get_description())

    # error example
    # We get an error because the argument for pathname is invalid
    song2 = Song('Title', 'Artist', 'Album', 'Runtime', 'Pathname', 'Filename')
