from django.http import HttpResponse
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
# def index(request):
# return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': 'something'}
    return render(request, 'email/test.html', context)




class PasswordResetEmail(BaseEmailMessage):
    def get_context_data(self):
        context = super().get_context_data()
        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.PASSWORD_RESET_CONFIRM_URL.format(**context)


def detail(request, question_id):
    t = PasswordResetEmail(template_name='email/test.html')
    return render(request, 'email/test.html', context)
