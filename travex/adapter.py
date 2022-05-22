from allauth.account.utils import perform_login
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from place.models import CustomUser
import logging

logger = logging.getLogger('django')

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        logger.warning(user)
        if user.id:
            return
        try:
            customer = CustomUser.objects.get(email=user.email)  # if user exists, connect the account to the existing account and login
            sociallogin.state['process'] = 'connect'
            perform_login(request, customer, 'none')
        except CustomUser.DoesNotExist:
            pass