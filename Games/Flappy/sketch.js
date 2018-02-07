
var bird;
var pipes = [];
var pipesPassed = 0;
var score = 0;
var gameOver = false;
function setup() {
	createCanvas(400, 600);
	bird = new Bird();
	pipes.push(new Pipe());

}


function draw() {
	background(0);
	fill(255);
	textSize(25);
	text("Score : " + score, 10, 25);

	for(var i = pipes.length-1; i >= 0; i--){
		pipes[i].show();
		pipes[i].update();

		if(pipes[i].hits(bird)){
			gameOver = true;
			break;
		}

		if(pipes[i].offscreen()){
			pipes.splice(i, 1);
		}
	}



	bird.update();
	bird.show();

	if(gameOver == true){
		for(var i = pipes.length - 1; i>= 0; i--){
			pipes[i].stop(bird);
		}
		textSize(30);
		fill(255);
		text("Game Over\nYou scored " + score + " points.\nPress f5 to play again!", 100, 300);
	}
	if(frameCount % 150 == 0 && gameOver == false){
		pipes.push(new Pipe());
		score ++;
	}



}

function keyPressed (){
	if(key === ' '){
		bird.up();
	}
}
