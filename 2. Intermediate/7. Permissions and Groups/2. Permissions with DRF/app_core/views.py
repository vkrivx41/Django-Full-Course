from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.views import LoginView

from rest_framework import generics, status, exceptions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app_core.models import Document, User
from app_core.serializers import DocumentSerializer, MeSerializer
from app_core.permissions import CanShareDocument, CanArchiveDocument, CanViewDocument


class LoginView(LoginView):
    template_name = "core/login.html"


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)

        return redirect(to="document:login")


class MeView(generics.GenericAPIView):
    serializer_class = MeSerializer

    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        print(self.request.user)
        user = User.objects.get(
            id=self.request.user.id
        )

        serializer = self.get_serializer(user)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class DocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    # permission_classes = [IsAuthenticated]


class DocumentDetailView(generics.RetrieveAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    permission_classes = [IsAuthenticated, CanViewDocument]
    lookup_url_kwarg = 'document_id'

    def get_object(self):
        current = super().get_object()
        
        if current.owner != self.request.user:
            raise exceptions.APIException(
                detail="You don't own this document",
                code=status.HTTP_404_NOT_FOUND
            )
        
        return current
        


# @login_required
# def document_list(request):
#     documents = Document.objects.all()

#     context: dict = {
#         'documents': documents
#     }

#     if request.user.has_perm('app_core.view_document'):
#         context['additional'] = "Confidential data for permitted users"

#     if request.user.has_perm('app_core.share_document'):
#         context['share'] = True

#     return render(request, 'core/index.html', context)


# @login_required
# @permission_required('app_core.view_document', raise_exception=True)
# def document_detail(request, id: int):
#     document = get_object_or_404(Document, id=id)

#     context: dict = {
#         'document': document
#     }

#     return render(request, 'core/detail.html', context)
