from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm

#Read the Persons

def person_list(request):
    search_query = request.GET.get('q', '')
    if search_query:
        people = Person.objects.filter(username__icontains=search_query)
    else:
        people = Person.objects.all()
    return render(request, 'dashboard/person_list.html', {'people': people, 'search_query': search_query})

# Create the Persons

def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'dashboard/person_form.html', {'form': form, 'title': 'Create Person'})

# Update the Persons

def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'dashboard/person_form.html', {'form': form, 'title': 'Update Person'})

# Delete the Persons

def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('person_list')