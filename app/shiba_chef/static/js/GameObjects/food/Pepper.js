/**
 * Created by jorik on 8-12-2016.
 */
function Pepper(x,y, width, height, texture) {
    //PIXI.Sprite.call(this);
    Food.call(this);

    var self = this;

    this.name = 'Pepper';

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

Pepper.prototype = new Food();
Pepper.prototype.constructor = Pepper;

Pepper.prototype.update = function() {

};


Pepper.prototype.copySelfAtLocation = function(self) {
    var newSelf = new Pepper(self.x, self.y, self.width, self.height, self.texture);
    Main.prototype.addGameObject(newSelf);
};


