var style = {
    fontFamily: 'Arial',
    fontSize: '18px'
}


function Recipe(stage, items) {
    PIXI.Sprite.call(this);
    
    const offset = 30;

    var self = this;

    this.x = this.y = 20;

    var stage = stage;

    var clear = function() {
        for (var key in self.ingredients) {
            stage.removeChild(self.ingredients[key]['text']);
        }
        self.ingredients = {};
    }

    this.updateText = function() {
        for (var key in this.ingredients) {
            var text = key + ': ' + self.ingredients[key]['done'] + '/' + this.ingredients[key]['required'];
            self.ingredients[key]['text'].text = text;
        }
    }

    var generate = function(json) {
        clear();
        var i = 0;
        for (var key in json) {
            var text = new PIXI.Text('', style);
            text.y = self.y + 15 + (offset * i);
            text.x = self.x + 15;
            self.ingredients[key] = {
                'done' : 0,
                'required' : json[key],
                'text' : text
            };
            stage.addChild(text);
            i++;
        }
        self.updateText();
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

Recipe.prototype.ingredients = {};

Recipe.prototype.increment = function(ingredient) {
    if (!(ingredient in this.ingredients))
        return false;
    if (this.ingredients[ingredient].done + 1 > this.ingredients[ingredient].required)
        return false;
    this.ingredients[ingredient].done++;
    this.updateText();
    return true;
}

Recipe.prototype.isDone = function() {
    for (key in this.ingredients) {
        var done = this.ingredients[key].done;
        var required = this.ingredients[key].required;
        if (done != required)
            return false;
    }
    return true;
}