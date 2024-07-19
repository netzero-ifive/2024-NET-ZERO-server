from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from .models import QRCode
import qrcode
import random
import string
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@api_view(['POST'])
def generate_qr_code(request):
    qr_data = request.POST.get('data')
    if not qr_data:
        return JsonResponse({'error': 'No data provided'}, status=400)

    parameter = generate_random_string()
    try:
        qr_code = QRCode.objects.create(data=qr_data, parameter=parameter)
    except:
        return JsonResponse({'error': 'Error creating QR code'}, status=500)

    qr_url = f'http://www.ifive.com/id/1235?price={parameter}'
    
    # Generate QR code image
    img = qrcode.make(qr_url)
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    file_name = f'{parameter}.png'
    file_path = default_storage.save(file_name, ContentFile(buffer.read()))

    qr_code_image_url = request.build_absolute_uri(f'/media/{file_path}')
    
    return JsonResponse({'url': qr_url, 'qr_code_image_url': qr_code_image_url})

def product_detail(request, parameter):
    qr_code = get_object_or_404(QRCode, parameter=parameter)
    return render(request, 'qrapp/product_detail.html', {'qr_code': qr_code})

def qr_form(request):
    return render(request, 'qrapp/qr_form.html')