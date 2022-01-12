

function renderButtons(colors){
    container = document.createElement('div')
    container.setAttribute('class', 'buttons-wrapper'); 
    colors.forEach(color => {
        let newButton = document.createElement('button');
        newButton.style.cssText = `background: ${color}`;
        newButton.value = color; 
        newButton.setAttribute('class', 'color-button');
        newButton.appendChild(document.createTextNode(color));
        newButton.onclick = function(){setBodyBackgroundColor(color)}
        container.appendChild(newButton);
    });
    document.getElementById('root').appendChild(container);
}

function createRandomColorButton(){
    return; 
}

Array.prototype.random = function () {
    return this[Math.floor((Math.random()*this.length))];
}

function setRandomBackgroundColor(colors){
    setBodyBackgroundColor(colors.random);
}

function setBodyBackgroundColor(color){
    element = document.body;
    setBackgroundColor(element, color);
}

function setBackgroundColor(element, color){
    element.style.backgroundColor = color;
}

function main(){
    colors = ['#fe7c00', '#ffd832', '#00b4ab', '#0269a4', '#022b56'];
    renderButtons(colors);
    setRandomBackgroundColor(colors);
}


main();