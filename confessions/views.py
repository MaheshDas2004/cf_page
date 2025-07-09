from django.shortcuts import render,redirect
from . models import Confession
# Create your views here.
def confessions(request):
    if request.method=="POST":
        show_modal=True
        print("dikh rha ha binod")
        return render(request,'confessions/confessions.html',{"show_modal":show_modal})
    
    all_confessions=Confession.objects.all().order_by('-created_at')
    return render(request, 'confessions/confessions.html',{"confessions":all_confessions})
def submit_confession(request):
    if request.method=="POST":
        confession=request.POST.get("confession")
        user=request.user
        print(user.username)
        print(confession)
        Confession.objects.create(user=user,content=confession)
        return redirect("confession")
        
