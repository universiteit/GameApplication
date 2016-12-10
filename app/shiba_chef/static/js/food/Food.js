/**
 * Created by jorik on 10-12-2016.
 */
function Food() {
    GameObject.call(this);

}

Food.prototype.update = function () {

};

Food.prototype = new GameObject();
Food.prototype.constructor = Food;