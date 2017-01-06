QUnit.module( "General game objects" ); ////////////////////////////////////////////////////////////////////////////////

QUnit.test("GameObject testing", function( assert ) {
    assert.ok(false, "This always fails, also Daniel is gay 8=====D~~~~~");
    var lettuce = new Lettuce(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    var hamburger = new Hamburger(0, 10, 100, 100, PIXI.Texture.fromImage('bread-lower'));

    assert.ok( lettuce.overlapsWith(hamburger), "testing correctly overlapping game objects successfully!" );

    var lettuce = new Lettuce(300, 300, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    var hamburger = new Hamburger(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));

    assert.notOk( lettuce.overlapsWith(hamburger), "testing not overlapping game objects successfully!" );

});
QUnit.test("Shiba Chef testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');

    var shiba = new ShibaChef(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    assert.ok (
        shiba.x == x &&
            shiba.y == y &&
            shiba.width == width &&
            shiba.height == height &&
            shiba.texture == texture &&
            shiba.shibaStatus == 0
        , "testing constructor of shiba was successful!"
    );

    shiba.shibaStatus = 2;
    shiba.update();

    assert.equal( shiba.texture, PIXI.Texture.fromImage("shiba-angry"), "tested shiba update function successfully!");

    shiba.beHappy(1);
    assert.equal(shiba.shibaStatus, 1, "tested shiba happy animation successfully!");

    Main.score = new Score(Main.stage, Main.renderer);
    shiba.getAngory(1);
    assert.equal(shiba.shibaStatus, 2, "tested shiba angry animation successfully!");

});

QUnit.module( "Equipment" ); ///////////////////////////////////////////////////////////////////////////////////////////
QUnit.test("Bin testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');

    var bin = new Bin(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    assert.ok (
        bin.x == x &&
        bin.y == y &&
        bin.width == width &&
        bin.height == height &&
        bin.texture == texture
        , "testing constructor of bim was successful!"
    );

});
QUnit.test("Choppingboard testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');

    var choppingBoard = new ChoppingBoard(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    assert.ok (
        choppingBoard.x == x &&
        choppingBoard.y == y &&
        choppingBoard.width == width &&
        choppingBoard.height == height &&
        choppingBoard.texture == texture
        , "testing constructor of choppingBoard was successful!"
    );
    var hamburger = new Hamburger(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));

    choppingBoard.addFood(hamburger);

    assert.equal( choppingBoard.food, hamburger, "added food to chopping board successfully!" );

    choppingBoard.update();

    assert.ok( choppingBoard.food.choppingStatus > 0, "updated food on chopping board successfully!" );

    choppingBoard.removeFood();

    assert.equal( choppingBoard.food, null, "removed food from chopping board successfully!");

});
QUnit.test("Grill testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');

    var grill = new Grill(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    assert.ok (
        grill.x == x &&
        grill.y == y &&
        grill.width == width &&
        grill.height == height &&
        grill.texture == texture
        , "testing constructor of grill was successful!"
    );
    var hamburger = new Hamburger(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));

    grill.addFood(hamburger);

    assert.equal( grill.food, hamburger, "added food to grill successfully!" );

    grill.update();

    assert.ok( grill.food.cookingStatus > 0, "updated food on grill successfully!" );

    grill.removeFood();

    assert.equal( grill.food, null, "removed food from grill successfully!");
});
QUnit.test("Presenting plate testing", function( assert ) {

    var ingredients = [
        new Ingredient('Lower bun', 0),
        new Ingredient('Hamburger', 15, { grilled: true }),
        new Ingredient('Lower bun', 15),
        new Ingredient('Hamburger', 15, { grilled: true }),
        new Ingredient('Upper bun', 15)
    ];

    Main.recipe = new Recipe(Main.stage, ingredients);
    Main.score = new Score(Main.stage, Main.renderer);

    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');

    var plate = new PresentingPlate(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    assert.ok (
        plate.x == x &&
        plate.y == y &&
        plate.width == width &&
        plate.height == height &&
        plate.texture == texture
        , "testing constructor of plate was successful!"
    );
    var hamburger = new Hamburger(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));

    plate.addIngredient(hamburger);

    assert.ok( hamburger.isOnPlate && Main.score.score == 25, "adding ingredient to plate tested successfully!");

    var ingredients = [
        new Ingredient('Hamburger', 15, { grilled: false }),
        new Ingredient('Lettuce', 15)
    ];

    Main.recipe = new Recipe(Main.stage, ingredients);
    Main.score = new Score(Main.stage, Main.renderer);
    Main.shiba = new ShibaChef(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    plate.dropOnPlate(hamburger);
    assert.equal( Main.score.score, 25, "dropping correct object on plate tested successfully!" );

    var wrongFood = new BreadLower(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    plate.dropOnPlate(wrongFood);
    assert.equal( Main.score.score, 15, "dropping wrong object on plate tested successfully!" );

});

QUnit.module( "Food" ); ////////////////////////////////////////////////////////////////////////////////////////////////
QUnit.test("Food object testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');
    var hamburger = new Hamburger(x, y, width, height, texture);

    testFoodConstructor(hamburger, x, y, width, height, texture, assert);

    var event = new GameObject();
    event.data = 1;
    hamburger.onDragStart(event);

    assert.ok(hamburger.dragging == true && hamburger.isInDrawer == false, "tested drag start of food object successfully");

    Main.choppingBoard = new ChoppingBoard(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    Main.grill = new Grill(0, 0, 100, 100, PIXI.Texture.fromImage('bread-lower'));
    hamburger.onDragEnd();
    assert.ok(hamburger.dragging == false && hamburger.alpha == 1.0, "tested drag end of food object successfully!");

});
QUnit.test("BreadLower testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');
    var breadLower = new BreadLower(x, y, width, height, texture);

    testFoodConstructor(breadLower, x, y, width, height, texture, assert);

    testCopySelfForFood(breadLower, assert);
});
QUnit.test("BreadUpper testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');
    var breadUpper = new BreadUpper(x, y, width, height, texture);

    testFoodConstructor(breadUpper, x, y, width, height, texture, assert);

    testCopySelfForFood(breadUpper, assert);
});
QUnit.test("Hamburger testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');
    var hamburger = new Hamburger(x, y, width, height, texture);

    testFoodConstructor(hamburger, x, y, width, height, texture, assert);

    testCopySelfForFood(hamburger, assert);

    hamburger.cookingStatus = 600;
    hamburger.checkCookingStatus();

    assert.ok( hamburger.isGrilled, "tested checking cooking status on grilled burger successfully!" );

    hamburger.cookingStatus = 1100;
    hamburger.checkCookingStatus();

    assert.notOk (hamburger.isGrilled, "tested checking cooking status on burned burger successfully!");
});
QUnit.test("Lettuce testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');
    var lettuce = new Lettuce(x, y, width, height, texture);

    testFoodConstructor(lettuce, x, y, width, height, texture, assert);

    testCopySelfForFood(lettuce, assert);

    lettuce.choppingStatus = 600;
    lettuce.checkChoppingStatus();

    assert.ok( lettuce.isChopped, "tested checking chopping status on chopped lettuce successfully!" );
});
QUnit.test("Pepper testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');
    var pepper = new Pepper(x, y, width, height, texture);

    testFoodConstructor(pepper, x, y, width, height, texture, assert);

    testCopySelfForFood(pepper, assert);
});
QUnit.test("Salt testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');
    var salt = new Salt(x, y, width, height, texture);

    testFoodConstructor(salt, x, y, width, height, texture, assert);

    testCopySelfForFood(salt, assert);
});
QUnit.test("Tomato testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');
    var tomato = new Tomato(x, y, width, height, texture);

    testFoodConstructor(tomato, x, y, width, height, texture, assert);

    testCopySelfForFood(tomato, assert);

    tomato.choppingStatus = 600;
    tomato.checkChoppingStatus();

    assert.ok( tomato.isChopped, "tested checking chopping status on chopped tomato successfully!" );
});

QUnit.module( "Lifeless" ); ////////////////////////////////////////////////////////////////////////////////////////////
QUnit.test("Ingredient testing", function( assert ) {
    var name = 'Hamburger';
    var height = 10;
    var options = {
        grilled: true,
        chopped: false
    };
    var style = {
        fontFamily: 'Arial',
        fontSize: '18px'
    };
    var ingredientHamburger = new Ingredient(name, height, options);

    assert.ok (
        ingredientHamburger.name == name &&
        ingredientHamburger.height == height
        , "testing constructor of ingredient was successful!"
    );

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
    var stage = new PIXI.Container();
    var recipe = new Recipe(stage, ingredients);
    assert.ok (
        recipe.x == 20 &&
        recipe.y == 20 &&
        recipe.ingredients == ingredients
        , "testing constructor of recipe was successful!"
    );

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
    assert.ok (
        score.score == 0 &&
        score.scoreLabel.text == 'Score: 0'
        , "testing constructor of score was successful!"
    );

    score.increment();
    assert.equal( score.score, 25, "incrementing score tested successfully!" );
    score.decrement();
    assert.equal( score.score, 15, "decrementing score tested successfully!" );

    score.score = 100;
    score.refresh();
    assert.equal(score.scoreLabel.text, 'Score: 100', "refreshing score label tested successfully!");
});
QUnit.test("Table testing", function( assert ) {
    var x = 0;
    var y = 0;
    var width = 100;
    var height = 100;
    var texture = PIXI.Texture.fromImage('bread-lower');
    var table = new Table(x, y, width, height, texture);

    assert.ok (
        table.x == x &&
        table.y == y &&
        table.width == width &&
        table.height == height &&
        table.texture == texture
        , "testing constructor of table was successful!"
    )

});

////////////////////////////////////////////////// HELPER FUNCTIONS /////////////////////////////////////////
var makeMain = function() {
    var main = new Main();
    main.stage = new PIXI.Container();

    var ingredients = [
        new Ingredient('Lower bun', 0),
        new Ingredient('Hamburger', 15, { grilled: true }),
        new Ingredient('Lower bun', 15),
        new Ingredient('Hamburger', 15, { grilled: true }),
        new Ingredient('Upper bun', 15)
    ];

    main.recipe = new Recipe(main.stage, ingredients);

    return main;
};

function testCopySelfForFood(food, assert) {
    var objectListSize = Main.gameObjects.length;
    food.copySelfAtLocation(food);

    assert.equal(Main.gameObjects.length, objectListSize+1, "tested copying self of "+food.name+ " successfully!");

}

function testFoodConstructor(madeFood, x, y, width, height, texture, assert) {
    assert.ok (
        madeFood.x == x &&
            madeFood.y == y &&
            madeFood.width == width &&
            madeFood.height == height &&
            madeFood.texture == texture &&
            madeFood.interactive == true &&
            madeFood.buttonMode == true
        , "testing constructor of " + madeFood.name + " was successful!"
    )
}