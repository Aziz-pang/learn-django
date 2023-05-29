from django.shortcuts import render,HttpResponse
from django.http import JsonResponse, QueryDict
from app02.models import Department

from django.http.multipartparser import MultiPartParser


# Create your views here.
def dept_index(request):
  dept_list = Department.objects.all()
  print(dept_list)
  return render(request, 'list.html', {"dept_list":dept_list})

def dept(request):
    nid = request.params.get('id')
    dept_name = request.params.get('deptName')

    if request.method == 'POST':
      Department.objects.create(title=dept_name)

    if request.method == 'PUT':
      Department.objects.filter(id=nid).update(title=dept_name)

    if request.method == 'DELETE':
      Department.objects.filter(id=nid).delete()

    res_data = {"code":200, "data": dept_name, "msg": "请求成功"}
    return JsonResponse(res_data)

