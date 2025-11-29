from django .http import HttpResponse
from django .shortcuts import render
def index(request):
    param={'name':'Akash','place':'india'}
    return render(request,'index.html',param) 
    

# def about(request):
#     return HttpResponse('<h1>hello world</h1>')
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc= request.POST.get('removepunc','off')
    UPPERcase= request.POST.get('UPPERCASE','off')
    newline= request.POST.get('newlineremover','off')
    spaceremover= request.POST.get('spaceremover','off')
    charcounter= request.POST.get('charcounter','off')
    if removepunc=='on':
        analyzed=''
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i
        params={'purpose':'removed punctuation','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    if(UPPERcase=='on'):
        analyzed =''
        for char in djtext:
            analyzed=analyzed + char.upper()
        params={'purpose':'Change to Upper case ','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    if(newline=='on'):
        analyzed=''
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
        params={'purpose':'new line remover','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if(spaceremover=='on'):
        analyzed=''
        for index, char in enumerate(djtext):
              if index + 1 < len(djtext):
                if not(djtext[index]==" " and djtext[index+1]==" "):
                    analyzed=analyzed+char
        params={'purpose':'space remover','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
    if(charcounter=='on'):
        analyzed = 0
        in_word = False
        for ch in djtext:
            if not ch.isspace() and not in_word:
                analyzed+= 1
                in_word = True
            elif ch.isspace():
                 in_word = False

        params={'purpose':'number of character','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    if(charcounter!='on'and spaceremover!='on' and newline!='on' and UPPERcase!='on' and removepunc!='on'):
        return HttpResponse("Select the operation ")

    return render(request,'analyze.html',params)
    
