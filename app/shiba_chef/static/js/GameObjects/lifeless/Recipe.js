function Recipe(stage, items) {
    PIXI.Sprite.call(this);

    var graphics = new PIXI.Graphics();

    graphics.beginFill(0x8E8E8E);
    
    graphics.drawRect(20, 20, 200, 350);
    graphics.endFill();

    stage.addChild(graphics);

}

Recipe.prototype = new GameObject();
Recipe.prototype.constructor = Recipe;