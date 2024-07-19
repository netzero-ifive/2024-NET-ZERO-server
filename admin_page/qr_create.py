from django.http import JsonResponse
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import uuid


def generate_random_string(length=8):
    return uuid.uuid4()


def generate_qr_code(data):
    parameter = generate_random_string()
    data = f"http://www.ifive.com/id/1235?price={data}"

    # Generate QR code image
    img = qrcode.make(data)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    file_name = f"{parameter}.png"
    file_path = default_storage.save(file_name, ContentFile(buffer.read()))

    qr_code_image_url = request.build_absolute_uri(f"/media/{file_path}")

    return JsonResponse({"url": qr_url, "qr_code_image_url": qr_code_image_url})
