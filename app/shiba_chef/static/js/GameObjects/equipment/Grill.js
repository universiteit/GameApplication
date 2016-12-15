/**
 * Created by jorik on 8-12-2016.
 */
function Grill(x,y, width, height, texture) {
    PIXI.Sprite.call(this);

    //var self = this;

    this.texture = texture;

    this.food = null;
    this.position.x = x;
    this.position.y = y;
    this.width = width;
    this.height = height;
}

Grill.prototype = new GameObject();
Grill.prototype.constructor = Grill;

Grill.prototype.update = function() {
    //this.food.forEach(function(food) {
    if(this.food) this.food.cookingStatus++;
    //})
};

Grill.prototype.addFood = function(gameObject) {
    this.food = gameObject;
};

Grill.prototype.removeFood = function(gameObject) {
    this.food = null;
};

//Grill.inherits(PIXI.Container);

//Pixi.Container.prototype.overlapsWith()