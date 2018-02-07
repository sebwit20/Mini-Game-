  function Pipe(){

    var spacing = 125;
    var centery = random(spacing, height - spacing);

    this.top =  centery - spacing / 2;
    this.bottom = height - (centery + spacing / 2);
    this.x = width;
    this.w = 50;
    this.speed = 2;
    this.highlight = false;

    this.show = function(){
        fill(color(20, 240, 0));

        if(this.highlight){
            fill(255, 0, 0)
        }
        rect(this.x, 0, this.w, this.top);
        rect(this.x, height - this.bottom, this.w, this.bottom);

    }

    this.update = function(){
        this.x -= this.speed;
    }
    this.offscreen = function(){
        return this.x < -  this.w;
    }
    this.hits = function(bird){
        if(bird.y < this.top || bird.y > height - this.bottom || bird.y - 16 < this.top || bird.y + 16 > height - this.bottom){
            if(bird.x > this.x && bird.x < this.x + this.w){
                this.highlight = true;
                return true;
            }
        }
        this.highlight = false;
        return false;
    }
    this.pass = function(bird){
        if(bird.y > this.top && bird.y < height - this.bottom){
            if(bird.x >this.x && bird.x < this.x + this.w){
                return true;
            }
        }
        return false;
    }
    this.stop = function(bird){
        this.speed = 0;
        this.highlight = false;
        bird.velocity = 0;
        bird.liftForce = 0;
        bird.gravity = 6;
    }
}
