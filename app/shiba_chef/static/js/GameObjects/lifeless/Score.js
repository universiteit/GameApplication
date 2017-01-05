function Score(stage, renderer) {
    var margin = 15;

    this.score = 0;
    this.scoreLabel = new PIXI.Text('Score: ' + this.score);
    this.scoreLabel.anchor.set(1,0);
    this.scoreLabel.position.x = renderer.width - margin;
    this.scoreLabel.position.y = margin;
    stage.addChild(this.scoreLabel);
}

Score.prototype.refresh = function() {
    this.scoreLabel.text = 'Score: ' + this.score;
};

Score.prototype.increment = function() {
    this.score += 25;
    this.refresh();
};

Score.prototype.decrement = function() {
    this.score -= 10;
    this.refresh();
};