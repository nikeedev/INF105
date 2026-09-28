let time = document.getElementById("time");
let fancy = document.getElementById("fancy")

// let fonts = ["Monsieur La Doulaise", "Mea Culpa", "Ballet", "Mrs Saint Delafield", "Hurricane", "Miss Fajardose", "WindSong", "Herr Von Muellerhoff", "Ruthie", "Mr De Haviland"];

const update = () => {
	time.innerText = new Date().toLocaleTimeString("nb-NO");

	window.requestAnimationFrame(update);
}
window.requestAnimationFrame(update);

/*
setInterval(() => {
	fancy.style.fontFamily = fonts[Math.round(Math.random()*fonts.length)]
//	document.querySelector("html").style.backgroundColor = `rgb(${Math.round(Math.random()*255)}, ${Math.round(Math.random()*255)}, ${Math.round(Math.random()*255)})` 
//	document.querySelector("html").style.color = `rgb(${Math.round(Math.random()*255)}, ${Math.round(Math.random()*255)}, ${Math.round(Math.random()*255)})` 
}, 100)
*/

let term = document.getElementById("terminal");
let out = document.getElementById("out");


term.onkeydown = (event) => {
    if (event.key == "Enter") {
        term.
    }
}


