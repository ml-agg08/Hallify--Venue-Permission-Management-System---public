from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout as authlogout
from clubreps.models import ClubReps
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required
from . models import UserType
from FacultyCoordinator.models import FacultyCoordinator
from VenueFacultyCoordinator.models import VenueFacultyCoordinator
from VenueFacultyStaff.models import VenueFacultyStaff
from Security.models import Security
from  Office.models import Office
from Faculty.models import Faculty
# Create your views here.


def account(request):
    user=None
    error=""

    if request.POST and 'register' in request.POST.dict():
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.create_user(
                username=username,
                password=password
            )

            request.session['new_user_id']=user.id

            return redirect('usertype')
        except Exception as e:
            error="Username already exists, please enter a different one!"
            return render(request,"account.html",{'user':user,'error':error})
        
    
    if request.POST and 'login' in request.POST.dict():
        
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:

            login(request,user)
                
            if not (UserType.objects.filter(user=user).exists()):
                request.session['new_user_id']=user.id
                return redirect('usertype')
            
            return redirect("firstpage")

        else:
            error='Wrong password/username, please try again.'


    return render(request,"account.html",{'user':user,'error':error})


def logout(request):
    authlogout(request)
    return redirect('account')

def usertype(request):
    user_id=request.session.get('new_user_id')
    if not user_id:
        return redirect('account')

    user=User.objects.get(id=user_id)

    if request.POST:
        selected_user_type=request.POST.get('user_type')

        UserType.objects.create(user=user,user_type=selected_user_type)

        del request.session['new_user_id']

        if request.user:
            return redirect("firstpage")

        return redirect('account')
    
    return render(request,"usertype.html")


def firstpage(request):

    if not request.user.is_authenticated:
        return redirect("account")

    user=request.user
    user_type=user.user_type
    user_type=user_type.user_type


    if user_type=='CR':

        if not (ClubReps.objects.filter(user=user).exists()):
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            url=reverse('permission_list')
            return redirect(f'{url}?status=no&page=1')   #is this required  (for all roles!)
        
    if user_type=='FAC':

        if not (Faculty.objects.filter(user=user).exists()):
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            url=reverse('FACPermissionList')
            return redirect(f'{url}?status=no&page=1')
                
    if user_type=='FC':

        if not (FacultyCoordinator.objects.filter(user=user).exists()):
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            url=reverse('FCPermissionList')
            return redirect(f'{url}?status=no&page=1')
                
    if user_type=='OFF':
                
        if not (Office.objects.filter(user=user).exists()):
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            url=reverse('OFFPermissionList')
            return redirect(f'{url}?status=no&page=1')

    if user_type=='VFC':
                
        if not (VenueFacultyCoordinator.objects.filter(user=user).exists()):
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            url=reverse('VFCPermissionList')
            return redirect(f'{url}?status=no&page=1')

    if user_type=='VFS':
                
        if not (VenueFacultyStaff.objects.filter(user=user).exists()):
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            url=reverse('VFSPermissionList')
            return redirect(f'{url}?page=1')

    if user_type=='SCY':
                
        if not (Security.objects.filter(user=user).exists()):
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            url=reverse('SCYPermissionList')
            return redirect(f'{url}?status=no&page=1')

@login_required(login_url='account')
def show_profile(request):

    user=request.user
    user_type=user.user_type
    user_type=user_type.user_type


    if user_type=='CR':

        profile=ClubReps.objects.get(user=user)
        if not profile:
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            return render(request,"crprofile.html",{'profile':profile})
        
    if user_type=='FAC':

        profile=Faculty.objects.get(user=user)
        if not profile:
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            return render(request,"facprofile.html",{'profile':profile})
                
    if user_type=='FC':

        profile=FacultyCoordinator.objects.get(user=user)
        if not profile:
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            return render(request,"fcprofile.html",{'profile':profile})
        
    if user_type=='OFF':
                
        profile=Office.objects.get(user=user)
        if not profile:
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            return render(request,"offprofile.html",{'profile':profile})
                
    if user_type=='VFC':

        profile=VenueFacultyCoordinator.objects.get(user=user)
        if not profile:
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            url=reverse('VFCPermissionList')
            return render(request,"vfcprofile.html",{'profile':profile})

    if user_type=='VFS':
                
        profile=VenueFacultyStaff.objects.get(user=user)
        if not profile:
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            return render(request,"vfsprofile.html",{'profile':profile})

    if user_type=='SCY':
                
        profile=Security.objects.get(user=user)
        if not profile:
            return render(request,'pleaseprofile.html',{'user_type':user_type})
        else:
            return render(request,"scyprofile.html",{'profile':profile})
        
def about(request):
    return render(request,"about.html")
