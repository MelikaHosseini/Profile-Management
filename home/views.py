from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from .models import *
from .forms import *
from .filters import * 


def index(request):
    return render(request, 'home/home.html')

def SignUpView(request, *args, **kwargs):
    if request.user.is_authenticated:
            messages.warning(request, 'you are already logged in' )
            return redirect('home:index')
    form = UserSignUpForm(request.POST or None)
    print(form)
    if form.is_valid():
        form.save()
        # full_name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(email = email, password = password)
        print(user)
        login(request, user)

        messages.success(request, f'Hey {email}' )


        return redirect("home:index")

    context = {
        "form" : form
    }
    return render(request, "home/sign-up.html", context)

def SignInView(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in' )
        return redirect('home:index')
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user_query = User.objects.get(email = email)
            user_auth = authenticate(request, email = email, password = password)

            if user_query is not None:
                 login(request, user_auth)
                 messages.success(request, "You are logged in")
                 reverse_url = request.GET.get("", "home:index")
                 return redirect(reverse_url)
            else:
                messages.error(request, "Username or password does not exist")
                return redirect('home:sign-in')
        except:
               messages.error(request, "User does not exist")
               return redirect('home:sign-in')

    return render(request, "home/sign-in.html")
def SignOutView(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("home:sign-in")
def deleteUserstemplate(request):
    return render(request, 'home/deleteUsers.html')
def deleteUsers(request):
    users = User.objects.all()
    for user in users:
        print(user)
        res = user.delete()
        return HttpResponse(res)

def viewUsersList(request):
    users = User.objects.all()
    return render(request, 'home/deleteByUserName.html', {'users':users})

def deleteByUserName(request, pk):
   result = User.objects.get(pk=pk)
   res = result.delete()
   return HttpResponse("user deleted: ", res)
def search(request):
    return render(request, 'home/searchByUserName.html')


def query(request):
    query = request.GET.get('query')
    results =  User.objects.filter(Q(username=query))
    if(results.exists()):
        return render(request, 'home/searchResults.html', {'results':results})
    else:
          return HttpResponse("no results found")


def searchByUserNameFilter(request):
    users = User.objects.all()
    searchByUserName_filter = searchUserFilter(request.GET, queryset = users)
    return render(request, 'home/searchResult.html', {'searchByUserName_filter':searchByUserName_filter})
