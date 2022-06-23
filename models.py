from django.db import models
from django.utils.translation import gettext_lazy as _

##################可以根据现有脚手架模型进行替换####################
class CreateTracker(models.Model):
    created_at = models.DateTimeField(_("Created Time"),auto_now_add=True,editable=False)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

class CreateUpdateTracker(CreateTracker):
    updated_at = models.DateTimeField(_("Updated Time"),auto_now=True,editable=False)

    def save(self,update_fields=None,*args,**kwargs):
        if update_fields:
            update_fields.append("updated_at")
        return super().save(update_fields=update_fields,*args,**kwargs)
        
    class Meta(CreateTracker.Meta):
        abstract = True