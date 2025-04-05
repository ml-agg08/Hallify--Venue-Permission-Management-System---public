from permissions.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver,Signal
from . models import FacultyCoordinator
from django.core.mail import send_mail

send_mail_fc_signal=Signal()

@receiver(post_save,sender=Permission)
def check_if_update(sender,instance,**kwargs):
    if instance.fc_tag=='no':
        send_mail_fc_signal.send(sender=sender,instance=instance)


@receiver(send_mail_fc_signal)
def send_mail_vfc(sender,instance,**kwargs):
    club=instance.owner
    fc=FacultyCoordinator.objects.get(club=club)


    club_name=club.club_name
    fc_name=f"{fc.firstname} {fc.lastname}"
    event_name=instance.event_name
    event_description=instance.event_description
    venue_name=instance.venue_name.venue_name
    date_start = instance.date_start.strftime("%d %B %Y")
    date_end = instance.date_end.strftime("%d %B %Y")
    time_start = instance.time_start.strftime("%I:%M %p")  
    time_end = instance.time_end.strftime("%I:%M %p")
    cr=instance.owner.clubrep

    cr_name=f"{cr.firstname} {cr.lastname}"
    cr_phone=cr.phone

    send_mail(
        subject=f"Request for Venue Permission Approval- {club_name}",
        message= f"""Dear Professor {fc_name}, 

        I hope you are doing well.  

        I am reaching out to formally request your approval for the venue permission for an upcoming event organized by our club,  {club_name}. Below are the details:  

        Event Details: 

        - Event Name: {event_name}  
        - Description: {event_description}  
        - Organized By: {club_name}  

        Venue Details:

        - Requested Venue: {venue_name}  
        - Date: {date_start} to {date_end} 
        - Time: {time_start} to {time_end}  

        We believe it will be a valuable addition to our campus activities.  

        To review and approve the request, please visit the Hallify website. You can find more details about the event and complete the approval process there.  

        [Click here to review and approve](https://lucky-nadean-aanandh-d140dffc.koyeb.app/)

        Please let us know if you require any further details. Looking forward to your support.  

        Best Regards,  
        {cr_name}  
        Club Representative, {club_name}  
        {cr_phone}
        """,
        recipient_list=[fc.email],
        fail_silently=False,
    )



