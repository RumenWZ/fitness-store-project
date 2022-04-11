from django.http import HttpResponse
from django.shortcuts import redirect


# def unauthenticated_user(value):
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('index')
#         else:
#             return value(request, *args, **kwargs)
#     return wrapper