from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from django.views import View
from product.models import Product, Allergen, Qrcode, ALLERGEN_CHOICES
from django.contrib import messages
from django.views.generic import ListView
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile


class CreateProductView(View):
    def get(self, request):
        context = {"allergen_choices": ALLERGEN_CHOICES}
        return render(request, "create_product.html", context)

    def post(self, request):
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        size = request.POST.get("size")
        materials_ko = request.POST.get("materials_ko")
        source_of_manufacture = request.POST.get("source_of_manufacture")
        caution = request.POST.get("caution")
        allergens = request.POST.getlist("allergens")
        qrcode_data = request.POST.get("qrcode_data")
        qrcode_image = request.FILES.get("qrcode_image")

        product = Product.objects.create(
            name=name,
            price=price,
            description=description,
            size=size,
            materials_ko=materials_ko,
            source_of_manufacture=source_of_manufacture,
            caution=caution,
        )

        for allergen in allergens:
            Allergen.objects.create(product=product, name=allergen)

        if qrcode_data or qrcode_image:
            Qrcode.objects.create(product=product, data=qrcode_data, image=qrcode_image)

        messages.success(request, "제품이 성공적으로 생성되었습니다.")
        return redirect("product_list")  # 제품 목록 페이지로 리다이렉트


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"


def generate_qr_code(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        link = request.POST.get("link")

        if not link:
            messages.error(request, "링크를 입력해주세요.")
            return render(request, "generate_qr_code.html", {"product": product})

        # QR 코드 생성
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # 이미지를 저장하기 위한 준비
        buffer = BytesIO()
        img.save(buffer, format="PNG")

        # Qrcode 모델 인스턴스 생성 및 저장
        qrcode_instance = Qrcode(product=product, data=link)
        qrcode_instance.image.save(
            f"qr_code_{product.id}.png", ContentFile(buffer.getvalue()), save=False
        )
        qrcode_instance.save()

        messages.success(request, "QR 코드가 성공적으로 생성되었습니다.")
        # return redirect(
        #     "product_detail", product_id=product.id
        # )  # 제품 상세 페이지로 리다이렉트

    return render(request, "generate_qr_code.html", {"product": product})
