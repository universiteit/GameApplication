var style = {
    fontFamily: 'Arial',
    fontSize: '18px'
}

function Ingredient(name, height, options) {
    self = this;
    self.name = name;
    self.height = height;
    self.text = new PIXI.Text(name, style);
    var defaults = {
        grilled: false,
        chopped: false
    };
    self.options = Object.assign({}, defaults, options);
}

Ingredient.prototype.isIngredient = function(object) {
    if (this.name != object)
        return false;
    if (this.options.grilled && !object.isGrilled)
        return false;
    if (this.options.chopped && !object.isChopped)
        return false;
    return true;
}

Ingredient.prototype.done = function() {
    this.text.style.fill = 0x33F74A;
}