/**
 * Created by jorik on 10-12-2016.
 */
function GameObject() {
    PIXI.Sprite.call(this);


}

GameObject.prototype = new PIXI.Sprite();
GameObject.prototype.constructor = GameObject;

GameObject.prototype.update = function () {

};


