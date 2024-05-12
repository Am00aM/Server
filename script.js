const car = document.getElementById('car');
const obstacle = document.getElementById('obstacle');

function moveLeft() {
  let leftPosition = parseInt(window.getComputedStyle(car).getPropertyValue('left'));
  if (leftPosition > 0) {
    car.style.left = ${leftPosition - 10}px;
  }
}

function moveRight() {
  let leftPosition = parseInt(window.getComputedStyle(car).getPropertyValue('left'));
  if (leftPosition < 250) {
    car.style.left = ${leftPosition + 10}px;
  }
}

function moveObstacle() {
  let topPosition = parseInt(window.getComputedStyle(obstacle).getPropertyValue('top'));
  obstacle.style.top = ${topPosition + 5}px;

  if (topPosition > 400) {
    obstacle.style.top = '-50px';
  }

  if (checkCollision()) {
    alert('Game Over! 😵');
    car.style.left = '50%';
  }

  requestAnimationFrame(moveObstacle);
}

function checkCollision() {
  let carRect = car.getBoundingClientRect();
  let obstacleRect = obstacle.getBoundingClientRect();

  return !(
    carRect.bottom < obstacleRect.top ||
    carRect.top > obstacleRect.bottom ||
    carRect.right < obstacleRect.left ||
    carRect.left > obstacleRect.right
  );
}

moveObstacle();
