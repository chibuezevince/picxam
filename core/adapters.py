from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model

User = get_user_model()


class HeadlessAuditAdapter(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        if template_prefix == "account/email/account_already_exists":
            return
        return super().send_mail(template_prefix, email, context)
