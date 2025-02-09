const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

let image = new Image();
image.src = imageSrc; 

let x = 100;
let y = 200;

image.onload = () => {
    console.log('Imagem carregada com sucesso');
    ctx.drawImage(image, x, y,150,150);
};

image.onerror = (e) => {
    console.error("Erro ao carregar a imagem:", e);
    alert("Não foi possível carregar a imagem!");
};

document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft') {
        x -= 10; 
    } else if (event.key === 'ArrowRight') {
        x += 10; 
    }else if (event.key == 'ArrowUp'){
        y -= 10;
    }else if (event.key == 'ArrowDown'){
        y += 10;
    }
    
    
    ctx.clearRect(0, 0, canvas.width, canvas.height);  
    
    if (image.complete) {
        ctx.drawImage(image, x, y,150,150);
    } else {
        console.log('A imagem ainda não foi carregada.');
    }
});
