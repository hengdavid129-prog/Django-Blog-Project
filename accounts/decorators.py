from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def role_require(*allow_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.profile.role in allow_roles:
                return view_func(request, *args, **kwargs)
            messages.error(request, 'You do not have permission to view this page.')
            return redirect('blog:index')
        return _wrapped_view
    return decorator