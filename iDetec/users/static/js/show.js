let detect_canvas = document.querySelector('#detect');
let ctx = detect_canvas.getContext('2d');
let img_src = document.querySelector('#getImage').value;
let xs = document.querySelectorAll('.x');
let ys = document.querySelectorAll('.y');
let points = [];
let detecting = false;
let image = new Image();
image.src = img_src;



function initCanvas() {
    ctx.clearRect(0, 0, detect_canvas.width, detect_canvas.height);
    detect_canvas.width = detect_canvas.scrollWidth;
    if (!imageVerifyDraw()) {
        setTimeout(initCanvas, 100);
        return;
    }
    ctx.lineWidth = 2;
    drawDetectionPoints();
}

function imageVerifyDraw() {
    if (image.complete && image.naturalWidth > 0) {
        let image_ratio = image.naturalWidth / image.naturalHeight;
        detect_canvas.height = detect_canvas.width / image_ratio;
        ctx.drawImage(image, 0, 0, detect_canvas.width, detect_canvas.height);
        return true;
    }
    return false;
}

initCanvas();

window.addEventListener('resize', initCanvas);

const resize_ob = new ResizeObserver(initCanvas);
resize_ob.observe(detect_canvas);



class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}
for(let i=0 ; i< xs.length ; i++){
    points.push(new Point(xs[i].value, ys[i].value));
}


function drawDetectionPoints() {
    ctx.strokeStyle = '#0f0';
    ctx.beginPath();
    points.forEach((point, index) => {
        if (index === 0) {
            ctx.moveTo(point.x * detect_canvas.width, point.y * detect_canvas.height);
        } else {
            ctx.lineTo(point.x * detect_canvas.width, point.y * detect_canvas.height);
        }
    });
    if(!detecting){
        ctx.closePath();
    }
    ctx.stroke();
}
console.log(points)