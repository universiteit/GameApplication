/**
 * Created by jorik on 8-12-2016.
 */
function BreadUpper(x,y, width, height, texture) {
    //PIXI.Sprite.call(this);
    Food.call(this);

    var self = this;

    this.name = 'Upper bun';

    this.texture = texture;

    //self.bounds = [];
    this.position.x = x;
    this.position.y = y;
    this.width = width;
    this.height = height;

    this.startPositionX = x;
    this.startPositionY = y;

    this.interactive = true;
    this.buttonMode = true;
    this.anchor.set(0.5);

}

BreadUpper.prototype = new Food();
BreadUpper.prototype.constructor = BreadUpper;

BreadUpper.prototype.update = function() {

};


BreadUpper.prototype.copySelfAtLocation = function(self) {
    var newSelf = new BreadUpper(self.x, self.y, self.width, self.height, self.texture);
    Main.prototype.addGameObject(newSelf);
};


