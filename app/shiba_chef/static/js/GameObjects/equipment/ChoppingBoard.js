/**
 * Created by jorik on 8-12-2016.
 */
function ChoppingBoard(x,y, width, height, texture) {
    PIXI.Sprite.call(this);

    //var self = this;

    this.texture = texture;

    this.food = null;

    //self.bounds = [];
    this.position.x = x;
    this.position.y = y;
    this.width = width;
    this.height = height;
}

ChoppingBoard.prototype = new GameObject();
ChoppingBoard.prototype.constructor = ChoppingBoard;

ChoppingBoard.prototype.update = function() {
    if(this.food) this.food.choppingStatus++;
};

ChoppingBoard.prototype.addFood = function(gameObject) {
    //delete original food
    Main.prototype.removeGameObject(this.food);
    gameObject.isOnChoppingBoard = true;
    this.food = gameObject;
};

ChoppingBoard.prototype.removeFood = function() {
   this.food = null;
};