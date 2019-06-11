#coding:utf-8
'''
Created on 2013-11-11
@author: Administrator
'''

from app.models import Announcement, Products, News, FaqCategory, \
    ProductCategory, ServiceCategory, AboutCategory, DownloadCategory, Faq, About, \
    Service, Download
from django.contrib import admin


class ExtendAnnouncement(admin.ModelAdmin): 
    list_display = ('id','title','content') 
    fields = ('title' , 'content')  
    list_per_page = 20
    
class ExtendProducts(admin.ModelAdmin): 
    list_display = ('id','catid','product_name','product_simple_desc','product_order') 
    fields = ('catid','product_name' , 'product_simple_desc' , 'product_full_desc' , 'product_pic' ,'product_order' , 'createddate')  
    list_per_page = 20
    
class ExtendNews(admin.ModelAdmin):
    list_display = ('id','title','createddate') 
    fields = ('title','content','createddate')  
    list_per_page = 20
    
class ExtendFaqCategory(admin.ModelAdmin):
    list_display = ('id','catname')     
    list_per_page = 20
    
class ExtendProductCategory(admin.ModelAdmin):
    list_display = ('id','catname')     
    list_per_page = 20
    
class ExtendProductServiceCategory(admin.ModelAdmin):
    list_display = ('id','catname')     
    list_per_page = 20
    
class ExtendAboutCategory(admin.ModelAdmin):
    list_display = ('id','catname')     
    list_per_page = 20
    
class ExtendDownloadCategory(admin.ModelAdmin):
    list_display = ('id','catname')     
    list_per_page = 20
    
class ExtendFaqs(admin.ModelAdmin):
    list_display = ('id','catid','title')     
    list_per_page = 20
    
class ExtendAbout(admin.ModelAdmin):
    list_display = ('id','catid','title')     
    list_per_page = 20
    
class ExtendService(admin.ModelAdmin):
    list_display = ('id','catid','title')     
    list_per_page = 20
    
class ExtendDownload(admin.ModelAdmin):
    list_display = ('id','catid','title','downloadurl')     
    list_per_page = 20
    

admin.site.register(Announcement , ExtendAnnouncement)
admin.site.register(Products , ExtendProducts)
admin.site.register(News , ExtendNews)

admin.site.register(FaqCategory , ExtendFaqCategory)
admin.site.register(ProductCategory , ExtendProductCategory)
admin.site.register(ServiceCategory , ExtendProductServiceCategory)
admin.site.register(AboutCategory , ExtendAboutCategory)
admin.site.register(DownloadCategory , ExtendDownloadCategory)

admin.site.register(Faq,ExtendFaqs)
admin.site.register(About,ExtendAbout)
admin.site.register(Service,ExtendService)
admin.site.register(Download,ExtendDownload)
