QUnit.test("Recipe testing", function( assert ) {
    var ingredients = [
        new Ingredient('Lower bun', 10),
        new Ingredient('Hamburger', 15),
        new Ingredient('Upper bun', 15)
    ];
    var recipe = new Recipe(new PIXI.Container(), ingredients);

    var breadLower = new BreadLower(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    assert.equal( recipe.finishIngredient(breadLower), true, "added correct ingredient successfully!" );

    var correctHeight = 10;
    assert.equal( recipe.getCurrentHeight(), correctHeight, "getting new current ingredient height successfully!" );

    var lettuce = new Lettuce(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    assert.equal( recipe.finishIngredient(lettuce), false, "added wrong ingredient successfully!" );

    assert.equal( recipe.getCurrentHeight(), correctHeight, "getting new current ingredient height after placing wrong ingredient successfully!" );

});

QUnit.module( "Equipment" );
QUnit.test("Bin testing", function( assert ) {
    var bin = new Bin(0, 0, 100, 100,PIXI.Texture.fromImage('bread-lower'));

    assert.equal( 1, 1, "hey");
});
QUnit.test("Choppingboard testing", function( assert ) {
    var choppingBoard = new ChoppingBoard(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    var hamburger = new Hamburger(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));

    choppingBoard.addFood(hamburger);

    assert.equal( choppingBoard.food, hamburger, "added food to chopping board successfully!" );

    choppingBoard.update();

    assert.ok( choppingBoard.food.choppingStatus > 0, "updated food on chopping board successfully!" );

    choppingBoard.removeFood();

    assert.equal( choppingBoard.food, null, "removed food from chopping board successfully!");

});
QUnit.test("Grill testing", function( assert ) {
    assert.equal( 1, 1, "hey");
});
QUnit.test("Presenting plate testing", function( assert ) {
    assert.equal( 1, 1, "hey");
});