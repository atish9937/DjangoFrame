from django.shortcuts import render, HttpResponse
from .models import *
hc = HeaderCode.objects.get(pageid=101).Header_Codes
def home(request):
    context={"name":'atish','hc':hc}
    return render(request,'downloader/home.html',context)
def downloader(request,slug):
    data=Downloader.objects.filter(Slug=slug)
    context={"name":'atish','hc':hc,'data':data}
    return render(request,'downloader/downloader.html',context)
def privacy(request):
    return render(request, "downloader/privacy.html")
def terms(request):
    return render(request, "downloader/terms.html")
def dmca(request):
    return render(request, "downloader/dmca.html")
def disclaimer(request):
    return render(request, "downloader/disclaimer.html")
def contactus(request):
    return render(request, "downloader/contactus.html")
def robots(request):
    context= RenderTxt.objects.get(pageid=101).Robots
    return HttpResponse(context)
def ads(request):
    context= RenderTxt.objects.get(pageid=101).Ads
    return HttpResponse(context)
