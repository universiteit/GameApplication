/**
 * Created by jorik on 10-12-2016.
 */
function Food() {
    GameObject.call(this);

    this.plateName = null;

    this.isGrillable = false;
    this.isChoppable = false;

    this.isOnGrill = false;
    this.isOnChoppingBoard = false;
    this.isInDrawer = true;
    this.isOnPlate = false;

    this.isChopped = false;

    this.cookingStatus = 0;
    this.choppingStatus = 0;

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
    //if not on equipment, make copy of object for next use
    if(this.isInDrawer) {
        this.copySelfAtLocation(this);
        this.isInDrawer = false;
    } else if(this.isOnGrill) {
        Main.grill.removeFood(this);
        this.isOnGrill = false;
    } else if(this.isOnChoppingBoard) {
        Main.choppingBoard.removeFood(this);
        this.isOnChoppingBoard = false;
    } else if(this.isOnPlate) {
        //not touchable, already part of the recipe
        return;
    }
    // store a reference to the data
    // the reason for this is because of multitouch
    // we want to track the movement of this particular touch
    this.data = event.data;
    this.alpha = 0.9;
    this.dragging = true;
};

Food.prototype.onDragEnd = function() {
    this.alpha = 1;
    this.dragging = false;
    // set the interaction data to null
    this.data = null;
    if(this.overlapsWith(Main.grill) && this.isGrillable) { //place in grill
        Main.grill.addFood(this);
        this.isInDrawer = false;
    } else if(this.overlapsWith(Main.choppingBoard) && this.isChoppable) {  //place in chopping board
        Main.choppingBoard.addFood(this);
        this.isInDrawer = false;
    } else if(this.overlapsWith(Main.bin)) {    //place in bin
        Main.prototype.throwFoodInBin(this);
    } else if(this.overlapsWith(Main.presentingPlate)) {    //place on plate
        Main.presentingPlate.dropOnPlate(this);
    } else {    //place outside of all equipment
        //remove self
        //Main.prototype.removeGameObject(this);
    }

};

Food.prototype.copySelfAtLocation = function() {

};