from django.shortcuts import render, get_object_or_404

from .models import *
from .forms import * 
# Create your views here.

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages

def MainPost(request): 
    object_list = Post.objects.all()
    
 
    #paginator = Paginator(object_list, 4) # 3 posts in each page 
    #page = request.GET.get('page') 
    #try: 
        #posts = paginator.page(page) 
    #except PageNotAnInteger: 
        # If page is not an integer deliver the first page 
        #posts = paginator.page(1) 
    #except EmptyPage: 
        # If page is out of range deliver last page of results 
        #posts = paginator.page(paginator.num_pages) 

    return render(request, 'Post/MainPost.html', {#'page': page, 
                                                   #'posts': posts, 
                                                  
                                                   'object_list': object_list,
                                                  
                                       
                                                  }) 

    

def AllFeaturePost(request): 
    object_list = Post.objects.all()
    
 
    #paginator = Paginator(object_list, 4) # 3 posts in each page 
    #page = request.GET.get('page') 
    #try: 
        #posts = paginator.page(page) 
    #except PageNotAnInteger: 
        # If page is not an integer deliver the first page 
        #posts = paginator.page(1) 
    #except EmptyPage: 
        # If page is out of range deliver last page of results 
        #posts = paginator.page(paginator.num_pages) 

    return render(request, 'Post/AllFeaturePost.html', {#'page': page, 
                                                   #'posts': posts, 
                                                  
                                                   'object_list': object_list,
                                                  
                                       })

def AboutUs(request): 
    object_list = Person.objects.all()
    
 
    #paginator = Paginator(object_list, 4) # 3 posts in each page 
    #page = request.GET.get('page') 
    #try: 
        #posts = paginator.page(page) 
    #except PageNotAnInteger: 
        # If page is not an integer deliver the first page 
        #posts = paginator.page(1) 
    #except EmptyPage: 
        # If page is out of range deliver last page of results 
        #posts = paginator.page(paginator.num_pages) 

    return render(request, 'Post/AboutUs.html', {#'page': page, 
                                                   #'posts': posts, 
                                                  
                                                   'object_list': object_list,
                                                  
                                       })

def ContactUs(request): 

    if request.method == 'POST':
        # A comment was posted
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            from_email = contact_form.cleaned_data['from_email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(from_email, subject, message,['jtnay12@gmail.com'],fail_silently=False)
                messages.success(request, "Message have been sucessfully send.")
            except BadHeaderError:
                messages.success(request, "Message have fail to send.")
            
            return render(request, 'Post/SucessEmail.html', {#'page': page, 
                                                   #'posts': posts, 
                                                  
                                                 
                                                   'contact_form':contact_form,
                                                   
                                       })
    else:
        contact_form = ContactForm()
        
    
 
    #paginator = Paginator(object_list, 4) # 3 posts in each page 
    #page = request.GET.get('page') 
    #try: 
        #posts = paginator.page(page) 
    #except PageNotAnInteger: 
        # If page is not an integer deliver the first page 
        #posts = paginator.page(1) 
    #except EmptyPage: 
        # If page is out of range deliver last page of results 
        #posts = paginator.page(paginator.num_pages) 

    return render(request, 'Post/ContactUs.html', {#'page': page, 
                                                   #'posts': posts, 
                                                  
                                                 
                                                   'contact_form':contact_form,
                                                   
                                       })


