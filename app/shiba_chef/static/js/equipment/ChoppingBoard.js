/**
 * Created by jorik on 8-12-2016.
 */
function ChoppingBoard(x,y, width, height, texture) {
    PIXI.Sprite.call(this);

    //var self = this;

    this.texture = texture;

    //self.bounds = [];
    this.position.x = x;
    this.position.y = y;
    this.width = width;
    this.height = height;
}

ChoppingBoard.prototype = Object.create(PIXI.Sprite.prototype);
ChoppingBoard.prototype.constructor = ChoppingBoard;
