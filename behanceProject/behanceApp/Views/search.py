from django.views import View
from django.shortcuts import *
from behanceApp.models import Information


class GetInformation(View):

    def get(self,request):
        return render(request,'search.html')

    def post(self,request):
        name = request.POST.get('name')
        user = Information.get_user_by_name(name)
        if user:
            print(user)
            return render(request, 'search.html',context={'user':user})











