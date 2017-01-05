/**
 * Created by jorik on 10-12-2016.
 */

Main.stage = null;
Main.renderer = null;

function Main() {
    Main.stage = new PIXI.Container();
    Main.renderer = PIXI.autoDetectRenderer(
        1200,
        720
    );

    Main.renderer.backgroundColor = 0xB7E3E6;
    document.body.appendChild(Main.renderer.view);

    this.loadSpriteSheet();
}

Main.presentingPlate = null;
Main.choppingBoard = null;
Main.grill = null;
Main.shiba = null;
Main.bin = null;
Main.gameObjects = [];

Main.recipe = null;
Main.score = null;

Main.finishGame = function() {
    $.ajax({
        type: 'POST',
        url: '/shiba_chef/score',
        contentType: 'application/json',
        data: JSON.stringify({
            score: Main.score.score
        })
    });

    Main.stage = new PIXI.Container();
    var stage = Main.stage;
    
    var style = {
        align: 'center'
    }
    var message = 'You win!\nScore: ' + this.score.score;
    var winText = new PIXI.Text(message, style);
    winText.anchor.set(0.5, 0.5);
    winText.position.x = Main.renderer.width / 2;
    winText.position.y = Main.renderer.height / 2;

    var retryButton = new PIXI.Graphics();
    retryButton.beginFill(0xAAAAAA);
    retryButton.lineStyle(1, 0xFFFFFF);
    retryButton.drawRoundedRect(winText.position.x - 100, winText.position.y + 100, 200, 75, 5);
    retryButton.endFill();

    var retryText = new PIXI.Text('Retry');
    retryText.position.x = winText.position.x - 100 + (retryButton.width / 2);
    retryText.position.y = winText.position.y + 100 + (retryButton.height / 2);
    retryText.style.fill = 0x000000;
    retryText.anchor.set(0.5, 0.5);

    retryButton.interactive = true;
    retryButton.on('mousedown', function() {
        Main.retry();
    });


    stage.addChild(retryButton);
    stage.addChild(retryText);
    stage.addChild(winText);
}

Main.retry = function() {
    Main.stage = new PIXI.Container();
    Main.gameObjects = [];
    main.makeWorld();
}

Main.prototype.update = function() {
    //update game objects
    Main.gameObjects.forEach(function(gameObject) {
        if(gameObject == undefined) {
            Main.prototype.removeGameObject(gameObject);
        } else {
            gameObject.update();
        }
    });
    Main.renderer.render(Main.stage);
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
    loader.add('presenting-plate', '../img/equipment/presenting-plate.png');

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

    //presenting plate
    Main.presentingPlate = new PresentingPlate(450, 320, 150, 90, PIXI.Texture.fromImage('presenting-plate'));
    Main.gameObjects.push(Main.presentingPlate);

    //chopping board
    Main.choppingBoard = new ChoppingBoard(260, 345, 190, 80, PIXI.Texture.fromImage('choppingBoard'));
    Main.gameObjects.push(Main.choppingBoard);

    //grill
    Main.grill = new Grill(630, 340, 200, 70, PIXI.Texture.fromImage('grill'));
    Main.gameObjects.push(Main.grill);

    // Recipe

    var ingredients = [
        new Ingredient('Lower bun', 0),
        new Ingredient('Hamburger', 15, { grilled: true }),
        new Ingredient('Lower bun', 15),
        new Ingredient('Hamburger', 15, { grilled: true }),
        new Ingredient('Upper bun', 15)
    ];

    Main.recipe = new Recipe(Main.stage, ingredients);

    Main.score = new Score(Main.stage, Main.renderer);

    //bin
    Main.bin = new Bin(100, 350, 150, 150, PIXI.Texture.fromImage('bin'));
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

Main.prototype.moveFoodToTop = function(food) {
    Main.stage.removeChild(food);
    Main.stage.addChild(food);
};