from django.contrib import admin
from .models import Text_original_page , head_products , products , Tags , Hero_section  , Frequency_questions , Team_Member , Contact_us , Newsletter , Address 

# Register your models here.



@admin.register(Text_original_page) 
class Text_original_page_Admin(admin.ModelAdmin) : 
    list_display = ("number" , "head" , )

@admin.register(Address)
class Address_Admin(admin.ModelAdmin) : 
    list_display = ("address" , "phone1" , "phone2" , "email" ) 
    search_fields = ("address" , "phone1" ,  "phone2" , "email")

    fields = ("address" , ("phone1" , "phone2" , "email" ) )  




@admin.register(Newsletter)
class Newsletter_admin(admin.ModelAdmin) : 
    list_display = ("email_member" , )
    search_fields = ("email_member" , )








@admin.register(Contact_us)
class Contact_us_Admin(admin.ModelAdmin) : 
    list_display = ("full_name" , "email" , "subject" )
    fields = (("full_name" , "email" ) , "subject")
    search_fields = ("full_name" , "email" , "subject" )
    




@admin.register(Team_Member)
class Team_Member_Admin(admin.ModelAdmin) : 
    list_display = ("Full_name" , "level" , "linkedin"   ) 
    list_editabl = ("level" , )

    search_fields = ("name" , "linkedin") 





@admin.register(Frequency_questions)
class Frequency_questions_admin(admin.ModelAdmin) : 
    list_display = ('question' , 'answer' ) 







@admin.register(Hero_section)
class Hero_section_admin(admin.ModelAdmin) : 
    list_display = ("name" , "sentence" , )
    search_fields = ("name" , )
    


@admin.register(Tags) 
class Tags_Admin(admin.ModelAdmin): 
    list_display = ("name" , )



@admin.register(head_products) 
class head_products_Admin(admin.ModelAdmin) : 
    list_display = ("name" , "slug")
    search_fields = ("name" , )
    
    prepopulated_fields = {'slug':('name' ,  )}
    
    
    
@admin.register(products) 
class products_Admin(admin.ModelAdmin) : 
    list_display = ("category" , "slug" , "applications"  , "name" , "get_tags" , "weigth" , "size_width" , "size_length" , "Id_product" , "date" )
    list_editabl = ( "status" ,  )
    search_fields = ("category" , "name" ) 
    prepopulated_fields = {'slug' : ('name' ,'category' , )}
    
    
    def get_tags(self , obj ) : 
        return ' , '.join([i.name for i in obj.tags.all() ])
    
    get_tags.short_description = "کلمات کلیدی"