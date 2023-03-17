from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from MainApp.forms import *
from django.contrib.auth import login, authenticate  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this



def index_page(request):
    context = {'pagename': 'PythonBin'}
    print(request.user.is_authenticated)
    return render(request, 'index.html', context)

def languages(request):
    context = {'pagename': 'PythonBin', "languages": Languages.objects.all()}
    print(request.user.is_authenticated)
    return render(request, 'languages.html', context)

def create_snippet(request):
    if not request.user.is_authenticated: return redirect("signin")
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user.id
            f.save()

        return redirect("list_snippets")


def snippets_page(request):
    snips = Snippet.objects.filter(public=True)
    context = {'pagename': 'Просмотр сниппетов', 'snips': snips, 'count': len(snips)}
    return render(request, 'view_snippets.html', context)


def view_snippet_page(request, id):
    item = Snippet.objects.get(pk=id)
    if item.public==False:
        if request.user.is_authenticated:

                if item.author == request.user.id:
                    return render(request, 'view_snippet.html', context={'pagename':item.name,'snippet': item})
                else:
                    return redirect('profile_snippets')

        else:
            return redirect("signin")
    else:
        return render(request, 'view_snippet.html', context={'pagename': item.name, 'snippet': item})

def view_snippet(request):
    if request.method == "POST":
        return redirect(f"/snippets/{request.POST['id']}")


def delete_snippet_page(request, id):

    snip = Snippet.objects.get(pk=id)

    if request.user.is_authenticated:
        if snip.author == request.user.id:
            snip.delete()
        else:
            return request("home")
    else:
        return redirect("signin")
    return redirect("/profile/snippets")
def raw_snippet_page(request, id):
    snip = Snippet.objects.get(pk=id)
    if snip.public==True:
        return render(request,"raw.html",context={"snippet": snip})
    else:
        if request.user.is_authenticated:
            if snip.author == request.user.id:
                return render(request,"raw.html",context={"snippet": snip})
            else:
                return redirect("/")
    return redirect("/profile/snippets")
def html_snippet_page(request, id):
    snip = Snippet.objects.get(pk=id)
    if snip.language != "HTML": return redirect("/")
    if snip.public==True:
        return render(request,"view_html_snippet.html",context={"snippet": snip})
    else:
        if request.user.is_authenticated:
            if snip.author == request.user.id:
                return render(request,"view_html_snippet.html",context={"snippet": snip})
            else:
                return redirect("/")
    return redirect("/profile/snippets")

def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
    messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})



def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "You have successfully logged out.")
    return redirect("home")

def profile_snippets_page(request,id):
    #if request.user.is_authenticated:
        snips = Snippet.objects.filter(author=id)
        context = {'pagename': 'Cниппеты', 'snips': snips, 'count': len(snips)}
        return render(request, 'profile_snippets.html', context)
    #else:
    #    return redirect("signin")
def profile_stats_page(request,id):
    print()
    snippets = Snippet.objects.filter(author=id)
    snippetLangCount = {}
    countsnipt = len(snippets)
    for snippet in snippets:
        if snippet.language in snippetLangCount:
            snippetLangCount[snippet.language]=snippetLangCount[snippet.language]+1
        else:
            snippetLangCount[snippet.language] = 1
    print(snippetLangCount)
    snippetProccent={}

    for language in snippetLangCount:
        snippetProccent[language]=(snippetLangCount[language]/countsnipt*100)

    resault = {}
    i=0
    for proc in snippetProccent:
        resault[f"{proc}: {round(snippetProccent[proc],2)}"]=len(snippetProccent)-i
        i+=1
    content = {"languages": resault,"pagename": "Статистика"}
    print(content)
    return render(request,"profile_stats.html", context=content)