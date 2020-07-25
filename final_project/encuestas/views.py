from django.shortcuts import render

# Create your views here.

def encuestaCreateView(request):
    form = encuestaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = FotoForm()

    context = {
            'form': form
            }
    return render(request, 'encuestas/encuestaCreate.html', context)

