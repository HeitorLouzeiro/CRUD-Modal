from django.contrib import messages
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import exampleModal


# Create your views here.
def home(request):
    template = 'modal/pages/home.html'
    personas = exampleModal.objects.all().order_by('name')
    context = {'personas': personas}
    return render(request, template, context)


def createModal(request):
    if not request.POST:
        raise Http404()
    if request.method == 'POST':
        name = request.POST.get('name')
        fistName = request.POST.get('fist_name')
        exampleModal.objects.create(name=name, fistName=fistName)
        messages.success(request, 'Data saved successfully!')
        return redirect('modal:home')
    else:
        messages.error(request, 'Data not saved!')
        return redirect(reverse('modal:home'))


def editModal(request):
    if not request.POST:
        raise Http404()
    id = request.POST.get('persona_id')
    personaedit = get_object_or_404(exampleModal, id=id)
    if request.method == 'POST':
        personaedit.name = request.POST.get('name')
        personaedit.fistName = request.POST.get('fist_name')
        personaedit.save()
        messages.success(request, 'Data saved successfully!')
        return redirect('modal:home')
    else:
        messages.error(request, 'Data not saved!')
        return redirect(reverse('modal:home'))


def deleteModal(request):
    if not request.POST:
        raise Http404()

    id = request.POST.get('persona_id')

    personadelete = get_object_or_404(exampleModal, id=id)

    personadelete.delete()
    messages.success(request, 'Data successfully deleted!')
    return redirect(reverse('modal:home'))
