from rest_framework.permissions import BasePermission


class CanViewDocument(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("app_core.view_document")

class CanShareDocument(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("app_core.share_document")
    
class CanArchiveDocument(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("app_core.archive_document")
    