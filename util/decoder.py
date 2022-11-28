import mutagen
from typing import Dict
from mutagen.flac import VCFLACDict
from mutagen.id3 import ID3

def retrieveAudioProperties(audio_file : str) -> Dict[str, str]|None:
  audio = mutagen.File(audio_file)
  if type(audio.tags) is VCFLACDict:
    return retrieveFlacAudioProperties(audio.tags)
  if type(audio.tags) is ID3:
    return retrieveID3AudioProperties(audio.tags)
  return None

def trimArtistString(artist : str) -> str:
  artist_sort = ''.join(e for e in artist if e.isalnum() or e == ' ')
  artist_sort = artist_sort.lower()
  if artist_sort.startswith('the '):
    artist_sort = artist_sort[4:] + ', the'
  return artist_sort

def retrieveFlacAudioProperties(flac_tags : VCFLACDict) -> Dict[str, str]:
  [artist] = (flac_tags['albumartist'] if 'albumartist' in flac_tags.keys() else flac_tags['artist'])
  [artist_sort] = flac_tags['albumartistsort'] if 'albumartistsort' in flac_tags.keys() else \
    (flac_tags['artistsort'] if 'artistsort' in flac_tags.keys() else flac_tags['artist'])

  return {
    'artist': artist,
    'artist_sort': trimArtistString(artist_sort),
    'title': flac_tags['album'][0],
    'date': flac_tags['date'][0]
  }

def retrieveID3AudioProperties(id3_tags : ID3) -> Dict[str, str]:
  [artist] = id3_tags.getall('TPE1') if id3_tags.getall('TPE2') == [] else id3_tags.getall('TPE2')
  [artist_sort] = id3_tags.getall('TSO2') if id3_tags.getall('TSO2') != [] else \
    (id3_tags.getall('TSOP') if id3_tags.getall('TSOP') != [] else [artist])
  artist_sort = artist_sort.text[0]

  return {
    'artist': artist.text[0],
    'artist_sort': trimArtistString(artist_sort),
    'title': str(id3_tags.get('TALB').text[0]) if id3_tags.get('TALB') is not None else None,
    'date': str(id3_tags.get('TDRC').text[0]) if id3_tags.get('TDRC') is not None else None
  }