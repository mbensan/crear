from django.shortcuts import redirect


def login_required(function):

    def wrapper(request, *args, **kwargs):
        if 'user' not in request.session:
            return redirect('/login')
        resp = function(request, *args, **kwargs)
        return resp
    
    return wrapper