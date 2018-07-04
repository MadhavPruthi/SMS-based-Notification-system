from django.shortcuts import render
from .forms import QueryForm

def Query(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = QueryForm()
    return render(request, 'Query/Query.html', {'form': form})

