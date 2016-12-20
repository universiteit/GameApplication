/**
 * Created by jorik on 13-12-2016.
 */
function Bin(x,y, width, height, texture) {
    PIXI.Sprite.call(this);

    this.texture = texture;

    this.position.x = x;
    this.position.y = y;
    this.width = width;
    this.height = height;
}

Bin.prototype = new GameObject();
Bin.prototype.constructor = Bin;

Bin.prototype.update = function() {

};
