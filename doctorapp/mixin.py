from django.shortcuts import redirect
from django.urls.base import reverse_lazy



class SuperUserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('home')


class ValidPermissionMixin( object ):
    permission_required = ""
    url_redirect = None

    def get_perm(self):
        if isinstance( self.permission_required, str):
            perms = ( self.permission_required )
        else:
            perms = self.permission_required
    
        return perms
    
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('docinicio')
        return self.url_redirect
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms( self.get_perm() ):
            return super().dispatch(request, *args, **kwargs )
        
        return redirect(self.get_url_redirect())