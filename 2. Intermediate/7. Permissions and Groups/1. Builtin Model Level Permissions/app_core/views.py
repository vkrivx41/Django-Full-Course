from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import LoginView

from app_core.models import Document


class LoginView(LoginView):
    template_name = "core/login.html"


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(to="document:login")


@login_required
# @permission_required('app_core.view_document', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()

    context: dict = {
        'documents': documents
    }

    if request.user.has_perm('app_core.view_document'):
        context['additional'] = "Confidential data for permitted users"

    if request.user.has_perm('app_core.share_document'):
        context['share'] = True

    return render(request, 'core/index.html', context)


@login_required
@permission_required('app_core.view_document', raise_exception=True)
def document_detail(request, id: int):
    document = get_object_or_404(Document, id=id)

    context: dict = {
        'document': document
    }
    return render(request, 'core/detail.html', context)
