from django.shortcuts import render

def index(request,inp):
    b=inp.split(" ")

  
    a,b,c,d=int(b[0]),int(b[1]),int(b[2]),int(b[3])
    if a>b>c>d:
        e=a
    elif b>c>d:
        e=b
    elif c>d:
        e=c
    else:
        e=d
    return render(request,'index.html',{'greater':e})

def index1(request,id1):
    name=['name','phono','designation','sal']
    det=[['adarsh',9481422585,'programmer',50000],['rajesh',9481422585,'programmer',50000],['sharanya',9481422585,'programmer',50000]]
    id2=int(id1)
   
    if id2>=len(det):
        b=False
    else:
         b=det[id2]
    return render(request,"index2.html",{'det':b,'name':name})