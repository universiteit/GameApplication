/**
 * Created by jorik on 8-12-2016.
 */
function Table(x,y, width, height, texture) {
    PIXI.Sprite.call(this);

    //var self = this;

    this.texture = texture;

    //self.bounds = [];
    this.position.x = x;
    this.position.y = y;
    this.width = width;
    this.height = height;
}

Table.prototype = new GameObject();
Table.prototype.constructor = Table;

Table.prototype.update = function() {

};
