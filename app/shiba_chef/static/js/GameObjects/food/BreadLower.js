/**
 * Created by jorik on 8-12-2016.
 */
function BreadLower(x,y, width, height, texture) {
    //PIXI.Sprite.call(this);
    Food.call(this);

    var self = this;

    this.texture = texture;

    //self.bounds = [];
    this.position.x = x;
    this.position.y = y;
    this.width = width;
    this.height = height;

    this.startPositionX = x;
    this.startPositionY = y;

    this.interactive = true;
    this.buttonMode = true;
    this.anchor.set(0.5);

    this
    // events for drag start
    .on('mousedown', this.onDragStart)
    .on('touchstart', this.onDragStart)
    // events for drag end
    .on('mouseup', this.onDragEnd)
    .on('mouseupoutside', this.onDragEnd)
    .on('touchend', this.onDragEnd)
    .on('touchendoutside', this.onDragEnd)
    // events for drag move
    .on('mousemove', this.onDragMove)
    .on('touchmove', this.onDragMove);

}

BreadLower.prototype = new Food();
BreadLower.prototype.constructor = BreadLower;

BreadLower.prototype.update = function() {

};


BreadLower.prototype.copySelfAtLocation = function(self) {
    var newSelf = new BreadLower(self.x, self.y, self.width, self.height, self.texture);
    Main.prototype.addGameObject(newSelf);
};


