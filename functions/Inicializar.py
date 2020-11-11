import os

class Inicializar:

    basepath = os.path.abspath(os.path.join(__file__, "../.."))

    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    BROWSER = u'CHROME'

    Environment = 'Test'
    
    if Environment == 'Test':
        URL = 'https://www.demoblaze.com/index.html'