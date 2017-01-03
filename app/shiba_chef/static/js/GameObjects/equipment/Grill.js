/**
 * Created by jorik on 8-12-2016.
 */
function Grill(x,y, width, height, texture) {
    PIXI.Sprite.call(this);

    var self = this;

    this.texture = texture;

    this.food = null;
    this.position.x = x;
    this.position.y = y;
    this.width = width;
    this.height = height;

    self.removeFood = function() {
        self.food.off('mousedown', self.removeFood)
                .off('touchstart', self.removeFood);
        self.food = null;
    }
    
}

Grill.prototype = new GameObject();
Grill.prototype.constructor = Grill;

Grill.prototype.update = function() {
    //this.food.forEach(function(food) {
    if(this.food != null) this.food.cookingStatus++;
    //})
};

Grill.prototype.addFood = function(gameObject) {
    this.food = gameObject;
    this.isOnGrill = true;
    // Stop grilling if food is picked up.

    this.food.on('mousedown', this.removeFood)
             .on('touchstart', this.removeFood);
};