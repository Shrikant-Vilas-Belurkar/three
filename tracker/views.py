from django.shortcuts import render

# Create your views here.
def tracker(r):
    return render(r, 'tracker.html')