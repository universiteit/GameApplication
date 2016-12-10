/**
 * Created by jorik on 8-12-2016.
 */
function Hamburger(x,y, width, height, texture) {
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

    //this.cookingStatus = 0;

    this
    // events for drag start
    .on('mousedown', onDragStart)
    .on('touchstart', onDragStart)
    // events for drag end
    .on('mouseup', onDragEnd)
    .on('mouseupoutside', onDragEnd)
    .on('touchend', onDragEnd)
    .on('touchendoutside', onDragEnd)
    // events for drag move
    .on('mousemove', onDragMove)
    .on('touchmove', onDragMove);


   function onDragStart(event) {
        // store a reference to the data
        // the reason for this is because of multitouch
        // we want to track the movement of this particular touch
        this.data = event.data;
        this.alpha = 0.5;
        this.dragging = true;
   }

   function onDragEnd() {
        this.alpha = 1;

        this.dragging = false;

        // set the interaction data to null
        this.data = null;

       if(isAboveGrill(this.position.x, this.position.y, this.width, this.height,
               640, 330, 180, 90)) {

       }else {
           //go back to starting position
           this.position.set(this.startPositionX, this.startPositionY);
       }
    }

    function onDragMove() {
        if (this.dragging)
        {
            var newPosition = this.data.getLocalPosition(this.parent);
            this.position.set(newPosition.x, newPosition.y);
        }
    }

    function isAboveGrill(x1, y1, w1, h1, x2, y2, w2, h2) { //640, 330, 180, 90
        return Collision.OverlapsWith(x1, y1, w1, h1, x2, y2, w2, h2);
        //return (this.position.x > 640 && this.position.x < 820 && this.position.y > 330 && this.position.y < 420);
    }


}

Hamburger.cookingStatus = 0;

Hamburger.prototype.isAboveGrill = function(x1, y1, w1, h1, x2, y2, w2, h2) { //640, 330, 180, 90
    return Collision.OverlapsWith(x1, y1, w1, h1, x2, y2, w2, h2);
    //return (this.position.x > 640 && this.position.x < 820 && this.position.y > 330 && this.position.y < 420);
};

Hamburger.prototype.update = function () {
    if(isAboveGrill()) {
        this.cookingStatus++;
        this.checkCookingStatus();
    }


};

Hamburger.prototype.checkCookingStatus = function () {
    if(this.cookingStatus > 300) {

    }
};

//Hamburger.prototype.onDragStart = function() {
//    // store a reference to the data
//    // the reason for this is because of multitouch
//    // we want to track the movement of this particular touch
//    this.data = event.data;
//    this.alpha = 0.5;
//    this.dragging = true;
//}
//
//Hamburger.prototype.onDragEnd = function() {
//    this.alpha = 1;
//
//    this.dragging = false;
//
//    // set the interaction data to null
//    this.data = null;
//}
//
//Hamburger.prototype.onDragMove = function() {
//    if (this.dragging)
//    {
//        var newPosition = this.data.getLocalPosition(this.parent);
//        this.position.x = newPosition.x;
//        this.position.y = newPosition.y;
//    }
//}

Hamburger.prototype = new Food();
Hamburger.prototype.constructor = Hamburger;