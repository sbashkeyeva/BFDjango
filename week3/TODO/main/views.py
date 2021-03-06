from django.shortcuts import render
from datetime import datetime, timedelta

from django.http import HttpResponse

def listed(request):
    tasks=[{
        'Name':'Task {}'.format(i),
        'Created': datetime.today().strftime("%d/%m/%y"),
        'Dueon':(datetime.today()+timedelta(days=2)).strftime("%d/%m/%y"),
        'Owner': 'admin',
        'Mark': 'Done',
        'Isnotcompl': True
    } for i in range (1,5)]
    context={'tasks': tasks}
    return render(request,'todo_list.html',context)
def completed(request):
    texts =[{
        'Name': 'Task 0',
        'Created': datetime.today().strftime("%d/%m/%y"),
        'Dueon': (datetime.today()+timedelta(days=2)).strftime("%d/%m/%y"),
        'Owner':'admin',
        'Mark':'Not Done',
        'Isnotcompl': False
    }]
    context = {'keys': texts}
    return render(request,'completed_todo_list.html',context)

