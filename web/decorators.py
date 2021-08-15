from django.shortcuts import render,redirect

def admin_check(function):
    def wrap(request,*args,**kwargs):
        
        if  str(request.user) != "AnonymousUser":
            if request.user is not None:
                # print(request.user.get_user_type())
                if not request.user.get_user_type()["is_admin"]:
                    msg ="Please Log-In using admin account"
                    return redirect("/login")
                else:
                    return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap