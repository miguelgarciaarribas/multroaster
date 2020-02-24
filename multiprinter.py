import datetime

class MultiPrinter:
    def __init__(self, multiplications):
        self.multiplications = multiplications

    def generate(self):
        today = datetime.datetime.now()
        date = today.strftime("%A %B %d %Y")



        
        result = """
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="mult.css">
</head>
<body>
"""
        result += '<p class="header"> Multiplications for %s </p>'% date
        result += '<div class="wrapper">'
        for mult in self.multiplications:
            result = result + "<div class=box> %s </div>\n" % str(mult)
        result += '</div></body>'
        return result
        
