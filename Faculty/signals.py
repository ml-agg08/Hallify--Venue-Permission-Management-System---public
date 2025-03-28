from permissions.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver,Signal
from django.core.mail import send_mail
from FacultyCoordinator.models import FacultyCoordinator
from VenueFacultyCoordinator.models import VenueFacultyCoordinator

send_mail_fac_signal=Signal()

@receiver(post_save,sender=Permission)
def check_if_update(sender,instance,**kwargs):

    if instance.fac_owner!=None:
        title=''
        name=''
        if instance.scy_tag=='yes':
            title="Security"
            name="Security"
        elif instance.vfc_tag=='yes':
            title="Venue Faculty Coordinator"
            venue=instance.venue_name
            vfc=VenueFacultyCoordinator.objects.get(venue=venue)
            name=vfc.firstname+" "+vfc.lastname
        elif instance.off_tag=='yes':
            title="Office Personnel"
            name="Office Personnel"    
        
        if(title!=''):
            send_mail_fac_signal.send(sender=sender,instance=instance,title=title,name=name)


@receiver(send_mail_fac_signal)
def send_mail_vfc(sender,instance,title,name,**kwargs):

    pm_user=instance.fac_owner


    first_name=pm_user.firstname
    last_name=pm_user.lastname
    venue_name=instance.venue_name.venue_name
    date_start = instance.date_start.strftime("%d %B %Y")
    date_end = instance.date_end.strftime("%d %B %Y")
    time_start = instance.time_start.strftime("%I:%M %p")  
    time_end = instance.time_end.strftime("%I:%M %p")
    event_name=instance.event_name
    event_description=instance.event_description

    off_tag_desc="Pending Approval"
    vfc_tag_desc="Pending Approval"
    scy_tag_desc="Pending Approval"

    if(instance.off_tag=='yes'):
        off_tag_desc="Approved"
    if(instance.vfc_tag=='yes'):
        vfc_tag_desc="Approved"        
    if(instance.scy_tag=='yes'):
        scy_tag_desc="Approved" 


    venue=instance.venue_name
    vfc=VenueFacultyCoordinator.objects.get(venue=venue)
    vfc_name=vfc.firstname+" "+vfc.lastname   

    final_status=''
    if instance.scy_tag=='yes':
        final_status="VENUE APPROVED !!- youv'e successfully attained all the permissions"

    send_mail(
        subject=title+'''-Permission Approved!''',
        from_email = os.getenv('EMAIL_HOST_USER')
        message='''Dear'''+first_name+last_name+''',
        We are pleased to inform you that '''+name+"("+title+")"+''' has approved your venue permission request for the following event details:

        📍 Venue Details:
        Venue:'''+venue_name+''''
        Date:'''+date_start+'''to'''+date_end+'''
        Time:'''+time_start+'''to'''+time_end+'''
        🎯 Event Details:
        Event Name: '''+event_name+'''
        Description: '''+event_description+'''
        ✅ Approval Status: 
         '''+final_status+''' 
        Office: '''+off_tag_desc+'''
        Venue Faculty Coordinator('''+vfc_name+'''): '''+vfc_tag_desc+'''
        Security: '''+scy_tag_desc+'''
        We kindly request you to check the Hallify website for further updates regarding the approval process.

        If you have any questions or require further assistance, please feel free to reach out.

        Thank you for using Hallify!''',
        recipient_list=[pm_user.email],
    )

