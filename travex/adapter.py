from allauth.account.utils import perform_login
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from place.models import CustomUser
import logging
logger = logging.getLogger('django')


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if user.id:
            return
        try:
            custom_user = CustomUser.objects.get(email=user.email)  # if user exists, connect the account to the existing account and login
            google_picture = user.socialaccount_set.filter(provider='google')[0].extra_data['picture']
            logger.warning(google_picture)
            # if google_picture:
            #     if not user.image:
            #         user.image = google_picture
            #         user.save()
            sociallogin.state['process'] = 'connect'
            perform_login(request, custom_user, 'none')
        except CustomUser.DoesNotExist:
            pass