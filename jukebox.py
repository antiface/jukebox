import time

class Jukebox:
    def __init__(self):
        song = Song()
        song.name = "Cashout"
        song.length = "4:25"
        self.songs = []
        self.songs.append(song)
        self.queue = Queue()
        self.supported_media = ['CD']
    
    def listsongs(self):
        songlist = []
        for song in self.songs:
            songlist.append(song.name)

        return songlist

    def addsong(self, name, length):
        song = Song()
        song.name = name
        song.length = length
        self.songs.append(song)

    def nextsong(self):
        self.queue.isplaying = True
        try:
            self.queue.queuelist[0].startsong()
            self.queue.queuelist.pop(0)

        except:
            print "Queue is empty"

        finally:
            self.queue.isplaying = False

class Mp3(Jukebox):
    def __init__(self):
        Jukebox.__init__(self)
        self.add_support()

    def add_support(self):
        self.supported_media.append('Mp3')


class Song:
    def startsong(self):
        length = self.length
        print "{} is playing for {} minutes and {} seconds".format(
                self.name, length.split(':')[0], length.split(':')[1])

    def endsong(self):
        length = self.length
        print "{} has ended".format(self.name)

class Queue:
    def __init__(self):
        self.queuelist = []
        self.isplaying = False

    def queuesong(self, song):
        self.queuelist.append(song)

