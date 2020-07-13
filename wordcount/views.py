from django.shortcuts import render
import random
# Create your views here.


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request,'result.html',{'fulltext' : full_text,'count' : len(word_list),'dictionary' : word_dictionary.items()})

def jebi(request): 
    return render(request,'jebi.html',)

def jebi_result(request):
     
    people= request.GET['jebi']
    
    people_list = people.split()

    return render(request,'jebi_result.html',{'random' : random.choice(people_list)})