''' Handles all data retrieval '''
import os
from lonely import Singleton
from model import Model



def get_mp3files(path):
    os.chdir(path)
    for root, dirs, files in os.walk(path): #check all files in path
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3": #Check for mp3 extension
                yield [os.path.join(root, filename), os.path.splitext(filename)[0]]

class Song:
    def __init__(self, id, path, name):
        self.id = id
        self.path = path
        self.name = name

    def get_path(self):
        return self.path

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        if self.name:
            return self.name


@Singleton #Marks Library as a singleton
class Library(Model):
    def __init__(self):
        self.songs = []

    def load(self, path="/"):
        i = 1
        for fpath, fname in get_mp3files(path):
            self.songs.append(Song(id=i, path=fpath, name=fname))
            i= i+1
        return True

    def get(self, id):
        for song in self.songs:
            if song.get_id() == id:
                return song


    def get_songs(self):
        return self.songs

    #Checks if library empty or nah
    def check_library(self):
        if self.songs:
            return True
        else:
            return False

