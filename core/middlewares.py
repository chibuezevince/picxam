from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse
from inertia import share


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
        share(
            request,
        )

        return get_response(request)

    return middleware
