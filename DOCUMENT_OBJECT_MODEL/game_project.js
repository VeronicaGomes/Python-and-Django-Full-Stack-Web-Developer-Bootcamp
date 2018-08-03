
var tile = document.querySelectorAll('td');

for (var i = 0; i < tile.length; i++) {

  tile[i].addEventListener('click', function() {
    if (this.textContent === ' ') {
      this.textContent = 'X';
    }else if (this.textContent === 'X') {
      this.textContent = 'O';
    }else {
      this.textContent = ' ';
    }
  });

}
