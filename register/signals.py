from django.dispatch import receiver
from django.db.models.signals import pre_save
from register.models import ticket
from threadlocals.threadlocals import get_current_request

        
@receiver(pre_save, sender=ticket)
def fill_user_field(sender, instance, *args, **kwargs):
    instance.user = get_current_request().user # Preenche o campo User automaticamente!