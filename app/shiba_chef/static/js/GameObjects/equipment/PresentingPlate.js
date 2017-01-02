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

    this.snapX = width/2;
    this.snapY = height/2 -10;
}

PresentingPlate.prototype = new GameObject();
PresentingPlate.prototype.constructor = Grill;

PresentingPlate.prototype.update = function() {

};

PresentingPlate.prototype.dropOnPlate = function(food) {
    //check if next ingredient
    if(Main.recipe.finishIngredient(food.plateName)) {
        Main.shiba.beHappy(1000);
        this.addIngredient(food);
    } else {    //DO NOT MAKE SHIBA CHEF ANGORY WITH YOUR PITIFUL OFFERINGS
        Main.shiba.getAngory(1000);
    }
};

PresentingPlate.prototype.addIngredient = function(food) {
        food.isOnPlate = true;
        //snap food to place and 
        food.x = this.position.x + this.snapX;
        food.y = this.position.y + this.snapY + Main.recipe.ingredients[Main.recipe.currentIngredient].height;
};
