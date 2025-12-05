from django.shortcuts import render

# Create your views here.
def about_view(request):
    return render(request, 'pages/about_me.html')

def experience_view(request):
    return render(request, 'pages/experience.html')