/**
 * Created by jorik on 8-12-2016.
 */
function Hamburger(x,y, width, height, texture) {
    //PIXI.Sprite.call(this);
    Food.call(this);

    var self = this;

    this.plateName = 'Hamburger';

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

    this.isGrillable = true;

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

Hamburger.prototype = new Food();
Hamburger.prototype.constructor = Hamburger;

Hamburger.prototype.update = function() {
    this.checkCookingStatus();

    //console.log(this.cookingStatus);
};

Hamburger.prototype.checkCookingStatus = function() {
    if(this.cookingStatus > 1000) {
        this.texture = PIXI.Texture.fromImage("burger-burned");
        this.isGrilled = false;
    } else if(this.cookingStatus > 500) {
        this.texture = PIXI.Texture.fromImage("burger");
        this.isGrilled = true;
    }

};

Hamburger.prototype.copySelfAtLocation = function(self) {
    var newSelf = new Hamburger(self.x, self.y, self.width, self.height, self.texture);
    Main.prototype.addGameObject(newSelf);
};


