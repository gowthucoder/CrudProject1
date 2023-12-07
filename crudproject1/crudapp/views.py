from django.shortcuts import render,redirect
from crudapp.models import Student
from crudapp.form  import StudentForm

def read(request):
    student=Student.objects.all()
    return render(request, 'apps/result.html',{'s':student})
def insert(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'apps/insert.html',{'form':form})
def delete(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return redirect('/result')
def update(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/result')
    return render(request,'apps/update.html',{'s':student})

# Create your views here.
