import mutagen
from typing import List, Dict
from mutagen.easyid3 import EasyID3
from mutagen.flac import VCFLACDict
from mutagen.id3 import ID3

def retrieveAudioProperties(audio_file : str) -> Dict[str, str]|None:
  audio = mutagen.File(audio_file)
  if type(audio.tags) is VCFLACDict:
    return retrieveFlacAudioProperties(audio.tags)
  if type(audio.tags) is ID3:
    return retrieveID3AudioProperties(audio.tags)
  return None

def retrieveFlacAudioProperties(flac_tags : VCFLACDict) -> Dict[str, str]:
  artist = flac_tags['albumartist'] if 'albumartist' in flac_tags.keys() else flac_tags['artist']
  artist_sort = flac_tags['albumartistsort'] if 'albumartistsort' in flac_tags.keys() else artist

  return {
    'artist': artist[0],
    'artist_sort': artist_sort[0],
    'title': flac_tags['title'][0],
    'date': flac_tags['date'][0]
  }

def retrieveID3AudioProperties(id3_tags : ID3) -> Dict[str, str]:
  [artist] = id3_tags.getall('TPE1') if id3_tags.getall('TPE2') == [] else id3_tags.getall('TPE2')
  [artist_sort] = [artist] if id3_tags.getall('TSO2') == [] else id3_tags.getall('TSO2')

  return {
    'artist': artist.text[0],
    'artist_sort': artist_sort.text[0],
    'title': str(id3_tags.get('TALB').text[0]) if id3_tags.get('TALB') is not None else None,
    'date': str(id3_tags.get('TDRC').text[0]) if id3_tags.get('TDRC') is not None else None
  }