from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView  # Import necessário
from Alunos.views import AlunosListView, NewAlunoCreateView, AlunoDetailView, AlunoUpdateView, AlunoDeleteView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('Alunos/', AlunosListView.as_view(), name='Alunos_list'),
    path('new_Aluno/', NewAlunoCreateView.as_view(), name='new_Aluno'),
    path('Aluno/<int:pk>/', AlunoDetailView.as_view(), name='Aluno_detail'),
    path('Aluno/<int:pk>/update/', AlunoUpdateView.as_view(), name='Aluno_update'),
    path('Aluno/<int:pk>/delete/', AlunoDeleteView.as_view(), name='Aluno_delete'),
    path('', TemplateView.as_view(template_name="alunos.html"), name='home'),  # Página inicial
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
