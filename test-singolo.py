import chess
import chess.pgn
import csv
from midiutil import MIDIFile


# -- LOADING MIDI TABLE -- #

tablepath = "/Users/bbtgnn/Documents/GitHub/chessmusic/notes.csv"
midict = {}

with open(tablepath) as csvfile:
    reader = csv.reader(csvfile)
    for r, row in enumerate(reader):
        if r != 0:
            if row[-1] != "":
                midict[row[-1]] = int(row[0])


# -- LOADING PGN -- #

filepath = "/Users/bbtgnn/Documents/GitHub/chessmusic/test.pgn"

pgn = open(filepath)
game = chess.pgn.read_game(pgn)


# -- SETUPPING MIDI -- #

track = 0
channel = 0
time = 0  # In beats
length = 1
tempo = 60  # In BPM
volume = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1
MyMIDI.addTempo(track, time, tempo)


# -- ADDING NOTES -- #

for i, node in enumerate(game.mainline()):

    square = chess.SQUARE_NAMES[node.move.to_square]

    note = midict[square]

    MyMIDI.addNote(track, channel, note, time, length, volume)

    if i % 2 == 1:
        time += length


# -- WRITING MIDI -- #

with open("chessmusic.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
