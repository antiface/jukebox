class JukeBox:


    def __init__(self):
        song = Song()
        song.name = "Cashout"
        song.length = "4:25"
        self.songs = []
        self.songs.append(song)
        self.queue = Queue()
        self.supported_media = ['CD']
    
    def list_songs(self):
        song_list = []
        for song in self.songs:
            song_list.append(song.name)

        return song_list

    def add_song(self, name, length):
        song = Song()
        song.name = name
        song.length = length
        self.songs.append(song)

    def next_song(self):
        self.queue.isplaying = True
        try:
            self.queue.queue_list[0].startsong()
            self.queue.queue_list.pop(0)

        except:
            print "Queue is empty"

        finally:
            self.queue.isplaying = False

class Mp3(JukeBox):


    def __init__(self):
        JukeBox.__init__(self)
        self.add_support()

    def add_support(self):
        self.supported_media.append('Mp3')


class Song:


    def start_song(self):
        length = self.length
        print "{} is playing for {} minutes and {} seconds".format(
                self.name, length.split(':')[0], length.split(':')[1]
                )

    def end_song(self):
        length = self.length
        print "{} has ended".format(self.name)

class Queue:


    def __init__(self):
        self.queue_list = []
        self.isplaying = False

    def queue_song(self, song):
        self.queue_list.append(song)

