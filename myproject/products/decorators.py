from django.shortcuts import redirect

def vendor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'vendor':
            
            if not request.user.vendor_profile.is_approved:
                return redirect('vendor_not_approved')

            return view_func(request, *args, **kwargs)
        
        return redirect('login')
    return wrapper