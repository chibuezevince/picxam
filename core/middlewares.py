from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse
from django.middleware.csrf import get_token
from inertia import share

from core.helpers import get_setting


def guest_required(redirect_to="/dashboard"):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


def pending_required(view_func):
    @wraps(view_func)
    def decorator(request, *args, **kwargs):
        if request.session.get("account_login") is None:
            current_url = request.get_full_path()
            return redirect(f'{reverse("login")}?next={current_url}')

        return view_func(request, *args, **kwargs)

    return decorator


def inertia_share(get_response):
    def middleware(request):
        get_token(request)
        share(
            request,
            user=lambda: {
                "name": request.user.name if request.user.is_authenticated else None,
                "email": request.user.email if request.user.is_authenticated else None,
            },
            accepted_file_types=[key.replace('.', '') for key in get_setting("accepted_file_types").keys()],
        )

        return get_response(request)

    return middleware
