import datetime


class MultiPrinter:
    def print(self, operations):
        today = datetime.datetime.now()
        date = today.strftime("%A %B %d %Y")

        
        result = """
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="mult.css">
<script src="multiclock.js"></script>
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
        result += '<p class="header"> Operations for Bruno - %s </p>'% date
        result += '<div class="control"> <input type="button" value="Toggle Results" onClick=toggleResults() /> </div>'
        result += '<div class="wrapper">'

        for op in operations:
            result = result + op.display()

        result += '</div></body>'
        return result
        
