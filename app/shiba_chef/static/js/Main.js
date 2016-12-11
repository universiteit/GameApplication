/**
 * Created by jorik on 10-12-2016.
 */
function Main() {
    this.stage = new PIXI.Container();
    this.renderer = PIXI.autoDetectRenderer(
        1200,
        720
    );

    this.gameObjects = [];

    this.renderer.backgroundColor = 0xB7E3E6;
    document.body.appendChild(this.renderer.view);

    this.loadSpriteSheet();
}

Main.prototype.update = function() {
    //update game objects
    this.gameObjects.forEach(function(gameObject) {
        gameObject.update();
    });
    this.renderer.render(this.stage);
    requestAnimationFrame(this.update.bind(this));
};

Main.prototype.loadSpriteSheet = function() {
    var loader = PIXI.loader;

    //loader.add("wall", "resources/wall.json");    //example
    loader.add('shiba-neutral', '../img/shiba_neutral.jpg');
    loader.add('table', '../img/equipment/desk.png');
    loader.add('choppingBoard', '../img/equipment/chopping-board.png');
    loader.add('grill', '../img/equipment/grill.png');

    loader.add('burger-raw', '../img/food/burger-raw.png');
    loader.add('burger', '../img/food/burger.png');
    loader.add('burger-burned', '../img/food/burger-burned.png');

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
    this.gameObjects.forEach(function(gameObject) {
        self.stage.addChild(gameObject);
    });
};

Main.prototype.createEnvironment = function() {
    //lifeless objects

    //table
    var tableTexture = PIXI.Texture.fromImage('table');
    var table = new PIXI.Sprite(tableTexture);

    table.position.x = 200;
    table.position.y = 250;

    table.scale.set(0.9);

    this.stage.addChild(table);

    //chopping board
    var choppingBoard = new Grill(270, 330, 180, 100, PIXI.Texture.fromImage('choppingBoard'));
    //this.gameObjects.push(choppingBoard);

    //grill
    var grill = new Grill(640, 330, 180, 90, PIXI.Texture.fromImage('grill'));
    //this.gameObjects.push(grill);
    this.stage.addChild(grill);
};

Main.prototype.createShiba = function() {
    var shibaTexture = PIXI.Texture.fromImage("shiba-neutral");
    var shiba = new PIXI.Sprite(shibaTexture);

    shiba.position.x = 400;
    shiba.position.y = 100;

    shiba.scale.set(0.4);

    this.stage.addChild(shiba);

    //this.gameObjects.push(shiba);

};

Main.prototype.createFood = function() {
    var burger = new Hamburger(200, 200, 80, 80, PIXI.Texture.fromImage("burger-raw"));
    this.gameObjects.push(burger);
};