function drawCircle(canvas_id, radius) {
    const canvas = document.getElementById(canvas_id);
    const ctx = canvas.getContext('2d');
    ctx.lineWidth = 2;
    ctx.strokeStyle = "black";
    ctx.beginPath();
    ctx.arc(0, 0, radius, 0, 2 * Math.PI);
    ctx.fill();
}

const GUIDANCE = {
    LINE: 'line',
    DOTS: 'dots',
    MARKS: 'marks',
    UNDEFINED: 'undefined'
}

function drawGrid(canvas_id, pattern) {
    const canvas = document.getElementById(canvas_id);
    const ctx = canvas.getContext('2d');
    const gridSize = 30
    ctx.lineWidth = 2;

    ctx.beginPath();

    // SOLID GRID
    for (i = 0; i < canvas.height; i+=gridSize) {
	ctx.translate(0, i);
	ctx.moveTo(0,0);
	ctx.lineTo(canvas.width,0);
	ctx.stroke();
	ctx.translate(0, -i);
    }

    for (i = 0; i < canvas.width; i+=gridSize) {
	ctx.translate(i, 0);
	ctx.moveTo(0,0);
	ctx.lineTo(0, canvas.height);
	ctx.stroke();
	ctx.translate(-i, 0);
    }
    ////

    if (pattern === 'square') {
	var segments = 4
	var guidance = [GUIDANCE.LINE, GUIDANCE.DOTS, GUIDANCE.DOTS, GUIDANCE.MARKS, GUIDANCE.MARKS,
			GUIDANCE.MARKS, GUIDANCE.MARKS, GUIDANCE.MARKS, GUIDANCE.DOTS];
	for (i = 0; i < guidance.length; ++i) {
	    ctx.translate(gridSize * i * segments, gridSize*3);
	    drawSquarePath(canvas_id, gridSize, guidance[i]);
	    ctx.translate(gridSize * i * segments, gridSize*7);
	    drawSquarePath(canvas_id, gridSize, guidance[i]);
	}
    } else if (pattern == 'triangle') {
	var segments = 2
	var guidance = [GUIDANCE.LINE, GUIDANCE.DOTS, GUIDANCE.DOTS, GUIDANCE.MARKS, GUIDANCE.MARKS,
			GUIDANCE.MARKS, GUIDANCE.MARKS, GUIDANCE.MARKS, GUIDANCE.MARKS,
			GUIDANCE.MARKS, GUIDANCE.MARKS, GUIDANCE.MARKS, GUIDANCE.MARKS,
			GUIDANCE.MARKS, GUIDANCE.MARKS, GUIDANCE.MARKS, GUIDANCE.DOTS];
	for (i = 0; i < guidance.length; ++i) {
	    ctx.translate(gridSize * i * segments, gridSize*3);
	    drawTriangularPath(canvas_id, gridSize, guidance[i]);
	    ctx.translate(gridSize * i * segments, gridSize*7);
	    drawTriangularPath(canvas_id, gridSize, guidance[i]);
	}
    } else {
	drawText(canvas_id, 0, 0, "Pattern Not supported")
    }


    ctx.setTransform(1, 0, 0, 1, 0, 0);
}


function drawSquarePath(canvas_id, gridSize, format) {
    const canvas = document.getElementById(canvas_id);
    const ctx = canvas.getContext('2d');
    const segments = [5, 8, 5];
    const radius = 5;

    ctx.translate
    ctx.beginPath();
    ctx.lineWidth = 7;
    if (format === GUIDANCE.DOTS)
	ctx.setLineDash(segments);
    else
	ctx.setLineDash([])

    ctx.moveTo(0,0);
    ctx.fillRect(0,0,1,1)
    if (format === GUIDANCE.MARKS) {
	drawCircle(canvas_id, radius);
    } else {
	ctx.lineTo(gridSize,0);
	ctx.stroke();
    }

    ctx.translate(gridSize, 0);
    ctx.moveTo(0, 0);
    ctx.fillRect(0,0,1,1)
    if (format === GUIDANCE.MARKS) {
	drawCircle(canvas_id, radius);
    } else {
    ctx.lineTo(0,-gridSize * 2);
    ctx.stroke();
   }

    ctx.translate(0, -gridSize*2);
    ctx.moveTo(0, 0);
    if (format === GUIDANCE.MARKS) {
	drawCircle(canvas_id, radius);
    }
   else {
       ctx.lineTo(gridSize*2, 0);
       ctx.stroke();
   }


    ctx.translate(gridSize*2, 0);
    ctx.moveTo(0, 0);
    if (format == GUIDANCE.MARKS) {
	drawCircle(canvas_id, radius);
    } else {
	ctx.lineTo(0, gridSize * 2);
	ctx.stroke();
    }

    ctx.translate(0, gridSize*2);
    ctx.moveTo(0, 0);
    if (format === GUIDANCE.MARKS) {
	drawCircle(canvas_id, radius);
    } else {
	ctx.lineTo(gridSize, 0);
	ctx.stroke();
    }

    ctx.setTransform(1, 0, 0, 1, 0, 0);
}

function drawTriangularPath(canvas_id, gridSize, format) {
    const canvas = document.getElementById(canvas_id);
    const ctx = canvas.getContext('2d');
    const segments = [5, 8, 5];
    const radius = 5;
    ctx.beginPath();

    ctx.lineWidth = 7;
    if (format === GUIDANCE.DOTS)
	ctx.setLineDash(segments);
    else
	ctx.setLineDash([])

    ctx.moveTo(0, 0);
    if (format === GUIDANCE.MARKS) {
	drawCircle(canvas_id, radius);
    } else {
	ctx.lineTo(gridSize, -gridSize*2);
	ctx.stroke();
    }
    ctx.translate(gridSize, -gridSize*2);
    ctx.moveTo(0, 0);
    if (format === GUIDANCE.MARKS) {
	drawCircle(canvas_id, radius);
    } else {
	ctx.lineTo(gridSize, gridSize*2);
	ctx.stroke();
    }
    ctx.translate(gridSize, gridSize*2);

    ctx.setTransform(1, 0, 0, 1, 0, 0);
}
