from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipement,Animal
from .forms import MoveForm

# Create your views here.

def animal_list(request):
    animals = Animal.objects.filter()
    return render(request, 'blog/animal_list.html', {'animals': animals})
 
def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    ancien_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
    etat = animal.etat
    message = ''
    form = MoveForm()
    if request.method == "POST":
        form = MoveForm(request.POST, instance=animal)
    else:
        form = MoveForm()
    form.save(commit=False)
    if form.is_valid():
        if animal.lieu.disponibilite == "libre" and animal.lieu.id_equip == "mangeoire" and etat == "affamé": #exception littiere pas besoin de changer sa disponibilité car toujours libre
            animal.etat = "repus"
            animal.save()
            form.save()
            nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
            nouveau_lieu.disponibilite = "occupé"
            nouveau_lieu.save()
            return redirect('animal_detail', id_animal=id_animal)
        elif animal.lieu.disponibilite == "libre" and animal.lieu.id_equip == "roue" and etat == "repus":
            ancien_lieu.disponibilite = "libre"
            ancien_lieu.save()
            animal.etat = "fatigué"
            animal.save()
            form.save()
            nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
            nouveau_lieu.disponibilite = "occupé"
            nouveau_lieu.save()
            return redirect('animal_detail', id_animal=id_animal)
        elif animal.lieu.disponibilite == "libre" and animal.lieu.id_equip == 'nid' and etat == 'fatigué':
            ancien_lieu.disponibilite = "libre"
            ancien_lieu.save()
            animal.etat = "endormi"
            animal.save()
            form.save()
            nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
            nouveau_lieu.disponibilite = "occupé"
            nouveau_lieu.save()
            return redirect('animal_detail', id_animal=id_animal)
        elif animal.lieu.id_equip == "litière" and etat == "endormi":   #ici exception pour la litière qui peut accueillir plusieurs animaux, et donc qu'on laisse toujours libre
            ancien_lieu.disponibilite = "libre"
            ancien_lieu.save()
            animal.etat = "affamé"
            animal.save()
            form.save()
            return redirect('animal_detail', id_animal=id_animal)
        else:
            message = 'Opération impossible, ' + animal.lieu.id_equip + " est déjà occupé, ou alors n'est pas le bon endroit où amener " + animal.id_animal + " lorsqu'il est " + etat
            form = MoveForm()
            return render(request,
                    'blog/animal_detail.html',
                    {'animal': animal, 'form': form, 'message': message})
    else:
        form = MoveForm()
        return render(request,
                  'blog/animal_detail.html',
                  {'animal': animal, 'form': form})