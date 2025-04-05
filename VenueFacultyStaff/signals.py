from permissions.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver,Signal
from . models import VenueFacultyStaff
from FacultyCoordinator.models import FacultyCoordinator
from VenueFacultyCoordinator.models import VenueFacultyCoordinator
from django.core.mail import send_mail

send_mail_vfs_signal=Signal()

@receiver(post_save,sender=Permission)
def check_if_update(sender,instance,**kwargs):

    if instance.fc_tag=='yes' and instance.vfc_tag=='yes' and instance.scy_tag=='yes' and     instance.venue_name.venue_type=='DP':
        send_mail_vfs_signal.send(sender=sender,instance=instance)


@receiver(send_mail_vfs_signal)
def send_mail_vfc(sender,instance,**kwargs):
    venue=instance.venue_name
    vfs=VenueFacultyStaff.objects.get(venue=venue)

    venue=instance.venue_name
    vfc=VenueFacultyCoordinator.objects.get(venue=venue)

    if instance.owner!=None:
        club=instance.owner  #notok
        club_name = club.club_name #notok
        club_stmnt=f'for an upcoming event organized by our club, {club_name},'
        fc=FacultyCoordinator.objects.get(club=club) #notok
        fc_name=f"{fc.firstname} {fc.lastname}"
        fc_stmnt=f'The event has already received approval from {fc_name}, the Faculty Coordinator,'

        pm_user = instance.owner.clubrep
        pm_name = f"{pm_user.firstname} {pm_user.lastname}"
        pm_phone = pm_user.phone
        role='Club representative'
    else:
        fc_stmnt=''
        club_stmnt=''
        club_name=''
        pm_user = instance.fac_owner
        pm_name = f"{pm_user.firstname} {pm_user.lastname}"
        pm_phone = pm_user.phone
        role='Faculty'


    vfc_name = f"{vfc.firstname} {vfc.lastname}"  
    event_name = instance.event_name
    event_description = instance.event_description
    venue_name = instance.venue_name.venue_name
    date_start = instance.date_start.strftime("%d %B %Y")
    date_end = instance.date_end.strftime("%d %B %Y")
    time_start = instance.time_start.strftime("%I:%M %p")  
    time_end = instance.time_end.strftime("%I:%M %p")

    send_mail(
        subject=f"Request for Venue Approval - {club_name} ({role})",
        message=f"""Dear Professor Security,  

        I hope you're doing well.  

        I am reaching out to formally convey using the venue {venue_name} for an upcoming event organized by our club, {club_name}. I am reaching out to formally convey that using the venue {venue_name}, {club_stmnt} {fc_stmnt} and Office Personnel and {vfc_name}, the Venue Faculty Coordinator.  

        Event Details: 
        - Event Name: {event_name}  
        - Description: {event_description}  
        - Organized By: {club_name} ({role})  

        Venue Details: 
        - Requested Venue: {venue_name}  
        - Date: {date_start} to {date_end}  
        - Time: {time_start} to {time_end}  

        We'll take care of the venue and keep it clean and safe.

        To see this request, please visit the Hallify website. You can find more details about the event.  

        [Click here to review and approve](https://lucky-nadean-aanandh-d140dffc.koyeb.app/)

        Please let us know if you require any further details. Looking forward to your support.  

        Best Regards,  
        {pm_name}  
        {role}, {club_name}  
        {pm_phone}   
        """,
        recipient_list=vfs.email,
        fail_silently=False,
    )



