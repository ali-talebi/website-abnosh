from django.db import models
from ckeditor.fields import RichTextField 
# Create your models here.


class services(models.Model) : 
    STATUS_CHOICES = (
        ('a' , 'فعال' )  , 
        ('d' , 'غیر فعال ') 
    )

    type_service_CHOICES = (
    
        ("bi bi-chat-left-dots"  , 'مشاوره' ) , 
        ("bi bi-bounding-box" , 'طراحی') , 
        ("bi bi-bounding-box" , 'نصب' ) , 
        ("bi bi-broadcast" , 'تعمیرات') , 
        ("bi bi-broadcast" , 'ساخت') 

    )


    name = models.CharField(verbose_name = "نام خدمت"  , max_length = 200 ) 

    slug = models.SlugField(verbose_name = "آدرس خدمت "  , max_length = 200 , unique = True ) 

    descriptions = RichTextField(verbose_name = "توضیحات خدمت" , null = True , blank = True )


    picture = models.FileField(upload_to = "Image_Services" , verbose_name = "عکس خدمت"  , blank = True , null = True ) 


    status = models.CharField(verbose_name = "وضعیت" , max_length =1 , choices = STATUS_CHOICES  )

    type_service = models.CharField(verbose_name = "نوع خدمت" , max_length =50 , choices = type_service_CHOICES  , null = True , blank = True )


    def __str__(self ) : 
        return self.name 

    class Meta : 
        db_table = "services"

        verbose_name_plural = "خدمات" 
        

    
