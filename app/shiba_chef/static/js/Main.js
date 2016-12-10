/**
 * Created by jorik on 10-12-2016.
 */
function Main() {
    this.stage = new PIXI.Container();
    this.renderer = PIXI.autoDetectRenderer(
        1200,
        720
    );

    this.renderer.backgroundColor = 0xB7E3E6;
    document.body.appendChild(renderer.view);

    this.loadSpriteSheet();
}

Main.stage =  new PIXI.Container();
Main.gameObjects = [];

Main.prototype.update = function() {
    //update game objects

    this.renderer.render(this.stage);
    requestAnimationFrame(this.update.bind(this));
};

Main.prototype.loadSpriteSheet = function() {
    var loader = PIXI.loader;
    //loader.add("wall", "resources/wall.json");    //example
    loader.once("complete", this.spriteSheetLoaded.bind(this));
    loader.load();
};

Main.prototype.spriteSheetLoaded = function() {
    makeWorld();
    requestAnimationFrame(this.update.bind(this));
};

Main.prototype.makeWorld = function() {

}