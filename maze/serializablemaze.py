# -*- coding: utf-8 -*-

from .maze import Maze

class SerializableMaze(Maze):
    def __init__(self, width=20, height=10):
        super().__init__(width, height)

    def serialize(self):
        serializedLine = ''
        for line in self._serialized_repr():
            for coord in line:
                serializedLine += coord + ','
            serializedLine = serializedLine[0:-1]
            serializedLine += ';'
        return serializedLine[0:-1]

    @staticmethod
    def getSerializedMaze(width=10, height=5):
        maze = SerializableMaze(width, height)
        maze.randomize()
        return maze.serialize()

if __name__ == '__main__':
    print(SerializableMaze.getSerializedMaze(15,10))
