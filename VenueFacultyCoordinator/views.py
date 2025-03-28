from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from . forms import VFCForm
from permissions.models import Permission
from . models import VenueFacultyCoordinator
from clubreps.models import ClubReps
from django.core.paginator import Paginator

@login_required(login_url='account')
def venuefacultycoordinator_profile(request):

    error=''

    if request.POST:
        frm=VFCForm(request.POST)
        if frm.is_valid():
            fc=frm.save(commit=False)
            fc.user=request.user
            fc.save()
            return redirect('VFCPermissionList')
        
        else:
            error=f'Sorry, this venue alraedy has a regsitered Venue Faculty Coordinator!'
    
    frm=VFCForm()
    return render(request,"venuefacultycoordinator_profile.html",{'frm':frm,'error':error})



@login_required(login_url='account')
def VFCPermissionList(request):

    fc=request.user.venuefacultycoordinator_profile.venue
    
    if 'page' and 'status' in request.GET:

        status=request.GET.get('status')

        if(status=='yes'):                                         #fc_tag can be null, handle for fac
            permission_set=Permission.objects.filter(venue_name=fc,fc_tag='yes',off_tag='yes',vfc_tag='yes').order_by('-created_at')
        else:
            permission_set=Permission.objects.filter(venue_name=fc,fc_tag='yes',off_tag='yes',vfc_tag='no').order_by('-created_at')

        permission_paginator=Paginator(permission_set,2)
        page_number=request.GET.get('page')
        permission_page_set=permission_paginator.get_page(page_number)

        return render(request,'VFCPermissionList.html',{'permission_set':permission_page_set})

    permission_set=Permission.objects.filter(venue_name=fc,fc_tag='yes',off_tag='yes',vfc_tag='no').order_by('-created_at')
    permission_paginator=Paginator(permission_set,2)
    page_number=request.GET.get('page')
    permission_page_set=permission_paginator.get_page(page_number)

    return render(request,'VFCPermissionList.html',{'permission_set':permission_page_set})

@login_required(login_url='account')
def VFCPermissiondetails(request,pk):
    permission_details=Permission.objects.get(id=pk)
    #handling cr and faculty role!!
    if permission_details.owner!=None:
        pm_user=ClubReps.objects.get(club=permission_details.owner)
    else:
        pm_user=permission_details.fac_owner
    return render(request,"vfcpermission_details.html",{'permission_details':permission_details,'pm_user':pm_user})

@login_required(login_url='account')
def VFCTagEdit(request,pk):
    permission_details=Permission.objects.get(id=pk)
    permission_details.vfc_tag='yes'
    permission_details.save()
    return redirect(f"/vfc_permission_details/{pk}")