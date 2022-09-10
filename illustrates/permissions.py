from math import perm
from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):  # 객체 전체, 즉 객체 리스트에 대한 권한
        if request.method == 'GET':
            return True
        return request.user.is_authenticated

    # GET, 즉 보는 건 누구나 할 수 있지만, 다른 기능은 작가만 가능
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.illustrator == request.user
