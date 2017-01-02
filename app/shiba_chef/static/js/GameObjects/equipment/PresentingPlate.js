/**
 * Created by jorik on 8-12-2016.
 */
function PresentingPlate(x,y, width, height, texture) {
    PIXI.Sprite.call(this);

    this.ingredients = [];

    this.texture = texture;

    this.food = null;
    this.position.x = x;
    this.position.y = y;
    this.width = width;
    this.height = height;
}

PresentingPlate.prototype = new GameObject();
PresentingPlate.prototype.constructor = Grill;

PresentingPlate.prototype.update = function() {

};

PresentingPlate.prototype.dropOnPlate = function(food) {

};

PresentingPlate.prototype.addIngredient = function(food) {

};
