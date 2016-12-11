/**
 * Created by jorik on 10-12-2016.
 */
function Food() {
    GameObject.call(this);

    this.isGrillable = false;

}

Food.prototype = new GameObject();
Food.prototype.constructor = Food;

Food.prototype.update = function () {

};
