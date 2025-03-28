from django.shortcuts import render,redirect
from . models import Permission
from django.core.paginator import Paginator
from . forms import PermissionForm
from . forms import ClashInfoForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import datetime
from Office.models import Office
from Security.models import Security



@login_required(login_url='account')
def list(request):
    
    if 'page' and 'status' in request.GET:

        status=request.GET.get('status')

        if(status=='yes'):
            permission_set=Permission.objects.filter(owner=request.user.clubrep_profile.club,fc_tag='yes',off_tag='yes',vfc_tag='yes',scy_tag='yes').order_by('-created_at')
        else:
            permission_set=Permission.objects.filter(owner=request.user.clubrep_profile.club,scy_tag='no').order_by('-created_at')

        permission_paginator=Paginator(permission_set,2)
        page_number=request.GET.get('page')
        permission_page_set=permission_paginator.get_page(page_number)

        return render(request,'permissions_list.html',{'permission_set':permission_page_set})

    permission_set = Permission.objects.filter(owner=request.user.clubrep_profile.club, scy_tag='no').order_by('-created_at')
    permission_paginator=Paginator(permission_set,2)
    page_number=request.GET.get('page')
    permission_page_set=permission_paginator.get_page(page_number)

    return render(request,'permissions_list.html',{'permission_set':permission_page_set})


@login_required(login_url='account')
def permission_details(request,pk):
    permission_details=Permission.objects.get(id=pk)
    print(permission_details)
    return render(request,"permission_details.html",{'permission_details':permission_details})

@login_required(login_url='account')
def create_permission(request):

    message=''
    permissions=None

    if request.POST and 'create' in request.POST.dict():

        print('im creating an event !!')

        frm=PermissionForm(request.POST)
        frm_clash=ClashInfoForm()
        if frm.is_valid():
            permission=frm.save(commit=False)
            permission.owner=request.user.clubrep_profile.club

            venue = frm.cleaned_data["venue_name"]
            club=permission.owner

            errors=[]
            f=0

            if not hasattr(club,"facultycoordinator") or club.facultycoordinator is None:
                error=f"Sorry, faculty coordinator for {club.club_name} hasn't registered on Hallify yet! Conatct the authorities."

                errors.append(error)

                f=1

            if not (Office.objects.all().exists()):
                error=f"Sorry, Office Personnel hasn't registered on Hallify yet! Conatct the authorities."

                errors.append(error)

                f=1

            if not hasattr(venue, "venuefacultycoordinator") or venue.venuefacultycoordinator is None:

                error = f"Sorry, venue faculty coordinator for {venue.venue_name} hasn't registered on Hallify yet! Contact the authorities."

                errors.append(error)

                f=1

            if not (Security.objects.all().exists()):
                error=f"Sorry, Security hasn't registered on Hallify yet! Conatct the authorities."

                errors.append(error)

                f=1

            if f==1:
                print(errors)
                return render(request, 'create_permission.html', {'frm': frm, 'frm_clash': frm_clash, 'permissions': permissions, 'message': message,'errors':errors})



            date_start=frm.cleaned_data['date_start']
            date_end=frm.cleaned_data['date_end']
            time_start=frm.cleaned_data['time_start']
            time_end=frm.cleaned_data['time_end']
            venue_name=frm.cleaned_data['venue_name']


            permissions = Permission.objects.filter(
                venue_name=venue_name
            ).filter(
                Q(date_start__lte=date_end, date_end__gte=date_start)&  
                (
                    Q(date_start__lt=date_end, date_end__gt=date_start)|  
                    Q(time_start__lt=time_end, time_end__gt=time_start)  
                )
            )
            
            if permissions.exists():
                message="Sorry, there's a clash with the following events!!"
                print('sorry, yoy got clashes with these events!!')
                return render(request,'create_permission.html',{'frm':frm,'frm_clash':frm_clash,'permissions':permissions,'message':message})

            permission.save()
            return redirect('permission_list')
        
    if request.POST and 'search' in request.POST.dict():

        frm=PermissionForm()

        frm_clash=ClashInfoForm(request.POST)

        if frm_clash.is_valid():
            venue_name=frm_clash.cleaned_data['venue_name']
            date_start=frm_clash.cleaned_data['date_start']
            date_end=frm_clash.cleaned_data['date_end']

            if(venue_name==None and date_start==None and date_end==None):
                permissions=Permission.objects.all()
            elif(date_start==None and date_end==None):
                permissions=Permission.objects.filter(venue_name=venue_name)
            elif(venue_name==None):
                permissions = Permission.objects.filter(
                    date_start__lte=date_end, 
                    date_end__gte=date_start
                )
            else:
                permissions = Permission.objects.filter(
                    venue_name=venue_name,
                    date_start__lte=date_end, 
                    date_end__gte=date_start
                )         

            return render(request,'create_permission.html',{'frm':frm,'frm_clash':frm_clash,'permissions':permissions})

    frm=PermissionForm()
    frm_clash=ClashInfoForm()
    return render(request,'create_permission.html',{'frm':frm,'frm_clash':frm_clash})
