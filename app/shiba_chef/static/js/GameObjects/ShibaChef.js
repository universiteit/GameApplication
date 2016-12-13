/**
 * Created by jorik on 13-12-2016.
 */
function ShibaChef(x,y, width, height, texture) {
    PIXI.Sprite.call(this);

    //var self = this;

    this.texture = texture;

    //self.bounds = [];
    this.position.x = x;
    this.position.y = y;
    this.width = width;
    this.height = height;
}

ShibaChef.prototype = new GameObject();
ShibaChef.prototype.constructor = ShibaChef;

ShibaChef.prototype.update = function() {

};