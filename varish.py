# ==========================
# Music Playlist Manager
# ==========================

class Song:

    def __init__(self, title, singer):
        self.title = title
        self.singer = singer

    def show(self):
        print(f"Song : {self.title}")
        print(f"Singer : {self.singer}")
        print("-" * 25)


class Playlist:

    def __init__(self):
        self.songs = []

    # Add Song
    def add_song(self):

        title = input("Song Name : ")
        singer = input("Singer Name : ")

        song = Song(title, singer)

        self.songs.append(song)

        print("Song Added")

    # View Playlist
    def view_playlist(self):

        if len(self.songs) == 0:
            print("Playlist Empty")
            return

        print("\n===== PLAYLIST =====")

        for song in self.songs:
            song.show()

    # Play Song
    def play_song(self):

        title = input("Song Name : ")

        for song in self.songs:

            if song.title.lower() == title.lower():

                print(f"Now Playing : {song.title}")
                return

        print("Song Not Found")

    # Delete Song
    def delete_song(self):

        title = input("Song Name : ")

        for song in self.songs:

            if song.title.lower() == title.lower():

                self.songs.remove(song)

                print("Song Deleted")
                return

        print("Song Not Found")


# ==========================
# Main Program
# ==========================

playlist = Playlist()

while True:

    print("\n===== MUSIC PLAYLIST =====")
    print("1. Add Song")
    print("2. View Playlist")
    print("3. Play Song")
    print("4. Delete Song")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        playlist.add_song()

    elif choice == "2":
        playlist.view_playlist()

    elif choice == "3":
        playlist.play_song()

    elif choice == "4":
        playlist.delete_song()

    elif choice == "5":
        print("Good Bye")
        break

    else:
        print("Invalid Choice")
