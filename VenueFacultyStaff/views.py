from django.shortcuts import render,redirect
from . forms import VFSForm
from django.contrib.auth.decorators import login_required
from permissions.models import Permission
from django.core.paginator import Paginator
from clubreps.models import ClubReps
# Create your views here.

@login_required(login_url='account')
def VenueFacultyStaffProfile(request):
    frm=VFSForm(request.POST)

    if request.POST:
        fs=frm.save(commit=False)
        fs.user=request.user
        fs.save()
        return redirect('VFSPermissionList')

    frm=VFSForm()
    return render(request,"venuefacultystaff.html",{"frm":frm})

@login_required(login_url='account')
def VFSPermissionList(request):

    fs=request.user.venuefacultystaff_profile.venue
    
    if 'page' in request.GET:

        permission_set=Permission.objects.filter(venue_name=fs,fc_tag='yes',off_tag='yes',vfc_tag='yes').order_by('-created_at')
        permission_paginator=Paginator(permission_set,2)
        page_number=request.GET.get('page')
        permission_page_set=permission_paginator.get_page(page_number)

        return render(request,'VFSPermissionList.html',{'permission_set':permission_page_set})

    permission_set=Permission.objects.filter(venue_name=fs,fc_tag='yes',off_tag='yes',vfc_tag='yes').order_by('-created_at')
    permission_paginator=Paginator(permission_set,2)
    page_number=request.GET.get('page')
    permission_page_set=permission_paginator.get_page(page_number)

    return render(request,'VFSPermissionList.html',{'permission_set':permission_page_set})


@login_required(login_url='account')
def VFSPermissiondetails(request,pk):
    permission_details=Permission.objects.get(id=pk)
    #handling cr and faculty role!!
    if permission_details.owner!=None:
        pm_user=ClubReps.objects.get(club=permission_details.owner)
    else:
        pm_user=permission_details.fac_owner
    return render(request,"vfspermission_details.html",{'permission_details':permission_details,'pm_user':pm_user})

