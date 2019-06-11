#coding:utf-8
'''
Created on 2013-11-11
@author: Administrator
'''
from app import models
from company import settings
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request): 
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME
    return render_to_response('index.html',context,context_instance=RequestContext(request))

def faq(request): 
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME
    cats = models.FaqCategory.objects.order_by('id')[0:1]
    if cats:
        context['catname'] = cats[0].catname
        faqs = models.Faq.objects.filter(catid=cats[0].id).order_by("id")
        context['faqs'] = faqs
    return render_to_response('faq.html',context,context_instance=RequestContext(request))

def faq_cat_detail(request,catid):
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME
    cat = models.FaqCategory.objects.get(id=catid)
    context['catname'] = cat.catname
    faqs = models.Faq.objects.filter(catid=catid).order_by("id")
    context['faqs'] = faqs
    return render_to_response('faq.html',context,context_instance=RequestContext(request))

def about(request): 
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME
    cats = models.AboutCategory.objects.order_by('id')[0:1]
    if cats:
        context['catname'] = cats[0].catname
        abouts = models.About.objects.filter(catid=cats[0].id).order_by("id")
        context['abouts'] = abouts
    return render_to_response('about.html',context,context_instance=RequestContext(request))

def about_cat_detail(request,catid): 
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME
    cat = models.AboutCategory.objects.get(id=catid)
    context['catname'] = cat.catname
    abouts = models.About.objects.filter(catid=catid).order_by("id")
    context['abouts'] = abouts
    return render_to_response('about.html',context,context_instance=RequestContext(request))

def service(request): 
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME
    cats = models.ServiceCategory.objects.order_by('id')[0:1]
    if cats:
        context['catname'] = cats[0].catname
        services = models.Service.objects.filter(catid=cats[0].id).order_by("id")
        context['services'] = services
    return render_to_response('service.html',context,context_instance=RequestContext(request))

def service_cat_detail(request,catid): 
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME
    cat = models.ServiceCategory.objects.get(id=catid)
    context['catname'] = cat.catname
    services = models.Service.objects.filter(catid=catid).order_by("id")
    context['services'] = services 
    return render_to_response('service.html',context,context_instance=RequestContext(request))

def products(request): 
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME
    cats = models.ProductCategory.objects.order_by('id')[0:1]
    if cats:
        context['catname'] = cats[0].catname
        products = models.Products.objects.filter(catid=cats[0].id).order_by("id")
        context['products'] = products
    return render_to_response('products.html',context,context_instance=RequestContext(request))

def product_cat_detail(request,catid): 
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME
    cat = models.ProductCategory.objects.get(id=catid)
    context['catname'] = cat.catname
    products = models.Products.objects.filter(catid=catid).order_by("id")
    context['products'] = products
    return render_to_response('products.html',context,context_instance=RequestContext(request))

def download(request): 
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME
    cats = models.DownloadCategory.objects.order_by('id')[0:1]
    if cats:
        context['catname'] = cats[0].catname
        downloads = models.Download.objects.filter(catid=cats[0].id).order_by("id")
        context['downloads'] = downloads
    return render_to_response('download.html',context,context_instance=RequestContext(request))

def download_cat_detail(request,catid):
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME
    cat = models.DownloadCategory.objects.get(id=catid)
    context['catname'] = cat.catname
    downloads = models.Download.objects.filter(catid=catid).order_by("id")
    context['downloads'] = downloads
    return render_to_response('download.html',context,context_instance=RequestContext(request))

def news(request):
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME  
    news = models.News.objects.all()
    context['items'] = news 
    return render_to_response('news.html',context,context_instance=RequestContext(request))

def news_detail(request,newsid):
    context={}
    context.update(csrf(request))
    context['webname']=settings.WEB_NAME  
    news = models.News.objects.get(id = newsid) 
    context['news'] = news
    return render_to_response('news_detail.html',context,context_instance=RequestContext(request))
    
    
