from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import auth

# Create your views here.
picturefiles = {'image': None, 'width': None, 'height': None}


class Index(View):
    def get(self, request):
        try:
            return render(request, 'main.html')
        except Exception as e:
            print(e)


class Picture(View):
    @csrf_exempt
    def post(self, request):
        try:

            image = request.FILES.get('image')

            width = request.POST.get('width')
            height = request.POST.get('height')
            widthinch = request.POST.get('widthinch')
            heightinch = request.POST.get('heightinch')
            style = request.POST.get('style')
            strength = request.POST.get('strength')
            size = request.POST.get('size')
            print(image, width, height, widthinch,
                  heightinch, style, strength, size)
            picturefiles['image'] = image
            # PictureSize.objects.create(name="scd",image=a)
            # return Js
            print(picturefiles)
            if request.user.is_authenticated:
                PictureSize.objects.create(image=image, width=width, height=height, heightininch=heightinch,
                                           widtininch=widthinch, style=style, strength=strength, size=size)
                return JsonResponse({'user': 'user'}, safe=False)
            else:
                return JsonResponse({'user': 'none'}, safe=False)
            return redirect('index')
        except Exception as e:
            print(e)


class Login(View):
    def get(self, request):
        try:
            print("FSddf")
            print(picturefiles)
            return render(request, 'login.html')
        except Exception as e:
            print(e)

    def post(self, request):
        try:
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            user = CustomUser.objects.get(mobile_no=phone,password=password)
            if user is not None:
                    auth.login(request, user)
                    return JsonResponse({'type':'success','success':'Login Successfully'})
            else:
                return JsonResponse({'type':'error','error':'Invalid Username And Password'})

            
        except Exception as e:
            print(e)


class Signup(View):
    def get(self, request):
        try:
            return render(request, 'signup.html')
        except Exception as e:
            print(e)

    def post(self, request):
        try:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            code = request.POST.get('code')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            password = request.POST.get('password')

            try:
                CustomUser.objects.get(mobile_no=phone)
                return JsonResponse({'type': 'warning', 'warning': "This User Already Registered! Please login"}, safe=False)
            except CustomUser.DoesNotExist:
                CustomUser.objects.create(mobile_no=phone, email=email, first_name=fname,
                                          last_name=lname, goo_uid=code, password=password, username=lname)
                user = CustomUser.objects.get(mobile_no=phone)
                if user is not None:
                    auth.login(request, user)
                    loguser = user.mobile_no
                    return JsonResponse({'type': 'success', 'success': "User Created Successfully", 'user': loguser}, safe=False)
        except Exception as e:
            print(e)


class Checkout(View):
    def get(self, request):
        try:
            return render(request, 'checkout.html')
        except Exception as e:
            print(e)
