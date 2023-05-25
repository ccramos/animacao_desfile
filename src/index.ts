import { Application, Sprite , Container} from 'pixi.js'

const app = new Application({
	view: document.getElementById("pixi-canvas") as HTMLCanvasElement,
	resolution: window.devicePixelRatio || 1,
	autoDensity: true,
	background: 0x6495ed,
	width: 1415,
	height: 950
});



const fundo: Sprite = Sprite.from("fundo.jpg");

const waypoints = [
	{ x:1400-20,	y:900 , a:360-0 },
	{ x:1400-270,	y:650 , a:360-45 },
	{ x:1400-270,	y:210 , a:360-0 },
	{ x:1400-1125,	y:210 , a:360-90 },
	{ x:1400-1125,	y:480 , a:360-180 },
	{ x:1400-705,	y:480 , a:360-270 },
	{ x:1400-705,	y:480 , a:360-270 },

];

const waypoints2 = [
	{ x:20,		y:900 , a: 0 },
	{ x:270,	y:650 , a: 45 },
	{ x:270,	y:200 , a: 0 },
	{ x:1125,	y:200 , a: 90 },
	{ x:1125,	y:490 , a: 180 },
	{ x:731,	y:490 , a: 270 },
	{ x:731,	y:490 , a: 270 },
];



const alunos: { nome: string; l: number; c: number; sprite: any}[] = []
const alunas: { nome: string; l: number; c: number; sprite: any}[] = []

for (let l=1; l<19; l++) {
	for (let c=6; c>0; c--) {
		alunos.push( {nome: `aluno ${l},${c}`, l:l , c:c, sprite: null})
		alunas.push( {nome: `aluna ${l},${c}`, l:l , c:c, sprite: null})
	}		
} 

	
// fun estádio
fundo.width = app.screen.width;
fundo.height = app.screen.height;
fundo.zIndex = 20;

app.stage.addChild(fundo);

const pelotao1 = criaPelotao(alunos, "boy1.png");
app.stage.addChild(pelotao1);

const pelotao2 = criaPelotao(alunas, "girl.png");
app.stage.addChild(pelotao2);

pelotao1.x = waypoints[0].x;
pelotao1.y = waypoints[0].y;
pelotao1.pivot.set(-60, 22*12/2);

pelotao2.x = waypoints2[0].x;
pelotao2.y = waypoints2[0].y;
pelotao2.pivot.set(-60, 22*12/2);

// const boy: Sprite = Sprite.from("boy1.png");
// app.stage.addChild(boy);
// boy.anchor.set(0.5,0.5);
// //app.stage.addChild(boy);
// boy.angle = 90;
// boy.scale.set(0.2 ,0.2); 
// boy.x = waypoints[0].x;
// boy.y = waypoints[0].y;

// const container = new Container();
// container.x = 140;
// container.y = 800;

let ponto = 1;
let ponto1 = 1;
//let linha = 1;

// Listen for animate update
app.ticker.add(() => {
	if ( ponto > 0 && moveToPoint( pelotao1, ponto, waypoints) ) {
		ponto++;
		if( ponto >= waypoints.length) {
			ponto = 0;
		}
		console.log (ponto, waypoints[ponto].x, waypoints[ponto].y, waypoints[ponto].a )
	}

	if ( ponto1 > 0 && moveToPoint( pelotao2, ponto1, waypoints2) ) {
		ponto1++;
		if( ponto1 >= waypoints2.length) {
			ponto1 = 0;
		}
		console.log (ponto1, waypoints2[ponto1].x, waypoints2[ponto1].y, waypoints2[ponto1].a )
	}

	if (ponto1 == 0 && ponto == 0) {
		viratodos(alunos, 90)
		viratodos(alunas, 270)
		ponto1 = -1
	}
///////////////////////////////////////////////////////////////
	if (ponto1 == -1){
		if ( andaColuna (-340, 230 )) {		
			ponto1--;
		}
		// fazcontorno()
	}



});

function moveToPoint ( obj : any, toPonto : any , waypoints : any)  {

	obj.angle = waypoints[toPonto].a;

	if (obj.x < waypoints[toPonto].x )
		obj.x++;;
	if (obj.x > waypoints[toPonto].x )
		obj.x--;

	if (obj.y < waypoints[toPonto].y )
		obj.y++;
	if (obj.y > waypoints[toPonto].y )
		obj.y--;
	
	if (obj.x == waypoints[toPonto].x && obj.y == waypoints[toPonto].y)
		return true
	
	return false
}

function criaPelotao ( alunos : any, imageName: any) : Container {
	const contPelotao = new Container();
	const distancia = 12;
	const cobertura = 20;
	
	for (let ix = 0; ix < alunos.length; ix++){
		const aluno: Sprite = Sprite.from(imageName);
		alunos[ix].sprite = aluno;
		alunos[ix].sprite.x = 0 - ((6 - alunos[ix].c) * cobertura) ;
		alunos[ix].sprite.y = 0 + alunos[ix].l * distancia;
		alunos[ix].sprite.anchor.set(0.5,0.5);
		alunos[ix].sprite.scale.set(0.11 ,0.11); 
		contPelotao.addChild(alunos[ix].sprite);
	}
	return contPelotao;
}


function viratodos ( elementos : any , direcao : any ) {

	for (let ix = 0; ix < elementos.length; ix++){
		elementos[ix].sprite.angle = direcao;
	}

}
let idColuna =1;
function andaColuna ( limite1 : number, limite2 : number) {
	
	const maxlin = alunas[alunas.length-1].l +1;

	for (let ix = 0; ix < alunas.length; ix++){
		if (alunas[ix].l >= (maxlin -idColuna) || alunas[ix].l <= idColuna ) {
			if ( alunas[ix].l >= (maxlin -idColuna) && alunas[ix].sprite.y > 613 ) {
				alunas[ix].sprite.angle = 0;
				alunas[ix].sprite.x++;
				//console.log("-->",alunas[ix].sprite.y)
			}
			else if ( alunas[ix].l <= idColuna && alunas[ix].sprite.y < -392) {
				alunas[ix].sprite.angle = 0;
				alunas[ix].sprite.x++;

			} else 	if ( alunas[ix].l >= (maxlin -idColuna) && alunas[ix].sprite.x < limite1 ) {
				alunas[ix].sprite.angle = 180;
				alunas[ix].sprite.y++;
				//console.log("-->",alunas[ix].sprite.y)
			}
			else if ( alunas[ix].l <= idColuna && alunas[ix].sprite.x < limite1) {
				alunas[ix].sprite.angle = 0;
				alunas[ix].sprite.y--;
				if (ix == 48) {
					return true
				}
				console.log("-->",ix)
			} 
			else
			{
				alunas[ix].sprite.x--;
				//console.log (alunas[ix].c ,alunas[ix].sprite.x )
				if (alunas[ix].c ==1 && alunas[ix].l == idColuna  && alunas[ix].sprite.x == limite1 +130 ) {
					if (idColuna < (maxlin/2)-1) {
						idColuna ++;
					} 

					console.log ("----", idColuna)
				}
			}
		}
		if (alunos[ix].l >= (maxlin -idColuna) || alunos[ix].l <= idColuna ) {
			if ( alunos[ix].l >= (maxlin -idColuna) && alunos[ix].sprite.y > 620 ) {
				alunos[ix].sprite.angle = 0;
				alunos[ix].sprite.x--;
				//console.log("-->",alunas[ix].sprite.y)
			}
			else if ( alunos[ix].l <= idColuna && alunos[ix].sprite.y < -385) {
				alunos[ix].sprite.angle = 0;
				alunos[ix].sprite.x--;

			}
			else if ( alunos[ix].l >= (maxlin -idColuna) && alunos[ix].sprite.x > limite2 ) {
				alunos[ix].sprite.angle = 180;
				alunos[ix].sprite.y++;
			}
			else if ( alunos[ix].l <= idColuna && alunos[ix].sprite.x > limite2 ) {
				alunos[ix].sprite.angle = 0;
				alunos[ix].sprite.y--;
			} 
			else
			{
				alunos[ix].sprite.x++;
				//console.log(alunos[ix].sprite.x)
			}
		}

	}

	return false	
}

// function fazcontorno() {
// 	//const maxlin = alunas[alunas.length-1].l +1;
// 	for (let ix = 0; ix < alunas.length; ix++){
// 		if (alunas[ix].sprite.x < -300){
// 		//console.log( '------>', alunas[ix].sprite.x , alunas[ix].sprite.x )
// 		}
// 	}
// }

