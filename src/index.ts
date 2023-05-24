import { Application, Sprite , Container} from 'pixi.js'

const app = new Application({
	view: document.getElementById("pixi-canvas") as HTMLCanvasElement,
	resolution: window.devicePixelRatio || 1,
	autoDensity: true,
	background: 0x6495ed,
	width: 1400,
	height: 900
});

const container = new Container();

const fundo: Sprite = Sprite.from("fundo.jpg");

fundo.width = app.screen.width;
fundo.height = app.screen.height;
fundo.zIndex = 20;

const boy: Sprite = Sprite.from("boy1.png");
app.stage.addChild(fundo);

app.stage.addChild(container);

container.addChild(boy);
boy.anchor.set(0.5,0.5);
//app.stage.addChild(boy);
boy.angle = 90;
boy.scale.set(0.2 ,0.2); 
boy.x=0;
boy.y=0;
container.x = 140;
container.y = 800;


// Move container to the center
container.pivot.x=0;
container.pivot.y=75;
container.x = (app.screen.width / 2);
container.y = (app.screen.height / 2);

// container.zIndex = 10;

// Center bunny sprite in local container coordinates
//container.pivot.x = container.width / 2;
//co.pivot.y = container.height / 2;


// Listen for animate update
app.ticker.add((delta) => {
    // rotate the container!
    // use delta to create frame-independent transform
    container.rotation += 0.01 * delta;
	
	console.log (delta);
});