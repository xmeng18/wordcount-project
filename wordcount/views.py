from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html',{'hithere':'this is me'})

def count(request):
    fulltext = request.GET['“fulltext”']
    #fulltext = request.GET.get('“fulltext”')
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords=sorted(worddictionary.items(),key = operator.itemgetter(1), reverse = True)

    return render(request,'count.html',\
    {'fulltext':fulltext, 'count':len(wordlist),'worddictionary':sortedwords})

def readme(request):
    return render(request,'readme.html',{'name':'Xiangyu Meng'})
