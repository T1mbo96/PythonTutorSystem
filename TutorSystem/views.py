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


def lesson_2_variables(request):
    return render(request, 'lesson_2/variables.html')


def lesson_2_variables_exercise(request):
    return render(request, 'lesson_2/variables_exercise.html')


def lesson_2_conditional_statements_if(request):
    return render(request, 'lesson_2/conditional_statements_if.html')


def lesson_2_turtle_graphics(request):
    return render(request, 'lesson_2/turtle_graphics.html')


def syntax_compendium(request):
    return render(request, 'syntax_compendium/compendium.html')
