from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('sign_up')
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def test_blockly_maze_embed(request):
    return render(request, 'lesson_1/test_blockly_maze_embed.html')


def test_blockly_custom(request):
    return render(request, 'lesson_1/test_blockly_custom.html')


def test_skulpt(request):
    return render(request, 'lesson_2/test_skulpt.html')


def syntax_compendium(request):
    return render(request, 'syntax_compendium/compendium.html')
