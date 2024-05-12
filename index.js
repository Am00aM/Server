var dino = document.getElementById('dino');
var gameContainer = document.getElementById('game-container');

function jump() {
  if (dino.classList != 'jump') {
    dino.classList.add('jump');
  
    setTimeout(function() {
      dino.classList.remove('jump');
    }, 300);
  }
}

document.addEventListener('keydown', function(event) {
  jump();
});

gameContainer.addEventListener('click', function() {
  jump();
});
