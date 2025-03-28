from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . forms import OfficeForm
from permissions.models import Permission
from django.core.paginator import Paginator
from clubreps.models import ClubReps
# Create your views here.


@login_required(login_url='account')
def office_profile(request):

    if request.POST:
        frm=OfficeForm(request.POST)
        if frm.is_valid():
            fc=frm.save(commit=False)
            fc.user=request.user
            fc.save()
            return redirect('OFFPermissionList')
    
    frm=OfficeForm()
    return render(request,"office_profile.html",{"frm":frm})


@login_required(login_url='account')
def OFFPermissionList(request):
    
    if 'page' and 'status' in request.GET:

        status=request.GET.get('status')

        if(status=='yes'):   #we can see if its fauclty and then dont check fc_tag at all
            permission_set=Permission.objects.filter(fc_tag='yes',off_tag='yes').order_by('-created_at')
        else:
            permission_set=Permission.objects.filter(fc_tag='yes',off_tag='no').order_by('-created_at')

        permission_paginator=Paginator(permission_set,2)
        page_number=request.GET.get('page')
        permission_page_set=permission_paginator.get_page(page_number)

        return render(request,'OFFPermissionList.html',{'permission_set':permission_page_set})

    permission_set=Permission.objects.filter(fc_tag='yes',off_tag='no').order_by('-created_at')
    permission_paginator=Paginator(permission_set,2)
    page_number=request.GET.get('page')
    permission_page_set=permission_paginator.get_page(page_number)

    return render(request,'OFFPermissionList.html',{'permission_set':permission_page_set})


@login_required(login_url='account')
def OFFPermissionDetails(request,pk):
    permission_details=Permission.objects.get(id=pk)
    #handling cr and faculty role!!
    if permission_details.owner!=None:
        pm_user=ClubReps.objects.get(club=permission_details.owner)
    else:
        pm_user=permission_details.fac_owner
    return render(request,"offpermission_details.html",{'permission_details':permission_details,'pm_user':pm_user})

@login_required(login_url='account')
def OFFTagEdit(request,pk):
    permission_details=Permission.objects.get(id=pk)
    permission_details.off_tag='yes'
    permission_details.save()
    return redirect(f"/offpermissiondetails/{pk}")


