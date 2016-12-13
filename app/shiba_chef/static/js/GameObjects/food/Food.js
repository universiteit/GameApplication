/**
 * Created by jorik on 10-12-2016.
 */
function Food() {
    GameObject.call(this);

    this.isGrillable = false;
    this.isChoppable = false;
    this.isOnGrill = false;

    this.cookingStatus = 0;

}

Food.prototype = new GameObject();
Food.prototype.constructor = Food;

Food.prototype.update = function () {

};

Food.prototype.onDragMove = function() {
    if (this.dragging)
    {
        var newPosition = this.data.getLocalPosition(this.parent);
        this.position.set(newPosition.x, newPosition.y);
    }
};

Food.prototype.onDragStart = function(event) {
    //make copy of object for next use
    this.copyObject(this);
    // store a reference to the data
    // the reason for this is because of multitouch
    // we want to track the movement of this particular touch
    this.data = event.data;
    this.alpha = 0.5;
    this.dragging = true;
};

Food.prototype.onDragEnd = function() {
    this.alpha = 1;
    this.dragging = false;
    // set the interaction data to null
    this.data = null;
    if(this.overlapsWith(Main.grill) && this.isGrillable) {
        Main.grill.addFood(this);
    } else {
        //remove

        //this.position.set(this.startPositionX, this.startPositionY);
    }
    Main.prototype.removeGameObject(this);
};