from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from Alunos.models import Aluno, AlunoInventory


def Aluno_inventory_update():
    Alunos_count = Aluno.objects.all().count()
    Alunos_value = Aluno.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    AlunoInventory.objects.create(
        Alunos_count=Alunos_count,
        Alunos_value=Alunos_value
    )


@receiver(pre_save, sender=Aluno)
def Aluno_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Bio gerada automaticamente!'


@receiver(post_save, sender=Aluno)
def Aluno_post_save(sender, instance, **kwargs):
    Aluno_inventory_update()


@receiver(post_delete, sender=Aluno)
def Aluno_post_delete(sender, instance, **kwargs):
    Aluno_inventory_update()