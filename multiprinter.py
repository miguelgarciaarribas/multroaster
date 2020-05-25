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
<link rel="preload" href="digital-7.ttf" as="font" type="font/ttf">
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
<title>Operations</title>
</head>
<body>
"""
        result += '<p class="header"> Operations for %s - %s </p>\n'% (config.studentName, date)
        result += '<div class="control"> <input type="button" value="Toggle Results" onClick=toggleResults() /> </div>\n'
        result += '<div class="wrapper">\n'

        order = 1
        for op in operations:
            result = result + op.display(order)
            order = order +1

        result += '</div></body>'
        print(result)
        return result

    def printIntro(self, category):
        result = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Operations</title>
        </head>
        <body>
          <h1> Welcome to hojitas for %s. </h1>
          <p>Please configure the operation roaster and click Generate to see a preview. </p>
        """
        return result % category.representation
