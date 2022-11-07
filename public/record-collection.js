
function renderAlbums(albums) {
  container = $('<div class=\'row\'>')
  current_row = $('<div class=\'row\'>')
  for (let i = 0 ; i < albums.length ; i++) {
    album_card = $('<div class=\'album col-3\'>')
    album_card.append('<img class="album-cover" title="' + albums[i].artist + ' - ' + albums[i].title + ' (' + albums[i].date + ')" src="' + albums[i].cover + '" />')
		album_card.append('<p class=\'titel\'>' + albums[i].title + '</p>')
		album_card.append('<p>' + albums[i].artist + '</p>')
    current_row.append(album_card)
    if (i % 4 == 3) {
      current_col = $('<div class=\'col-xl-6\'>')
      current_col.append(current_row)
      container.append(current_col)
      current_row = $('<div class=\'row\'>')
    }
  }
  $('#container').html(container)
}

function getAlbumsByArtistDate(callback) {
  getSortedAlbums(callback, function(a, b) {
    if ( a.artist_sort < b.artist_sort ){
      return -1;
    }
    if ( a.artist_sort > b.artist_sort ){
      return 1;
    }
    if ( a.date < b.date ){
      return -1;
    }
    return 1;
  })
}

function getAlbumsByDateTitle(callback) {
  getSortedAlbums(callback, function(a, b) {
    if ( a.date < b.date ){
      return -1;
    }
    if ( a.date > b.date ){
      return 1;
    }
    if ( a.title < b.title ){
      return -1;
    }
    return 1;
  })
}

function getSortedAlbums(callback, comparisonFunction) {
  $.get('albums.json', function(data) {
    callback(data.sort(comparisonFunction));
  });
}

$(() => {
  getAlbumsByDateTitle(renderAlbums)
})