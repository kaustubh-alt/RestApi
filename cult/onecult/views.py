from rest_framework.decorators import api_view
from .serial import doserial, addserial
from .models import *
import uuid
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from .forms import ImageUploadForm
from PIL import Image
from io import BytesIO
from django.http import FileResponse


@api_view(['GET'])
def showdata(request):
    if 'uid' in request.GET:
        uid = request.GET['uid']
        uiddat = Todo.objects.filter(uid = uid)
        fildata = doserial(uiddat, many=True)
        return Response({'status': 200,'data': fildata.data, 'msg': f'''Data fetched for {uid}'''})
    else:
        raw = Todo.objects.all()
        serial = doserial(raw, many=True)
        return Response({'status': 200,'data': serial.data, 'msg': 'Data fetched'})


@api_view(['POST'])
def adddata(request):
    data = request.data
    serial = addserial(data = data)
    if serial.is_valid():
        serial.save()
        return Response({'status': 200,'data':data, 'msg': 'Data added'})
    else:
        return Response({'status': 400, 'msg': 'Data is not valid','data':data})
    
@api_view(['PUT'])
def updatedata(request):
    dat = request.data
    id = dat.get('uid')
    
    modata = Todo.objects.get(pk=id)

    serial = doserial(modata,data = dat)
    if serial.is_valid():
        serial.save()
        return Response({'status': 200,'data':dat, 'msg': f'''Data Updated Succesfully for {dat.get('uid')}'''})
    else:
        return Response({'status': 400, 'msg': 'failed to update data','data':dat})
    
@api_view(['DELETE'])
def deldata(request):
    uid = request.GET.get('uid')
    try:
        obj = Todo.objects.get(pk=uid)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    obj.delete()
    return Response({'status':status.HTTP_204_NO_CONTENT,'msg':f'''Data deleted succusfully for {uid}'''})

def convert_image_to_pdf(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = Image.open(form.cleaned_data['image'])
            buffer = BytesIO()
            img.save(buffer, "PDF")
            buffer.seek(0)
            return FileResponse(buffer, content_type='application/pdf', filename='converted.pdf')
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})








