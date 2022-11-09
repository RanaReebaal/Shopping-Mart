
from django.http import HttpResponse
from django.shortcuts import render
import json
from . import views

def home(request):
    return render(request, 'home.html')


def contact(request):
    name = request.GET.get('us_name')
    age = request.GET.get('us_age')
    city = request.GET.get('us_city')
    job = request.GET.get('us_job')
    if name:
        if age:
            if city:
                if job:
                    class model():
                        def __init__(self, member, age, city, job):
                            self.member = member
                            self.age = age
                            self.city = city
                            self.job = job

                        def member_name(self):
                            return self.member

                        def member_age(self):
                            return self.age

                        def member_city(self):
                            return self.city

                        def member_job(self):
                            return self.job

                    user = model(name, age, city, job)

                    output = {
                        'user_name': user.member,
                        'user_age': user.age,
                        'user_city': user.city,
                        'user_job': user.job
                    }                    
                    with open('UserContactPageData.json', 'a') as d:
                        json.dump(output, d, indent=4)
                    return render(request, 'contact.html', output)
    return render(request, 'contact.html')


def index(request):
    name = request.GET.get('u_name')
    age = request.GET.get('u_age')
    image = request.GET.get('u_img')
    city = request.GET.get('u_city')
    job = request.GET.get('u_job')
    if name:
        if age:
            if image:
                if city:
                    if job:
                        class model():
                            def __init__(self, member, age, image, city, job):
                                self.member = member
                                self.age = age
                                self.image = image
                                self.city = city
                                self.job = job

                            def member_name(self):
                                return self.member

                            def member_age(self):
                                return self.age

                            def member_image(self):
                                return self.image
                            
                            def member_city(self):
                                return self.city

                            def member_job(self):
                                return self.job

                        user = model(name, age, image, city, job)

                        output = {
                            'user_name': user.member,
                            'user_age': user.age,
                            'user_image': user.image,
                            'user_city': user.city,
                            'user_job': user.job
                        }                    
                        with open('UserData.json', 'a') as d:
                            json.dump(output, d, indent=4)
                        return render(request, 'index.html', output)
    return render(request, 'index.html')
