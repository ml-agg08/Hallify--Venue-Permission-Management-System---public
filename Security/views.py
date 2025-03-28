from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . forms import SecurityForm
from permissions.models import Permission
from django.core.paginator import Paginator
from clubreps.models import ClubReps
# Create your views here.

@login_required(login_url='account')
def security_profile(request):

    if request.POST:
        frm=SecurityForm(request.POST)
        if frm.is_valid():
            fc=frm.save(commit=False)
            fc.user=request.user
            fc.save()
            return redirect('SCYPermissionList')
    
    frm=SecurityForm()
    return render(request,"security_profile.html",{"frm":frm})

@login_required(login_url='account')
def SCYPermissionList(request):
    
    if 'page' and 'status' in request.GET:

        status=request.GET.get('status')

        if(status=='yes'):
            permission_set=Permission.objects.filter(fc_tag='yes',off_tag='yes',vfc_tag='yes',scy_tag='yes').order_by('-created_at')
        else:
            permission_set=Permission.objects.filter(fc_tag='yes',off_tag='yes',vfc_tag='yes',scy_tag='no').order_by('-created_at')

        permission_paginator=Paginator(permission_set,2)
        page_number=request.GET.get('page')
        permission_page_set=permission_paginator.get_page(page_number)

        return render(request,'SCYPermissionList.html',{'permission_set':permission_page_set})

    permission_set=Permission.objects.filter(fc_tag='yes',off_tag='yes',vfc_tag='yes',scy_tag='no').order_by('-created_at')
    permission_paginator=Paginator(permission_set,2)
    page_number=request.GET.get('page')
    permission_page_set=permission_paginator.get_page(page_number)

    return render(request,'SCYPermissionList.html',{'permission_set':permission_page_set})



@login_required(login_url='account')
def SCYPermissionDetails(request,pk):
    permission_details=Permission.objects.get(id=pk)
    #handling cr and faculty role!!
    if permission_details.owner!=None:
        pm_user=ClubReps.objects.get(club=permission_details.owner)
    else:
        pm_user=permission_details.fac_owner
    return render(request,"scypermission_details.html",{'permission_details':permission_details,'pm_user':pm_user})

@login_required(login_url='account')
def SCYTagEdit(request,pk):
    permission_details=Permission.objects.get(id=pk)
    permission_details.scy_tag='yes'
    permission_details.save()
    return redirect(f"/scypermissiondetails/{pk}")
