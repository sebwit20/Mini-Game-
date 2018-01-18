function Bird(){
    this.y = height / 2;
    this.x = 64;

    this.gravity = 0.6;
    this.liftForce = -15;
    this.velocity = 0;

    this.show = function(){
        fill(color(255, 255, 0));
        ellipse(this.x, this.y, 32, 32);
    }

    this.update = function(){
        this.velocity += this.gravity;
        this.velocity *= 0.9;
        this.y += this.velocity;

        if(this.y >= height){
            this.y = height - 10;
            this.velocity = 0;
        }

        if(this.y < 0){
            this.y = 0;
            this.velocity = 0;
        }
    }
    this.up = function (){
        this.velocity += this.liftForce;
    }

}
