from django.shortcuts import render
from .forms import LengkapiFormCompany
from django.shortcuts import redirect
from landingpage.models import Company
# Create your views here.
def company_home(request):
    user = request.user
    context = {
        'user': user.username
    }
    return render(request,'company_home.html', context)

def company_profile(request):
    # user = request.user
    try:
        data_company = Company.objects.get(user=request.user)
    except:
        data_company = False
    if not data_company: # jika query set kosong
        data_company = False
    print(data_company)
    context = {
        'data_company': data_company, 
    }
    return render(request, "company_profile.html", context)

def company_lengkapi_profile(request):
    if request.method == 'POST':
        form = LengkapiFormCompany(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect('company:company_profile')
    else:
        form = LengkapiFormCompany()
    return render(request, 'company_lengkapi_profile.html', {'form': form})