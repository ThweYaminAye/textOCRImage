
from django.shortcuts import render
from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  

data = {}
def imagetoText(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        image = Image.open(image)
        res = pytesseract.image_to_string(image)
        result = res.split('\n')
        for text in result:
            if re.findall('^Ma|^Maung|^Daw|^U',text):
                data['name'] = text[0:len(text)-11]
            if re.findall('^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)',text):
                data['date'] = text
            if (re.findall('Ks$',text)):
                data['amount'] = text[1:]
            if re.findall('^\d{10}',text):
                data['id'] = text
        return render(request, 'result.html',{'data':data})
    return render(request,'index.html')



# Create your views here.
