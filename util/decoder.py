import mutagen
from typing import List
from mutagen.easyid3 import EasyID3

def retrieveAudioProperties(audio_file : str) -> List:
  audio = mutagen.File(audio_file)
  if type(audio.tags) is mutagen.flac.VCFLACDict:
    print('FLAC:')
    print(audio.tags)
  if type(audio.tags) is mutagen.id3.ID3:
    print('ID3:')
    print(audio.tags)
  return []