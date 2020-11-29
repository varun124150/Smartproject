

# Create your views here.
from django.shortcuts import render,redirect
from .models import Employee
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(request):
    
    return render(request,'home.html')


def add(request):
   if request.method == "POST":
      Employe_name=request.POST.get("Employe_name")
      Employe_phone=request.POST.get("Employe_phone")
      Employe_department=request.POST.get("Employe_department")
      Employe_Email=request.POST.get("Employe_Email")
      Employe_Adress=request.POST.get("Employe_Adress")
      uploaded_file = request.FILES['document']
      #fs = FileSystemStorage()
      #name = fs.save(uploaded_file.name,uploaded_file)
      #url = fs.url(name)
      obj=Employee(name=Employe_name, phone=Employe_phone, department=Employe_department ,email=Employe_Email, picture=uploaded_file,address=Employe_Adress)
      obj.save()

      return redirect("home")
      
   
   #code
   else:
      
      return render(request,'add.html')
      
def show(request):
    employee=Employee.objects.all()
    context={
            "employee":employee
            }
    return render(request,'show.html',context)

