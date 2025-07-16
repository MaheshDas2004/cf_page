from django.shortcuts import render,redirect
from . models import Confession
# Create your views here.
def confessions(request):
    all_confessions=Confession.objects.all().order_by('-created_at')
    if request.GET.get("create"):
        return render(request, 'confessions/confessions.html',
                      {"confessions":all_confessions,
                       "show_modal":True,
                       "confession":None})
    
    if request.GET.get("edit"):
        confession=Confession.objects.get(id=request.GET.get("edit"))
        return render(request, 'confessions/confessions.html',
                      {"confessions":all_confessions,
                       "show_modal":True,
                       "confession":confession})

    return render(request, 'confessions/confessions.html',{"confessions":all_confessions})


def my_confessions(request):
    user=request.user
    all_my_confessions=Confession.objects.filter(user=user).order_by('-created_at')
    return render(request, 'confessions/my_confessions.html',{"confessions":all_my_confessions})

def delete_confession(request,id):
    conf=Confession.objects.get(id=id)
    conf.delete()
    return redirect("confession")

    

def submit_confession(request):
    if request.method=="POST":
        confessionContent=request.POST.get("confessionContent")
        confession_id=request.POST.get("confession_id")
        user=request.user
        if(confession_id):
            confession=Confession.objects.get(id=confession_id)
            confession.content=confessionContent
            confession.save()
        else:
            Confession.objects.create(user=user,content=confessionContent)
        return redirect("confession")
        
