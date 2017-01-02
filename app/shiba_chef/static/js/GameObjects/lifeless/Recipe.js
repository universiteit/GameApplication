function Recipe(stage, items) {
    PIXI.Sprite.call(this);
    
    const offset = 30;

    var self = this;

    this.x = this.y = 20;

    var stage = stage;

    var clear = function() {
        self.ingredients.forEach(function(element) {
            stage.removeChild(element.text);
        })
    }

    var generate = function(items) {
        clear();
        items.forEach(function(element, index) {
            element.text.y = self.y + 15 + (offset * index);
            element.text.x = self.x + 15;
            stage.addChild(element.text);
        });
        self.ingredients = items;
    }

    // Background
    var graphics = new PIXI.Graphics();


    graphics.beginFill(0x82562A);
    graphics.drawRoundedRect(this.x, this.y, 200, 350, 15);
    graphics.endFill();

    stage.addChild(graphics);
    generate(items);

}

Recipe.prototype = new GameObject();
Recipe.prototype.constructor = Recipe;

Recipe.prototype.currentIngredient = 0;
Recipe.prototype.ingredients = [];


Recipe.prototype.finishIngredient = function(ingredient) {
    return this.currentIngredient < this.ingredients.length && (this.ingredients[this.currentIngredient].isIngredient(ingredient)) ? ((this.ingredients[this.currentIngredient].done()) | ++this.currentIngredient) > 0 : false // Ask Jorik.
}

Recipe.prototype.getCurrentHeight = function() {
    var height = 0;
    for(var i = 0; i < this.currentIngredient; i++) {
        height += this.ingredients[i].height;
    }
    return height;
}

