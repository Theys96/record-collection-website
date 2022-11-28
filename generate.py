import util.indexer as indexer
import util.decoder as decoder
import util.image_processor as images
import os
import json
import hashlib

def getHash(artist : str, album : str) -> str:
  return hashlib.md5((artist + album).encode()).hexdigest()[:10]

BASE_DIR : str = '../Muziek/'
PUBLIC_DIR : str = './public/'
COVERS_DIR : str = 'covers'

os.makedirs(PUBLIC_DIR, exist_ok=True)
os.makedirs(os.path.join(PUBLIC_DIR, COVERS_DIR), exist_ok=True)

albums = []
for album in indexer.getAlbumList(BASE_DIR):

  audio_file = indexer.findArbitraryMusicFile(os.path.join(BASE_DIR, album))
  audio_properties = None if audio_file is None else decoder.retrieveAudioProperties(audio_file)
  cover_file = indexer.findCoverFile(os.path.join(BASE_DIR, album))

  if audio_properties is not None and cover_file is not None:
    index = len(albums)
    audio_properties['cover'] = os.path.join(COVERS_DIR, f'%s.jpg' % (getHash(audio_properties['artist'], audio_properties['title'])))
    images.copyAndCompressPicture(cover_file, os.path.join(PUBLIC_DIR, audio_properties['cover']))
    albums.append(audio_properties)

with open(os.path.join(PUBLIC_DIR, 'albums.json'), 'w') as outfile:
  json.dump(albums, outfile)