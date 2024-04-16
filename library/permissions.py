from rest_framework.permissions import BasePermission
from .models import Request



class IsAuthenticatedOrReadOnlyForPost(BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        return request.user and request.user.is_authenticated
    
    
class CanDeleteRequest(BasePermission):
    
    def has_permission(self, request, view):
        if request.method == "DELETE":
            pk = view.kwargs["pk"]
            req = Request.objects.get(pk=pk)
            return request.user == req.user
