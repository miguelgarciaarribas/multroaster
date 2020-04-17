function drawClock(canvas_id, diameter, length, width, hour, minute) {
    drawTimes(canvas_id, diameter, length, width);
    drawHandles(canvas_id, hour, minute, diameter, length, width);
}

function drawTimes(canvas_id, diameter, length, width) {
    const canvas = document.getElementById(canvas_id);
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = 'black';
    radius = diameter / 2
    smalltick = radius / 20
    largetick = radius / 10

    ctx.translate(length/2, width/2);

    ctx.font = radius*0.15 + "px arial";
    ctx.textBaseline="middle";
    ctx.textAlign="center";

    for (i = 0; i <= 360  ; i += 360 / 60) {
	isHour = (i % 15) === 0;
	degrees = i;
	ctx.rotate(degrees * Math.PI / 180);
	ctx.translate(radius, 0);

	if (isHour) {
	    ctx.fillRect(0, 0, largetick, 5);
	    if (i != 0) {
		ctx.translate(30, 5);
		ctx.rotate(-degrees * Math.PI / 180);
		var number = ((i / 30) + 3) % 12;
		if (number === 0)
		    number = 12
		ctx.fillText(number , 0, 0);
		ctx.rotate(degrees * Math.PI / 180);
		ctx.translate(-30, -5);
	    }
	} else {
	    ctx.fillRect(0, 0, smalltick, 5);
	}

	ctx.translate(-radius, 0);
	ctx.rotate(-degrees * Math.PI / 180);
    }

    ctx.setTransform(1, 0, 0, 1, 0, 0);
}

function drawHandles(canvas_id, hour, minute, diameter, length, width) {
    const canvas = document.getElementById(canvas_id);
    const ctx = canvas.getContext('2d');

    ctx.translate(length/2, width/2);
    ctx.fillStyle = 'black';

    ctx.beginPath();
    ctx.arc(0,0,((diameter/2)*0.1),0,2*Math.PI);
    ctx.fill();
    
    minuteLength = (diameter/2)*0.8;
    hourLength = (diameter/2)*0.6;

    var hourAngle = ((hour % 12) * 30) - 90;
    hourAngle = hourAngle + ((minute / 60) * 30);

    var minuteAngle = (minute * 6) - 90;

    ctx.rotate(hourAngle * Math.PI / 180);
    ctx.fillRect(0, 0, hourLength, 2);
    ctx.translate(hourLength, 3);
    ctx.rotate(35 * Math.PI / 180);
    ctx.fillRect(0, 0, -15, -3);
    ctx.rotate(-35 * 2 *  Math.PI / 180);
    ctx.fillRect(0, 0, -15, -3);
    ctx.rotate(35 *  Math.PI / 180);
    ctx.translate(-hourLength, -3);
    ctx.rotate(-hourAngle * Math.PI / 180);

    ctx.rotate(minuteAngle * Math.PI / 180);
    ctx.fillRect(0, 0, minuteLength, 2);
    ctx.translate(minuteLength, 2);
    ctx.rotate(35 * Math.PI / 180);
    ctx.fillRect(0, 0, -15, -3);
    ctx.rotate(-35 * 2 *  Math.PI / 180);
    ctx.fillRect(0, 0, -15, -3);
    ctx.rotate(35 *  Math.PI / 180);
    ctx.translate(-minuteLength, -2);
    ctx.rotate(-minuteAngle * Math.PI / 180);

    ctx.setTransform(1, 0, 0, 1, 0, 0);
}


