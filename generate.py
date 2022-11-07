import util.indexer as indexer
import util.decoder as decoder
import util.image_processor as images
import os
import json

BASE_DIR : str = '../Muziek/'
PUBLIC_DIR : str = './public/'
COVERS_DIR : str = 'covers'

albums = []
for album in indexer.getAlbumList(BASE_DIR):

  audio_file = indexer.findArbitraryMusicFile(os.path.join(BASE_DIR, album))
  audio_properties = None if audio_file is None else decoder.retrieveAudioProperties(audio_file)
  cover_file = os.path.join(BASE_DIR, album, 'Cover.jpg')

  if (audio_properties is not None and os.path.exists(cover_file)):
    index = len(albums)
    audio_properties['cover'] = os.path.join(COVERS_DIR, f'%04d.jpg' % index)
    images.copyAndCompressPicture(cover_file,  os.path.join(PUBLIC_DIR, audio_properties['cover']))
    albums.append(audio_properties)

with open(os.path.join(PUBLIC_DIR, 'albums.json'), 'w') as outfile:
  json.dump(albums, outfile)