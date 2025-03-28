from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from . forms import CRForm

@login_required(login_url='account')
def clubrep_profile(request):
    error=''
    if request.POST:
        frm=CRForm(request.POST)
        if frm.is_valid():
            cr=frm.save(commit=False)
            cr.user=request.user
            print("user is",request.user)
            cr.save()
            return redirect('permission_list')
        else:
            error=f'Sorry, this club alraedy has a regsitered Club Representative!'

    frm=CRForm()

    return render(request,"clubrep_profile.html",{'frm':frm,'error':error})
