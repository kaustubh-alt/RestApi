from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
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

# Secure your views by enforcing authentication and permissions

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def showdata(request):
    if 'uid' in request.GET:
        uid = request.GET['uid']
        uiddat = Todo.objects.filter(uid=uid)
        if not uiddat.exists():
            return Response({'status': 404, 'msg': f'Data not found for {uid}'}, status=status.HTTP_404_NOT_FOUND)
        fildata = doserial(uiddat, many=True)
        return Response({'status': 200, 'data': fildata.data, 'msg': f'Data fetched for {uid}'})
    else:
        raw = Todo.objects.all()
        serial = doserial(raw, many=True)
        return Response({'status': 200, 'data': serial.data, 'msg': 'Data fetched'})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def adddata(request):
    data = request.data
    serial = addserial(data=data)
    if serial.is_valid():
        serial.save()
        return Response({'status': 200, 'data': data, 'msg': 'Data added'})
    else:
        return Response({'status': 400, 'msg': 'Data is not valid', 'errors': serial.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updatedata(request):
    dat = request.data
    id = dat.get('uid')

    try:
        modata = Todo.objects.get(pk=id)
    except Todo.DoesNotExist:
        return Response({'status': 404, 'msg': 'Data not found'}, status=status.HTTP_404_NOT_FOUND)

    serial = doserial(modata, data=dat)
    if serial.is_valid():
        serial.save()
        return Response({'status': 200, 'data': dat, 'msg': f'Data updated successfully for {dat.get("uid")}'})
    else:
        return Response({'status': 400, 'msg': 'Failed to update data', 'errors': serial.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deldata(request):
    uid = request.GET.get('uid')
    if not uid:
        return Response({'status': 400, 'msg': 'UID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        obj = Todo.objects.get(pk=uid)
    except Todo.DoesNotExist:
        return Response({'status': 404, 'msg': 'Data not found'}, status=status.HTTP_404_NOT_FOUND)

    obj.delete()
    return Response({'status': status.HTTP_204_NO_CONTENT, 'msg': f'Data deleted successfully for {uid}'})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
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
            return Response({'status': 400, 'msg': 'Invalid form data', 'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})
