from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from . forms import FCForm
from permissions.models import Permission
from . models import FacultyCoordinator
from clubreps.models import ClubReps
from django.core.paginator import Paginator

@login_required(login_url='account')
def facultycoordinator_profile(request):

    error=''

    if request.POST:
        frm=FCForm(request.POST)
        if frm.is_valid():
            fc=frm.save(commit=False)
            fc.user=request.user
            fc.save()
            return redirect('FCPermissionList')
        else:
            error=f'Sorry, this club alraedy has a regsitered Faculty Coordinator!'
    frm=FCForm()
    return render(request,"facultycoordinator_profile.html",{'frm':frm,'error':error})

@login_required(login_url='account')
def FCPermissionList(request):

    fc=request.user.facultycoordinator_profile.club

    if 'status' in request.GET and 'page' in request.GET:

        status=request.GET.get('status')

        if(status=='yes'):
            permission_set=Permission.objects.filter(owner=fc,fc_tag='yes').order_by('-created_at')
        else:
            permission_set=Permission.objects.filter(owner=fc,fc_tag='no').order_by('-created_at')

        permission_paginator=Paginator(permission_set,2)
        page_number=request.GET.get('page')
        permission_page_set=permission_paginator.get_page(page_number)

        return render(request,'FCPermissionList.html',{'permission_set':permission_page_set})

    permission_set=Permission.objects.filter(owner=fc,fc_tag='no').order_by('-created_at')
    permission_paginator=Paginator(permission_set,2)
    page_number=request.GET.get('page')
    permission_page_set=permission_paginator.get_page(page_number)

    return render(request,'FCPermissionList.html',{'permission_set':permission_page_set})

@login_required(login_url='account')
def FCPermissiondetails(request,pk):
    permission_details=Permission.objects.get(id=pk)
    clubrep=ClubReps.objects.get(club=permission_details.owner)
    return render(request,"fcpermission_details.html",{'permission_details':permission_details,'clubrep':clubrep})

@login_required(login_url='account')
def FCTagEdit(request,pk):
    permission_details=Permission.objects.get(id=pk)
    permission_details.fc_tag='yes'
    permission_details.save()
    return redirect(f"/fc_permission_details/{pk}")








"""
secuirty:aanandheyy08@gmail.com
off:inkerhubtkmce@gmail.com
"""