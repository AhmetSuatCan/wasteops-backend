from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .forms import OrganizationForm

def create_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organization_list')  # Change this to wherever you want to go after creation
    else:
        form = OrganizationForm()

    return render(request, 'organizations/create_organization.html', {'form': form})

