from django.contrib import admin
from django.urls import path
from onecult.views import *

urlpatterns = [
    path('', showdata, name="showdata"),
    path('add', adddata, name="adddata"),
    path('update', updatedata, name="updatedata"),
    path('delete', deldata, name="deldata"),
    path('image-to-pdf',convert_image_to_pdf, name="imagetopdf")
]

