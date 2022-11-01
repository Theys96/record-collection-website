import os
import mutagen
from typing import List

def getAlbumList(base_dir: str) -> List[str]:
  albums = []
  for (_, artist_folders, _) in os.walk(base_dir):
    for artist_folder in artist_folders:
      for (_, album_folders, _) in os.walk(os.path.join(base_dir, artist_folder)):
        for album_folder in album_folders:
          albums.append(os.path.join(base_dir, artist_folder, album_folder))
        break
    break
  return albums

def findArbitraryMusicFile(dir: str) -> str|None:
  for (_, _, files) in os.walk(dir):
    for file in files:
      audio = mutagen.File(os.path.join(dir, file))
      if audio is not None:
        return os.path.join(dir, file)
  return None