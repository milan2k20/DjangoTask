from django.shortcuts import *
from django.views import View
from behanceApp.models import Information


class InformationView(View):

    def get(self,request):
        return render(request,'information.html')

    def post(self,request):
        name = request.POST.get('name')
        url = request.POST.get('url')
        phone = request.POST.get('phone')

        user = Information(name = name, url = url, phone=phone)
        value = {'name':name, 'url':url}
        error_message = user.ValiadteUser()

        if not error_message:
            user.register()
            return redirect('search')
        else:
            data = {'error':error_message, 'values':value}
            return render(request,'information.html', context = data)



