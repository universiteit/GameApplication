/**
 * Created by jorik on 8-12-2016.
 */
function Grill(x,y, width, height, texture) {
    PIXI.Sprite.call(this);

    //var self = this;

    this.texture = texture;

    //self.bounds = [];
    this.position.x = x;
    this.position.y = y;
    this.width = width;
    this.height = height;

    function updateSelf() {

    }
}

Grill.prototype = Object.create(PIXI.Sprite.prototype);
Grill.prototype.constructor = Grill;

//Grill.inherits(PIXI.Container);

//Pixi.Container.prototype.overlapsWith()