from django.shortcuts import redirect


def login_required(function):

    def wrapper(request, *args):
        if 'usuario' not in request.session:
            return redirect('/login')
        resp = function(request, *args)
        return resp
    
    return wrapper