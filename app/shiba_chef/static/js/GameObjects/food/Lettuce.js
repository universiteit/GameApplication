/**
 * Created by jorik on 8-12-2016.
 */
function Lettuce(x,y, width, height, texture) {
    //PIXI.Sprite.call(this);
    Food.call(this);

    var self = this;

    this.name = 'Lettuce';

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

    this.isChoppable = true;

}

Lettuce.prototype = new Food();
Lettuce.prototype.constructor = Lettuce;

Lettuce.prototype.update = function() {
    if(this.isOnChoppingBoard) {
        this.checkChoppingStatus();
    }
};


Lettuce.prototype.copySelfAtLocation = function(self) {
    var newSelf = new Lettuce(self.x, self.y, self.width, self.height, self.texture);
    Main.prototype.addGameObject(newSelf);
};

Lettuce.prototype.checkChoppingStatus = function() {
    if(!this.isChopped) {
        if (this.choppingStatus > 200) {
            this.texture = PIXI.Texture.fromImage("lettuce-cut");
            this.isChopped = true;
        } else {
            this.texture = PIXI.Texture.fromImage("lettuce");
        }
    }
};
