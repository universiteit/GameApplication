/**
 * Created by jorik on 10-12-2016.
 */

Main.stage = null;

function Main() {
    Main.stage = new PIXI.Container();
    this.renderer = PIXI.autoDetectRenderer(
        1200,
        720
    );

    this.renderer.backgroundColor = 0xB7E3E6;
    document.body.appendChild(this.renderer.view);

    this.loadSpriteSheet();
}

Main.choppingBoard = null;
Main.grill = null;
Main.shiba = null;
Main.bin = null;
Main.gameObjects = [];

Main.recipe = null;

Main.prototype.update = function() {
    //update game objects
    Main.gameObjects.forEach(function(gameObject) {
        if(gameObject == undefined) {
            Main.prototype.removeGameObject(gameObject);
        } else {
            gameObject.update();
        }
    });
    this.renderer.render(Main.stage);
    requestAnimationFrame(this.update.bind(this));
};

Main.prototype.loadSpriteSheet = function() {
    var loader = PIXI.loader;

    //shiba
    loader.add('shiba-neutral', '../img/DogeDefault.png');
    loader.add('shiba-angry', '../img/DogeAngry.png');
    loader.add('shiba-happy', '../img/DogeHappy.png');

    //equipment
    loader.add('table', '../img/equipment/desk.png');
    loader.add('choppingBoard', '../img/equipment/chopping-board.png');
    loader.add('grill', '../img/equipment/grill.png');
    loader.add('bin', '../img/equipment/bin.png');

    //food
    loader.add('bread-lower', '../img/food/BreadLowerPart.png');
    loader.add('bread-upper', '../img/food/BreadUpperPart.png');
    loader.add('burger-raw', '../img/food/BurgerRaw.png');
    loader.add('burger', '../img/food/Burger.png');
    loader.add('burger-burned', '../img/food/BurgerBurned.png');
    loader.add('eggplant', '../img/food/Eggplant.png');
    loader.add('fish', '../img/food/Fish.png');
    loader.add('lettuce', '../img/food/Lettuce.png');
    loader.add('lettuce-cut', '../img/food/LettucePiece.png');
    loader.add('pepper', '../img/food/Peppered.png');
    loader.add('salt', '../img/food/Salted.png');
    loader.add('legolegoland', '../img/food/Salt.png');
    loader.add('tomato', '../img/food/Tomato.png');
    loader.add('tomato-cut', '../img/food/TomatoSlice.png');

    loader.once("complete", this.spriteSheetLoaded.bind(this));
    loader.load();
};

Main.prototype.spriteSheetLoaded = function() {
    this.makeWorld();

    requestAnimationFrame(this.update.bind(this));
};

Main.prototype.makeWorld = function() {
    this.createShiba();

    this.createEnvironment();

    this.createFood();

    var self = this;
    Main.gameObjects.forEach(function(gameObject) {
        Main.stage.addChild(gameObject);
    });
};

Main.prototype.createEnvironment = function() {
    //lifeless objects

    //table
    var table = new Table(200, 250, 720, 360, PIXI.Texture.fromImage('table'));
    Main.gameObjects.push(table);

    //chopping board
    Main.choppingBoard = new ChoppingBoard(270, 330, 180, 100, PIXI.Texture.fromImage('choppingBoard'));
    Main.gameObjects.push(Main.choppingBoard);

    //grill
    Main.grill = new Grill(640, 330, 180, 90, PIXI.Texture.fromImage('grill'));
    Main.gameObjects.push(Main.grill);

    // Recipe
    Main.recipe = new Recipe(Main.stage, {
        'Hamburger': 50,
        'Pineapple': 700
    });

    var added = Main.recipe.increment('Pineapple');
    var error = Main.recipe.increment('RandomShit');

    //bin
    Main.bin = new Bin(100, 320, 150, 200, PIXI.Texture.fromImage('bin'));
    Main.gameObjects.push(Main.bin);
};

Main.prototype.createShiba = function() {
    Main.shiba = new ShibaChef(400, 80, 280, 330, PIXI.Texture.fromImage("shiba-neutral"));
    Main.gameObjects.push(Main.shiba);
};

Main.prototype.createFood = function() {
    //create rectangle
    var foodRec = new PIXI.Graphics();

    foodRec.beginFill(0x7aabf9);

    // set the line style to have a width of 5 and set the color to red
    foodRec.lineStyle(2, 0x4a699b);

    // draw a rectangle
    foodRec.drawRect(280, 480, 430, 140);

    Main.stage.addChild(foodRec);

    var foodColumns = 4;

    var foodStartX = 360;
    var foodStartY = 520;

    var foodDiffX = 90;
    var foodDiffY = 60;

    var foods = [];
    //define foods
    foods.push(new BreadLower(200, 200, 100, 50, PIXI.Texture.fromImage("bread-lower")));
    foods.push(new BreadUpper(200, 200, 100, 50, PIXI.Texture.fromImage("bread-upper")));
    foods.push(new Lettuce(200, 200, 90, 60, PIXI.Texture.fromImage("lettuce")));
    foods.push(new Tomato(200, 200, 70, 60, PIXI.Texture.fromImage("tomato")));
    foods.push(new Hamburger(200, 200, 70, 50, PIXI.Texture.fromImage("burger-raw")));
    foods.push(new Salt(200, 200, 70, 40, PIXI.Texture.fromImage("salt")));
    foods.push(new Pepper(200, 200, 70, 60, PIXI.Texture.fromImage("pepper")));
    foods.push(new Hamburger(200, 200, 70, 50, PIXI.Texture.fromImage("burger-raw")));

    //push and set positions
    foods.forEach(function(food, index) {
        food.position.x = foodStartX + (foodDiffX * (index % foodColumns));
        food.position.y = foodStartY + (foodDiffY * Math.floor(index / foodColumns));
        //food.position.y = foodStartY;
        Main.gameObjects.push(food);
    });

};

Main.prototype.addGameObject = function(gameObject) {
    Main.gameObjects.push(gameObject);
    Main.stage.addChild(gameObject);
};

Main.prototype.removeGameObject = function(gameObject) {
    var index = Main.gameObjects.indexOf(gameObject);
    if (index > -1) {
        Main.gameObjects.splice(index, 1);
    }
    Main.stage.removeChild(gameObject);
};

Main.prototype.throwFoodInBin = function(food) {
    Main.prototype.removeGameObject(food);
};