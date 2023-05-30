import functools

from flask import session, request, redirect, url_for


def login_required(route_func):
    @functools.wraps(route_func)
    def decorated_route(*args, **kwargs):
        if not session.get('user') or request.cookies.get('AuthToken') != session.get('user'):
            return redirect(url_for('auth.views.login_page'))
        return route_func(*args, **kwargs)

    return decorated_route
