QUnit.test("Recipe testing", function( assert ) {
    var ingredients = [
        new Ingredient('BreadLower', 10),
        new Ingredient('Hamburger', 15),
        new Ingredient('BreadUpper', 15)
    ];
    var recipe = new Recipe(new PIXI.Container(), ingredients);

    assert.equal( recipe.finishIngredient('BreadLower'), true, "added correct ingredient successfully!" );

    var correctHeight = 10;
    assert.equal( recipe.getCurrentHeight(), correctHeight, "getting new current ingredient height successfully!" );

    assert.equal( recipe.finishIngredient('Lettuce'), false, "added wrong ingredient successfully!" );

    assert.equal( recipe.getCurrentHeight(), correctHeight, "getting new current ingredient height after placing wrong ingredient successfully!" );

});

QUnit.module( "Foods" );
QUnit.test("")