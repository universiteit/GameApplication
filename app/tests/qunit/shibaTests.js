

QUnit.module( "Equipment" ); ///////////////////////////////////////////////////////////////////////////////////////////
//QUnit.test("Bin testing", function( assert ) {
//    var bin = new Bin(0, 0, 100, 100,PIXI.Texture.fromImage('bread-lower'));
//
//    assert.equal( bin, bin, "hey");
//});
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
    var grill = new Grill(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    var hamburger = new Hamburger(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));

    grill.addFood(hamburger);

    assert.equal( grill.food, hamburger, "added food to grill successfully!" );

    grill.update();

    assert.ok( grill.food.cookingStatus > 0, "updated food on grill successfully!" );

    grill.removeFood();

    assert.equal( grill.food, null, "removed food from gril successfully!");
});
QUnit.test("Presenting plate testing", function( assert ) {
    var plate = new PresentingPlate(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));

    assert.equal( 1, 1, "hey");
});

QUnit.module( "Food" ); ////////////////////////////////////////////////////////////////////////////////////////////////
QUnit.test("BreadLower testing", function( assert ) {
    assert.equal( 1, 1, "hey");
});

QUnit.module( "Lifeless" ); ////////////////////////////////////////////////////////////////////////////////////////////
QUnit.test("Ingredient testing", function( assert ) {
    var ingredientHamburger = new Ingredient('Hamburger', 10, {
        grilled: true,
        chopped: false
    });

    var hamburger = new Hamburger(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    assert.notOk( ingredientHamburger.isIngredient(hamburger), "Testing if wrong object is not correct in ingredient was successful!" );
    hamburger.isGrilled = true;

    assert.ok( ingredientHamburger.isIngredient(hamburger), "Testing if object is correct object mentioned in ingredient was successful!" );

    ingredientHamburger.done();
    assert.equal(ingredientHamburger.text.style.fill, '#33f74a', "testing if ingredient changed correctly after labeled done successful!")

});
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

    recipe.finishIngredient(new Hamburger(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower')));
    recipe.finishIngredient(new BreadUpper(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower')));
    assert.ok( recipe.isDone(), "Recipe correctly shows as done after adding all of the right ingredients!" );
});
QUnit.test("Score testing", function( assert ) {
    var score = new Score(new PIXI.Container(), PIXI.autoDetectRenderer(
        1200,
        720
    ));

    score.increment();
    assert.equal( score.score, 25, "incrementing score tested successfully!" );
    score.decrement();
    assert.equal( score.score, 15, "decrementing score tested successfully!" );

    score.score = 100;
    score.refresh();
    assert.equal(score.scoreLabel.text, 'Score: 100', "refreshing score label tested successfully!");
});