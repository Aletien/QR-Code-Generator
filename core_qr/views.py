from django.shortcuts import render
from .forms import GenerateQrCodeForm
import qrcode
import os
from django.conf import settings

def generate_qr_code(request):
    if request.method == 'POST':
        form = GenerateQrCodeForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Generate QR code
            qr = qrcode.make(url)
            file_name = restaurant_name.replace(' ', '_').lower() + '.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)

            # Image url 
            qr_image_url = os.path.join(settings.MEDIA_URL, file_name)

            return render(request, 'core_qr/qrcode.html', {'restaurant_name': restaurant_name, 'qr_image_url': qr_image_url, 'file_name': file_name})
    else:
        form = GenerateQrCodeForm()
        context = {
            'form': form,
        }
        return render(request, 'core_qr/generate_qr_code.html', context)