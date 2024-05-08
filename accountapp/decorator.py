from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def wrapper(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs["pk"])

        if request.user == user:
            return func(request,*args, **kwargs)
        else:
            return HttpResponseForbidden("허용되지 않는 접근입니다.")

    return wrapper