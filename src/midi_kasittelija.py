import mido

savellaji_arvot = {
        "C":0,
        "C#":-1,
        "Db":-1,
        "D":-2,
        "Eb":-3,
        "E":-4,
        "F":-5,
        "F#":-6,
        "Gb":-6,
        "G":5,
        "Ab":4,
        "A":3,
        "Bb":2,
        "B":1,
        "Cb":1,
        }

def LueMidi(tiedostopolku):
    midi = mido.MidiFile(tiedostopolku)
    tulos = []
    for raita in midi.tracks:
        raidan_nuotit = []
        vaara_savellaji = False
        transponointi = 0

        for viesti in raita:
            if viesti.type == "key_signature":
                if viesti.key[-1] == "m":
                    vaara_savellaji = True

                vaara_savellaji = False
                transponointi = savellaji_arvot[viesti.key]
            elif not vaara_savellaji:
                if viesti.type == "note_on" and viesti.velocity > 0:
                    raidan_nuotit.append(viesti.note+transponointi)
        if raidan_nuotit:
            tulos.append(raidan_nuotit)

    return tulos

def KirjoitaMidi(tiedostopolku, nuotit):
    midi = mido.MidiFile()
    track = mido.MidiTrack()

    track.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(120), time=0))
    track.append(mido.MetaMessage("time_signature"))

    for nuotti in nuotit:
        if nuotti:
            track.append(mido.Message("note_on", note=nuotti, velocity=64, time=0))
            track.append(mido.Message("note_on", note=nuotti, velocity=0, time=480))

    midi.tracks.append(track)

    midi.save(tiedostopolku)
