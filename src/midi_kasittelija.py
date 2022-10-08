"""Mahdollistaa MIDI-tiedostojen lukemisen ja kirjoittamisen.
from midi_kasittelija imort lue_midi, kirjoita_midi
"""
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

def lue_midi(tiedostopolku):
    """Lukee nuotit MIDI tiedostosta"""
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
                else:
                    vaara_savellaji = False
                    transponointi = savellaji_arvot[viesti.key]
            elif not vaara_savellaji:
                if viesti.type == "note_on" and viesti.velocity > 0:
                    raidan_nuotit.append(viesti.note+transponointi)
        if raidan_nuotit:
            tulos.append(raidan_nuotit)

    return tulos

def kirjoita_midi(tiedostopolku, nuotit, tempo=120, rytmi="1/4"):
    """Kirjoittaa halutut nuotit valittuun MIDI-tiedostoon annetulla tempolla"""
    midi = mido.MidiFile()
    raita = mido.MidiTrack()

    rytmi = rytmi_taulukoksi(rytmi)
    iskun_kesto = midi.ticks_per_beat
    rytmi = [round(x*4*iskun_kesto) for x in rytmi]

    raita.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(tempo), time=0))
    raita.append(mido.MetaMessage("time_signature"))
    raita.append(mido.Message("program_change", program=0, time=0))

    rytmi_i = 0

    for nuotti in nuotit:
        if nuotti:
            raita.append(mido.Message("note_on", note=nuotti, velocity=64, time=0))
            raita.append(mido.Message("note_on", note=nuotti, velocity=0, time=rytmi[rytmi_i]))
            rytmi_i = (rytmi_i + 1) % len(rytmi)

    midi.tracks.append(raita)
    midi.save(tiedostopolku)

def rytmi_taulukoksi(rytmi):
    rytmi = rytmi.split("|")
    tulos = []
    for alkio in rytmi:
        alkio = alkio.split("/")
        if len(alkio) == 2:
            tulos.append(int(alkio[0]) / int(alkio[1]))
        elif len(alkio) == 1:
            tulos.append(int(alkio[0]))
        else:
            continue

    return tulos
