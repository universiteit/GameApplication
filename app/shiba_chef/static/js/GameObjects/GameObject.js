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

GameObject.prototype.overlapsWith = function(gameObject) {
    return (
        (this.x + this.width > gameObject.x)
        && (this.x < gameObject.x + gameObject.width)
        && (this.y + this.height > gameObject.y)
        && (this.y < gameObject.y + gameObject.height)
    );
};

GameObject.prototype.copyObject = function(gameObject) {
    Main.prototype.addGameObject(Object.assign({}, gameObject));
    //gameObject.copy());
};


