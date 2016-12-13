/**
 * Created by jorik on 8-12-2016.
 */
function Grill(x,y, width, height, texture) {
    PIXI.Sprite.call(this);

    //var self = this;

    this.texture = texture;

    this.food = [];

    //self.bounds = [];
    this.position.x = x;
    this.position.y = y;
    this.width = width;
    this.height = height;
}

Grill.prototype = new GameObject();
Grill.prototype.constructor = Grill;

Grill.prototype.update = function() {

};

Grill.prototype.addFood = function() {

}
//Grill.inherits(PIXI.Container);

//Pixi.Container.prototype.overlapsWith()