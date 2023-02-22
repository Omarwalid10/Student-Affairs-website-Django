from unicodedata import name
from django.shortcuts import render
from base.models import Student
from .forms import StudentForm
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def BeginHomepage(request):
    return render(request,'BeginHomePage.html')

def homepage(request):
    return render(request,'HomePage.html')

def addstudent(request):
    submitted = False
    exist = False
    if request.method == "POST":
        std_name = request.POST['name']
        print(std_name)
        std_id = request.POST['id']
        print(std_id)
        students = Student.objects.all()
        for student in students:
            if student.ID == std_id:
                exist = True
                return render(request,'addstudent.html',{
                    "submitted": submitted,
                    "exist" : exist
                })
        std_GPA = request.POST['gpa']
        print(std_GPA)
        
        std_DOB = request.POST['data of birth']
        print(std_DOB)
        
        std_LEVEL = request.POST['level']
        std_Gender = request.POST['gender']
        std_Email = request.POST['email']
        std_Status = request.POST['status']
        std_Department = request.POST['department']
        std_Num = request.POST['phone']
        if str(std_Department) != "NULL" and exist == False:
            Student.objects.create(name= str(std_name), ID = str(std_id),GPA = str(std_GPA),dob = str(std_DOB),level = str(std_LEVEL),gender = str(std_Gender),email= str(std_Email),status = str(std_Status), department = str(std_Department),phone_Num = str(std_Num))
            submitted = True
        else:
            Student.objects.create(name= str(std_name), ID = str(std_id),GPA = str(std_GPA),dob = str(std_DOB),level = str(std_LEVEL),gender = str(std_Gender),email= str(std_Email),status = str(std_Status), department = "NULL",phone_Num = str(std_Num))
            submitted = True

        
        return render(request,'addstudent.html',{
            "submitted": submitted,
            "exist" : exist
        })
    else:
        return render(request,'addstudent.html',{
            "submitted": submitted
        })

def assign(request,departments,studentlist,searchedname):
            idx = 0
            print(departments)
            print(studentlist)
            List = list(studentlist)
            print(len(List))
            for student in List:
                print(student)
                if student.level > 2:
                    if departments[idx] != "":
                        print(student)
                        Name = student.name
                        talleb = Student.objects.filter(name = str(Name))
                        print("before:")
                        print(talleb)
                        talleb.update(department = str(departments[idx]))
                        print("after:")
                        print(talleb)
                        idx = idx + 1
                else:
                    continue
            success = True
            objects = Student.objects.filter(name__contains = searchedname)
            return render(request,'Assignment.html',{
                'studentlist': objects,
                'success' : success
            })

@csrf_protect
def assignment(request,SearchedName):
    studentlist = Student.objects.filter(name__contains = SearchedName)
    test = list(studentlist)
    success = False
    if len(test) == 0:
        return render(request,"404.html",{
            "name": SearchedName
    })
    else:
        if request.method == "POST":
            departments = request.POST.getlist('deps')
            return assign(request,departments,studentlist,SearchedName)
            idx = 0
            print(departments)
            print(studentlist)
            List = list(studentlist)
            print(len(List))
            for student in List:
                print(student)
                if student.level > 2:
                    print(student)
                    Name = student.name
                    talleb = Student.objects.filter(name = str(Name))
                    print("before:")
                    print(talleb)
                    talleb.update(department = str(departments[idx]))
                    print("after:")
                    print(talleb)
                    idx = idx + 1
                else:
                    continue

                objects = Student.objects.filter(name__contains = SearchedName)
                success = True
                return render(request,'Assignment.html',{
                    'studentlist': objects,
                    'success' : success
                })
        else:
            return render(request,'Assignment.html',{
                'studentlist': studentlist,
                'success' : success
            })

def search(request):
    if request.method == "POST":
        Name = request.POST['idStudent']
        return HttpResponseRedirect(reverse("assignment", args=(str(Name),)))
    else:    
        return render(request,'SearchStudent.html')

def editing(request,std_ID):
    if Student.objects.filter(pk=str(std_ID)).exists():
        talleb = Student.objects.get(pk = str(std_ID))
        return render(request,'editing.html',{
            'talleb': talleb,
        })
    else:
        return render(request,"404.html",{
            "name":std_ID
        })

def edit(request):
    if request.method == "POST":
        std_ID = request.POST['idStudent']
        return HttpResponseRedirect(reverse("editing", args=(str(std_ID),)))
    else:
        return render(request,'EditPage.html')

def update(request,std_ID):
    updated = False
    student = Student.objects.get(pk = str(std_ID))
    if request.method == "POST":
        std_name = request.POST['std_name']
        std_id = request.POST['std_id']
        std_GPA = request.POST['std_gpa']
        std_DOB = request.POST['std_date']
        std_LEVEL = request.POST['std_lvl']
        std_Gender = request.POST['std_gender']
        std_Email = request.POST['std_email']
        std_Status = request.POST['std_status']
        std_Num = request.POST['std_num']
        talleb = Student.objects.filter(pk = str(std_ID))
        talleb.update(name = std_name)
        talleb.update(ID = std_id)
        talleb.update(GPA = std_GPA)
        talleb.update(dob = std_DOB)
        talleb.update(level = std_LEVEL)
        talleb.update(gender = std_Gender)
        talleb.update(email = std_Email)
        talleb.update(status = std_Status)
        talleb.update(phone_Num= std_Num)
        updated = True
        return render(request,'Update.html',{
            "talleb": student,
            "updated": updated
        })
    else:
        return render(request,'Update.html',{
            "talleb": student,
            "updated": updated
        })

def delete(request,std_ID):
    student = Student.objects.filter(pk = str(std_ID))
    student.delete()
    return render(request,'Delete.html')

def studentlist(request):
    tmam = False
    students = Student.objects.all()
    if request.method == "POST":
        students.update(status = "INACTIVE")
        status_list = request.POST.getlist('checkboxes')
        for x in status_list:
            talleb = Student.objects.filter(pk = str(x))
            talleb.update(status = "ACTIVE")
        updated = Student.objects.all()
        tmam = True
        return render(request,'StudentsList.html',{
            'students':updated,
            'tmam' : tmam
        })
    else:
        return render(request,'StudentsList.html',{
            'students':students,
            'tmam': tmam
        })

