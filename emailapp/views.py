from django.shortcuts import render, redirect  # Import render để sử dụng template
from django.http import JsonResponse  # Import HttpResponse để trả về phản hồi đơn giản
from .email import get_email_list, get_email_by_id, delete_email_by_id

# from django.http import HttpResponse  # Import HttpResponse để trả về phản hồi đơn giản

# Create your views here.
# Views là trung tâm bộ não xử lý logic của ứng dụng Django. Chúng nhận yêu cầu từ người dùng, xử lý dữ liệu và trả về phản hồi. Trong ví dụ này, chúng ta sẽ tạo một view đơn giản để hiển thị một thông điệp chào mừng.

# Trả về 3 loại phản hồi phổ biến:
# 1. HttpResponse: Trả về một phản hồi đơn giản với nội dung văn bản.
# 2. JsonResponse: Trả về dữ liệu dưới dạng JSON, thường được sử dụng cho các API.
# 3. TemplateResponse: Trả về một trang HTML được tạo từ một template.


# Ví dụ về một view đơn giản sử dụng HttpResponse:
# def home(request):
#     return HttpResponse("Hello Phong! Welcome to the Email App.")


# Ví dụ trả về template
def home(request):
    query = request.GET.get("q")
    emails = get_email_list()

    if query:
        emails = [email for email in emails if query.lower() in email.title.lower()]

    return render(
        request, "home.html", {"emailObj": emails}
    )  # Sử dụng render để trả về một template HTML


def detail_email(request, id):
    email = get_email_by_id(id)
    return render(request, "detail_email.html", {"email": email})


def search_email(request):
    query = request.GET.get("q")
    page = request.GET.get("page", 1)

    return JsonResponse({"query": query, "page": page})


def delete_email(request, id):
    if request.method == "POST":
        delete_email_by_id(id)
    return redirect("home")
