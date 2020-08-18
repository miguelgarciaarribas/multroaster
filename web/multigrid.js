const GUIDANCE = {
    LINE: 'line',
    DOTS: 'dots',
    MARKS: 'marks',
    UNDEFINED: 'undefined'
}

function drawHorizontalGrid(canvas_id, grid_size) {
    const canvas = document.getElementById(canvas_id);
    const ctx = canvas.getContext('2d');

    for (i = 0; i < canvas.width; i+=grid_size) {
        ctx.translate(i, 0);
        ctx.moveTo(0,0);
        ctx.lineTo(0, canvas.height);
        ctx.stroke();
        ctx.translate(-i, 0);
    }

    ctx.setTransform(1, 0, 0, 1, 0, 0);
}

function drawVerticalGrid(canvas_id, grid_size) {
    const canvas = document.getElementById(canvas_id);
    const ctx = canvas.getContext('2d');
    for (i = 0; i < canvas.height; i+=grid_size) {
        ctx.translate(0, i);
        ctx.moveTo(0,0);
        ctx.lineTo(canvas.width,0);
        ctx.stroke();
        ctx.translate(0, -i);
    }

    ctx.setTransform(1, 0, 0, 1, 0, 0);
}

function drawFigureGrid(canvas_id, pattern) {
    const canvas = document.getElementById(canvas_id);
    const ctx = canvas.getContext('2d');
    const gridSize = 30
    ctx.lineWidth = 2;

    ctx.beginPath();

    drawVerticalGrid(canvas_id, gridSize);
    drawHorizontalGrid(canvas_id, gridSize);

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
    const radius = 3.5;

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
    const radius = 3.5;
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


function drawCircle(canvas_id, radius) {
    const canvas = document.getElementById(canvas_id);
    const ctx = canvas.getContext('2d');
    ctx.lineWidth = 2;
    ctx.strokeStyle = "black";
    ctx.beginPath();
    ctx.arc(0, 0, radius, 0, 2 * Math.PI);
    ctx.fill();
}


function drawRow(canvas_id, row, height) {
    const gridSize = 18;
    const canvas = document.getElementById(canvas_id);
    const ctx = canvas.getContext('2d');
    ctx.lineWidth = 2;
    ctx.beginPath();

    var x = 0;
    var y = gridSize * height;


    ctx.moveTo(x, y);
    cells = row.split(',');
    for (var i = 0; i < cells.length; ++i) {
        x = gridSize * i;
        ctx.moveTo(x, y);

        if (cells[i] === ' ') {
            ctx.moveTo(x + gridSize, y);
        }

        else if (cells[i] === 'ensw') {  // '┼'
            ctx.moveTo(x + gridSize/2, y);
            ctx.lineTo(x + gridSize/2, y + gridSize);
            ctx.moveTo(x, y + gridSize / 2);
            ctx.lineTo(x + gridSize, y + gridSize/2);
        }
        else if (cells[i] === 'ens') {  // '├'
            ctx.moveTo(x + gridSize /2, y);
            ctx.lineTo(x + gridSize /2, y + gridSize);
            ctx.moveTo(x + gridSize /2, y + gridSize / 2);
            ctx.lineTo(x + gridSize, y + gridSize / 2);
        }
        else if (cells[i] === 'enw') {  //'┴'
            ctx.moveTo(x + gridSize /2, y);
            ctx.lineTo(x + gridSize/2, y + gridSize /2)
            ctx.moveTo(x, y + gridSize /2);
            ctx.lineTo(x + gridSize, y + gridSize /2);
        }
        else if (cells[i] === 'esw') {  //'┬'
            ctx.moveTo(x, y + gridSize /2);
            ctx.lineTo(x + gridSize, y + gridSize /2);
            ctx.moveTo(x + gridSize/2, y + gridSize /2);
            ctx.lineTo(x + gridSize/2, y + gridSize);
        }
        else if (cells[i] === 'es') { //'┌',
            ctx.moveTo(x + gridSize/2, y + gridSize /2);
            ctx.lineTo(x + gridSize, y + gridSize /2);
            ctx.moveTo(x + gridSize/2, y + gridSize /2);;
            ctx.lineTo(x + gridSize/2, y + gridSize);
        }
        else if (cells[i] === 'en') { //'└',
            ctx.moveTo(x + gridSize/2, y);
            ctx.lineTo(x + + gridSize/2, y + gridSize/2);
            ctx.lineTo(x + gridSize, y + gridSize/2);
        }
        else if (cells[i] === 'ew') {  // '─'
            ctx.moveTo(x, y + gridSize / 2);
            ctx.lineTo(x + gridSize, y + gridSize / 2);
        }
        else if (cells[i] === 'e') {  // '╶'
            // pass
        }
        else if (cells[i] === 'w') {  //  '╴'
            // pass
        }
        else if (cells[i] === 'nsw') {  // '┤'
            ctx.moveTo(x + gridSize/2, y);
            ctx.lineTo(x + gridSize/2, y + gridSize);
            ctx.moveTo(x + gridSize/2, y + gridSize/2);
            ctx.lineTo(x, y + gridSize/2);
        }
        else if (cells[i] === 'ns') { // '│'
            ctx.moveTo(x + gridSize / 2, y);
            ctx.lineTo(x + gridSize / 2, y + gridSize);
        }
        else if (cells[i] === 'sw') {  // '┐'
            ctx.moveTo(x, y + gridSize /2);
            ctx.lineTo(x + gridSize /2, y + gridSize /2);
            ctx.lineTo(x + gridSize /2, y + gridSize);
        }
        else if (cells[i] === 'nw') { // '┘',
            ctx.moveTo(x + gridSize /2 , y);
            ctx.lineTo(x + gridSize/2, y + gridSize /2);
            ctx.lineTo(x, y + gridSize /2);
        }
        else if (cells[i] === 's') {  // '╷'
            ctx.moveTo(x + gridSize /2, y + gridSize /2);
            ctx.lineTo(x + gridSize /2, y + gridSize);
        }
        else if (cells[i] === 'n') {  // '╵'
            ctx.moveTo(x + gridSize /2, y);
            ctx.lineTo(x + gridSize /2, y + gridSize/2);
        }
        else if (cells[i] === 'ns') {  // '╵'
            ctx.lineTo(x, y + gridSize);
            ctx.moveTo(x, y);
        }


        else {
            console.log('unsupported ' + cells[i]);
        }
    }
    ctx.stroke()
}

function drawMaze(canvas_id, laberinth) {
    const canvas = document.getElementById(canvas_id);
    const ctx = canvas.getContext('2d');
    rows  = laberinth.split(";");
    for (var i = 0; i < rows.length; ++i) {
        drawRow(canvas_id, rows[i], i);
    }
    ctx.setTransform(1, 0, 0, 1, 0, 0);
}
