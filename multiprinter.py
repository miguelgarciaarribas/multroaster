import datetime


class MultiPrinter:
    def print(self, config, operations):
        today = datetime.datetime.now()
        date = today.strftime("%A %B %d %Y")

#TODO Replace with a proper template

        result = """
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="mult.css">
<script src="multifigures.js"></script>
<script src="multigrid.js"></script>
<script>
function toggleResults() {
  var results = document.getElementsByClassName('result');
  for(i = 0; i < results.length; i++) {
    if (results[i].style.display === 'inline'){
     results[i].style.display = 'none';
    }  else {
     results[i].style.display = 'inline';
    }
  }
}


</script>
</head>
<body>
"""
        result += '<p class="header"> Operations for %s - %s </p>'% (config.studentName, date)
        result += '<div class="control"> <input type="button" value="Toggle Results" onClick=toggleResults() /> </div>'
        result += '<div class="wrapper">'

        order = 1
        for op in operations:
            result = result + op.display(order)
            order = order +1

        result += '</div></body>'
        print(result)
        return result
