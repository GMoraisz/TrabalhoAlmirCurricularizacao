from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Alunos.views import (
    AlunosListView,
    NewAlunoCreateView,
    AlunoDetailView,
    AlunoUpdateView,
    AlunoDeleteView,
    logout_view,  # Importando a função logout_view
)
from accounts.views import register_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # URL para a função de logout
    path('Alunos/', AlunosListView.as_view(), name='Alunos_list'),
    path('new_Aluno/', NewAlunoCreateView.as_view(), name='new_Aluno'),
    path('Aluno/<int:pk>/', AlunoDetailView.as_view(), name='Aluno_detail'),
    path('Aluno/<int:pk>/update/', AlunoUpdateView.as_view(), name='Aluno_update'),
    path('Aluno/<int:pk>/delete/', AlunoDeleteView.as_view(), name='Aluno_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
