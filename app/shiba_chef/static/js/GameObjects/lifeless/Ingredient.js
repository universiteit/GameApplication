var style = {
    fontFamily: 'Arial',
    fontSize: '18px'
}

function Ingredient(name, height) {
    self = this;
    self.name = name;
    self.height = height;
    self.text = new PIXI.Text(name, style);
}

Ingredient.prototype.isIngredient = function(object) {
    if (typeof object === 'string')
        return this.name == object;
    return this.name == Object.prototype.toString.call(obj).match(/^\[object\s(.*)\]$/)[1];
}

Ingredient.prototype.done = function() {
    this.text.style.fill = 0x33F74A;
}