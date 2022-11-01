import util.indexer as indexer
import util.decoder as decoder
import os
from mutagen.easyid3 import EasyID3

BASE_DIR : str = '../Muziek/'

for album in indexer.getAlbumList(BASE_DIR):
  print(album)
  audio_file = indexer.findArbitraryMusicFile(os.path.join(BASE_DIR, album))
  if (audio_file is not None):
    decoder.retrieveAudioProperties(audio_file)
