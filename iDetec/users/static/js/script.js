let detect_canvas = document.querySelector('#detect');
let ctx = detect_canvas.getContext('2d');
let detection_control = document.querySelector('#detect_frames_control');
let img_src = document.querySelector('#getImage').value;
let points = [];
let detecting = false;
let image = new Image();
let submit = document.querySelector('#submit');
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

detect_canvas.addEventListener('click', (e) => {
    if (detecting) {
        let x = (e.layerX - detect_canvas.offsetLeft) / detect_canvas.width;
        let y = (e.layerY - detect_canvas.offsetTop) / detect_canvas.height;
        points.push(new Point(x, y));
        ctx.clearRect(0, 0, detect_canvas.width, detect_canvas.height);
        ctx.drawImage(image, 0, 0, detect_canvas.width, detect_canvas.height);
        ctx.fillStyle = '#0f0';
        points.forEach(point => {
            ctx.fillRect(point.x * detect_canvas.width - 2, point.y * detect_canvas.height - 2, 4, 4);
        });
        drawDetectionPoints();
    }
});

detection_control.querySelector('.add').addEventListener('click', (e) => {
    if (!detecting) {
        detecting = true;
        points = [];
        initCanvas();
        detection_control.querySelector('.add').innerHTML = 'Stop';
    } else {
        if (points.length < 3) {
            alert('Not enough points');
            return;
        }
        detecting = false;
        let pts_string = '';
        points.forEach((p,i) =>{
            pts_string += p.x + ';' + p.y;
            if(i != points.length - 1){
                pts_string += '-';
            }
        });
        document.querySelector('#pts_string').value = pts_string;
        drawDetectionPoints();
        detection_control.querySelector('.add').innerHTML = 'Restart';
    }
});



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

window.addEventListener('beforeunload', (e) => {
    if (points.length > 0) {
        e.returnValue = 'Are you sure you want to leave?';
    }
});





