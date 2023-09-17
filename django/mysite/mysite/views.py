#created by me
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("hello")
# def about(request):
#     return HttpResponse(''' <h1>hello about </h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> click here </a>''')
# def nav(request):
#     return HttpResponse(''' click here for your sites\n <a href="https://www.google.com/">google</a> <a href="https://www.whatsapp.com/">whatsapp</a> <a href="https://www.facebook.com/">facebook</a>''')

def index(request):
    params={'name':'suro','place':'mars'}
    return render(request,'index2.html', params)
    # return HttpResponse("home")
def analyze(request):
     djtext= request.POST.get('text','default')
     print(djtext)
     removepunc=request.POST.get('removepunc','off')
     capitalize=request.POST.get('capitalize','off')
     extraspaceremover=request.POST.get('extraspaceremover','off')
     newlineremover=request.POST.get('newlineremover','off')
     charcount=request.POST.get('charcount','off')
     # print(removepunc)
     if removepunc=="on":
         punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ '''
         analyze= ""
         for char in djtext:
             if char not in punctuations:
                 analyze =analyze + char
         params={'purpose':'removed punctuations','analyzed_text':analyze}
         # return render(request,'analyze2.html',params)
         djtext=analyze

     if capitalize=="on":
         analyze=""
         for char in djtext:
             analyze=analyze +char.upper()
         params = {'purpose': 'Capitalize Text', 'analyzed_text': analyze}
         djtext = analyze
         # return render(request, 'analyze2.html', params)

     if extraspaceremover == "on":
         analyze = ""
         for index, char in enumerate(djtext):
             if not(djtext[index]==" " and djtext[index+1]==" "):
                 analyze = analyze + char
         params = {'purpose': 'Remove extra space ', 'analyzed_text': analyze}
         djtext = analyze
         # return render(request, 'analyze2.html', params)

     if newlineremover == "on":
         analyze = ""
         for char in djtext:
             if char !="\n" and char!="\r":

                 analyze = analyze + char
         params = {'purpose': 'Remove new line', 'analyzed_text': analyze}
         djtext = analyze
         # return render(request, 'analyze2.html', params)

     if charcount == "on":
         analyze = ""
         for char in djtext:
              analyze =len(djtext)
         params = {'purpose': 'Count characters', 'analyzed_text': analyze}

     if( removepunc!="on" and capitalize!="on" and extraspaceremover != "on" and charcount != "on" and newlineremover != "on" ):
        return HttpResponse("Error")



     return render(request, 'analyze2.html', params)






