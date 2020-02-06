from song import Song

"""
Testing for audio files
Authors: Anmol Anand(A01174846), Felix Ruttan(A01070306), Nick Janus(A01179897).
"""

def main():
    
    # Test 1
    print(" -> Test 1")
    song1 = Song('Crazy', 'Gnarls Barkley', 'St. Elsewhere', '3:02', "music/", "crazy.mp3")
    song2 = Song('Tunak Tunak Tun', 'Daler Mehndi', 'Daler Mehndi', '5:03', "music/", "tunak.mp3")

    print(song1.get_description())
    print(song2.get_description())

    print(song1.meta_data())
    print(song2.meta_data())

if __name__ == "__main__":
    main()