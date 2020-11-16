from django.contrib.auth.tokens import default_token_generator
from djoser import utils
from djoser.conf import settings
from django.conf import settings as dsettings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def urlParams(user):
    params = {}
    params['uid'] = utils.encode_uid(user.pk)
    params['token'] = default_token_generator.make_token(user)
    return params


class BaseEmail:
    subject = None
    template_name = None

    def __init__(self, request=None, context=None):
        self.request = request
        self.context = {} if context is None else context
        self.context['SITE_NAME'] = 'Shop'
        self.context['DOMAIN'] = dsettings.DOMAIN
        self.from_email = dsettings.DEFAULT_FROM_EMAIL
        self.context['BASE_URL'] = request.build_absolute_uri('/')

    def send(self, to, *args, **kwargs):
        html_message = render_to_string(self.template_name, self.context)
        send_mail(self.subject, self.subject, self.from_email, to, html_message=html_message)


class PasswordResetEmail(BaseEmail):
    def __init__(self, request=None, context=None):
        super().__init__(request, context)
        self.subject = '[%s] Reset your password' % self.context['SITE_NAME']
        self.template_name = 'users/password_reset.html'
        self.context['URL'] = settings.PASSWORD_RESET_CONFIRM_URL.format(**urlParams(self.context.get('user')))


class ActivationEmail(BaseEmail):
    def __init__(self, request=None, context=None):
        super().__init__(request, context)
        self.subject = '[%s] Active your account' % self.context['SITE_NAME']
        self.template_name = 'users/activation.html'
        self.context['URL'] = settings.ACTIVATION_URL.format(**urlParams(self.context.get('user')))


class PasswordChangedConfirmationEmail(BaseEmail):
    def __init__(self, request=None, context=None):
        super().__init__(request, context)
        self.subject = '[%s] Your password was reset' % self.context['SITE_NAME']
        self.template_name = 'users/password_changed_confirmation.html'
