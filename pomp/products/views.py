from django.shortcuts import render , get_object_or_404  , redirect 
from .models import products , head_products , Hero_section , Frequency_questions  , Team_Member , Address  , Text_original_page
from services.models import services  
from django.http import HttpResponse 
from .forms import Contact_us_forms  , Newsletter_form , Newsletter_form2 
# Create your views here.





def Text_original_page_views(request) : 
    obj_text = Text_original_page.objects.all()
    context = {
        'data' : obj_text 
    }

    return render(request , 'website/index.html' , context )





def newsletter(request) : 
    if request.method == "GET"  :
        
        account = request.GET.get("email_account")

        form = Newsletter_form(account) 

        if form.is_valid()  : 
            form.save()

            return HttpResponse("با موفقیت عضو شدید")

    else : 
        form = Newsletter_form() 



    context = {'form2':form}

    return render(request , 'website/index.html' , context )









def Total_product(request) : 
    obj = products.objects.all()
    count_project = obj.count() 
    obj_services = services.objects.all()
    picture = Hero_section.objects.all() 
    team_member = Team_Member.objects.all()
    questions = Frequency_questions.objects.all() 
    address_list = Address.objects.all() 
    obj_text = Text_original_page.objects.all().order_by('number')
    

    if request.method == "POST" : 


        form = Contact_us_forms(request.POST) 
        if form.is_valid() : 
            form.save()

            return redirect("app1:Total_product")

        
    else : 
        form = Contact_us_forms()



    






    context = {'obj_text':obj_text , 'obj_address':address_list , 'form':form   ,  'members': team_member , 'count_project':count_project , 'obj' : obj , 'obj_services' : obj_services , 'picture' :picture , 'questions':questions  }
    return render(request , 'website/index.html' , context )








def details_of_product(request , slug , id  ) : 
    obj = get_object_or_404(products  , slug = slug  , id = id  ) 

    

    if request.method == "POST" : 
        form_news_letter = Newsletter_form(request.POST) 

        if form_news_letter.is_valid() : 
            form_news_letter.save()
            return redirect('app1:Total_product')


    else : 
        form_news_letter = Newsletter_form(request.POST) 




    content = {'obj1':obj , 'form_news_letter' : form_news_letter }
    return render(request , 'website/portfolio-details.html'  , content )



        





