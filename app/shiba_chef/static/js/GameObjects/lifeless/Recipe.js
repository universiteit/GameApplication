function Recipe(stage, items) {
    /* 
    items = {
        'Hamburger' : 15,
        'Pineapple' : 700
    } */
    var self = this;

    this.x = this.y = 20;

    PIXI.Sprite.call(this);

    var stage = stage;

    this.ingredients = {};

    var clear = function() {
        for (var key in this.ingredients) {
            stage.removeChild(this.ingredients[key]['text']);
        }
        this.ingredients = {};
    }

    const offset = 30;

    this.updateText = function() {
        for (var key in this.ingredients) {
            var text = key + ': ' + this.ingredients[key]['done'] + '/' + this.ingredients[key]['required'];
            this.ingredients[key]['text'].text = text;
        }
    }

    var generate = function(json) {
        clear();
        var i = 0;
        for (var key in json) {
            var text = new PIXI.Text();
            text.y = self.y + 15 + (offset * i);
            text.x = self.x + 15;
            this.ingredients[key] = {
                'done' : 0,
                'required' : json[key],
                'text' : text
            };
            stage.addChild(text);
            i++;
        }
        self.updateText();
    }

    var graphics = new PIXI.Graphics();


    graphics.beginFill(0x82562A);
    graphics.drawRoundedRect(this.x, this.y, 200, 350, 15);
    graphics.endFill();

    stage.addChild(graphics);
    generate(items);

}

Recipe.prototype = new GameObject();
Recipe.prototype.constructor = Recipe;


Recipe.prototype.increment = function(ingredient) {
    this.ingredients[ingredient]['done'];
    this.updateText();
}