from django.db import models
from django.utils import timezone  
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.





class Text_original_page(models.Model) : 


    





    
    number = models.IntegerField(verbose_name = "شماره " , null = True , blank = True )
    head = models.CharField(verbose_name= "سر تیتر " , max_length = 100 )
    body = models.TextField(verbose_name = "متن "  ) 
    
    class Meta : 
        db_table= "Text_original_page"
        verbose_name_plural = "متن برای صفحه اصلی " 

        









class Address(models.Model) : 
    address = models.CharField(verbose_name = "آدرس ما " , max_length = 500 )
    phone1 = models.IntegerField(verbose_name =  "شماره تلفن 1 " )
    phone2 = models.IntegerField(verbose_name =  "شماره تلفن 2 " )  

    email = models.EmailField(verbose_name = "ایمیل")

    class Meta : 
        db_table = "Address"
        verbose_name_plural = "آدرس ما " 




    








class  Newsletter(models.Model) : 

    email_member = models.EmailField(verbose_name = "ایمیل"  , max_length = 300 )



    def __str__(self) : 
        return self.email_member  


    class Meta : 

        db_table = "Newsletter"
        verbose_name_plural = "خبرنامه"




class Contact_us(models.Model) : 
    full_name  = models.CharField(verbose_name = "نام و نام خانوادگی"  , max_length = 200  )
    email = models.EmailField(verbose_name = "ایمیل" , max_length = 300 )
    subject = models.CharField(verbose_name = "موضوع" , max_length = 200 ) 
    message = models.TextField(verbose_name = "متن پیام " )


    def __str__(self) : 
        return self.full_name 

    class Meta : 
        db_table = "Contact_us"
        verbose_name_plural = "ارتباط با ما "








class Team_Member(models.Model) : 

    level_status = (
        ('Leader' , 'مدیر عامل' ) , 
        ('client' , 'کارمند' )  , 

    )
    Full_name = models.CharField(verbose_name = "اسم کامل" , max_length = 100 ) 

    level = models.CharField(verbose_name = "سمت فرد" ,  choices = level_status  , max_length = 100 ) 
    picture = models.FileField(verbose_name = "عکس افراد"  , upload_to = "Image_Team_Member/" , null = True , blank = True )
    linkedin = models.CharField(verbose_name = "آدرس لینکدین" , max_length = 100 , blank = True , null = True )
    instagram = models.CharField(verbose_name = "آدرس اینستاگرام" , max_length = 100 , null = True , blank = True )


    






    def __str__(self ) : 
        return self.Full_name 

    class  Meta : 
        db_table = "Team_Member" 
        verbose_name_plural = "اعضا"






class Hero_section(models.Model) : 
    name = models.CharField(verbose_name = "نام عکس " , blank = True , null = True , max_length = 100 )
    sentence = models.CharField(verbose_name = "جمله مورد نظر برای  صفحه اول وبسایت " , max_length = 300 , blank = True , null = True ) 
    picture  = models.FileField(verbose_name = "عکس صفحه اول وبسایت "   , upload_to = "Image_First_Page/" , blank = True , null  = True ) 


    def  __str__(self) : 
        return self.name 


    class Meta : 
        db_table = "Hero_section"

        verbose_name_plural = "عکس های صفحه اولیه وبسایت "





class Frequency_questions(models.Model) : 

    question = models.CharField(verbose_name = "سوال" , blank = True , null = True , max_length = 300 )
    answer   = models.TextField(verbose_name = "جواب" , blank = True , null = True   )


    def __str__(self) : 
        return self.question[:50]

    class Meta : 
        db_table = "Frequency_questions"

        verbose_name_plural = "سوالات متداول"





class head_products(models.Model) : 
    name = models.CharField(verbose_name="نام دسته محصول" , max_length= 200 )
    slug = models.SlugField(verbose_name="آدرس" , blank=True , null = True )
    
    
    def __str__(self) : 
        return self.name 
    
    class Meta : 
        db_table = "head_products"
        verbose_name_plural = "دسته بندی اصلی محصولات"
        
        
        
        
class Tags(models.Model) : 
    name = models.CharField(verbose_name="نام کلمه کلیدی" , max_length= 200 )
    
    def __str__(self) : 
        return self.name 
    
    class Meta : 
        db_table = "Tags" 
        verbose_name_plural = "کلمات کلیدی" 
        
        
        
        
        
class products(models.Model) : 
    STATUS_CHOICES = (
        ('d' , 'پیش نویس') , 
        ('p' , 'منتشر')  
    )


    type_product_status = (
        ("col-lg-4 col-md-6 portfolio-item filter-app" , 'تابلو')  , 
        ("col-lg-4 col-md-6 portfolio-item filter-card" , 'پمپ' )  , 
    )



    category = models.ForeignKey('head_products' , verbose_name="دسته بندی اصلی محصول" , null=True , on_delete=models.CASCADE , blank = True ) 
    name = models.CharField(verbose_name="نام محصول" , max_length=200 )
    slug = models.SlugField(verbose_name="آدرس محصول" , null = True , blank = True , max_length= 200 , unique= True  )
    picture = models.FileField(verbose_name="عکس محصول" , upload_to= "Products_Image" , blank = True , null = True ) 
    picture2 = models.FileField(verbose_name = "عکس 2 محصول " , upload_to = "Products_Image" , blank = True , null = True ) 
    picture3 = models.FileField(verbose_name = "عکس 3 محصول " , upload_to = "Products_Image" , blank = True , null = True ) 

    descriptions = RichTextField(verbose_name = "توضیحات محصول "  , blank = True , null = True  )
    size_length = models.IntegerField(verbose_name="  سایز طول محصول بر حسب سانتی متر "  , null = True , blank = True )
    size_width  =  models.IntegerField(verbose_name="سایز عرض محصول بر حسب سانتی متر "  , null = True , blank = True )
    weigth = models.IntegerField(verbose_name="وزن محصول بر حسب کیلو گرم" , null = True , blank = True )
    status = models.CharField(verbose_name="وضعیت"  , max_length =  1 , blank = True , null = True , default = "p"   , choices= STATUS_CHOICES )
    
    applications = models.CharField(verbose_name="کاربرد ها محصول" , max_length= 500 , null = True , blank = True ) 
    tags = models.ManyToManyField('Tags' , verbose_name="کلمات کلیدی" )
    Id_product = models.IntegerField(verbose_name="بارکد یا کد محصول " , null = True , blank = True )
    date = models.DateTimeField(verbose_name="تاریخ"  , null = True , blank = True , default=timezone.now )
    
    type_product = models.CharField(verbose_name = "نوع محصول " , max_length = 50  , choices = type_product_status , null = True , blank = True )
    
    def __str__(self) : 
        return self.name  
    
    
    def get_absolute_url(self):
        return reverse("app1:details_of_product", args = [ self.slug , str(self.id)])
    
    
    
    class Meta : 
        db_table = "products"
        verbose_name_plural = "محصولات"