from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        summary = request.POST.get('about')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        previous_work = request.POST.get('pwork')
        skills = request.POST.get('skills')
        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work,skills=skills)
        profile.save()
    return render(request,'cvapp/index.html')

def generate(request,id):
    cv = Profile.objects.get(pk = id)
    template = loader.get_template('cvapp/cv.html')
    context={'cv':cv}
    html = template.render(context)
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "cv.pdf"
    return response
def list(request):
    profile=Profile.objects.all()
    context = {'profile':profile}
    return render(request,'cvapp/list.html',context)

