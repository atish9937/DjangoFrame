from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Pages(models.Model):
    pageid=models.IntegerField(default=101)
    privacy=RichTextField(blank=True)
    termsandcondition=RichTextField(blank=True)
    dmca=RichTextField(blank=True)
    disclaimer=RichTextField(blank=True)
    contactus=RichTextField(blank=True)
    def __str__(self):
        return "Pages"
    
class HomePage(models.Model):
    CHOICES=(('Yes','Yes'),('No','No'))
    pageid=models.IntegerField(default=101)
    Name=models.CharField(max_length=60,blank=False,default='Home')
    ShowAllDownloader=models.CharField(max_length=6,choices=CHOICES,default='No')
    # Slug=models.SlugField(max_length=200,allow_unicode=True, blank=True)
    Meta_Title=models.CharField(max_length=80,blank=True)
    Meta_Description=models.CharField(max_length=200,blank=True)
    Featured_Image=models.ImageField(upload_to='uploads/featuredimages/', blank=True)
    Logo=models.ImageField(upload_to='uploads/logos/', blank=True)
    Body_Title=models.CharField(max_length=80,blank=True)
    Content_Above_DownloadersList=RichTextUploadingField(blank=True)
    Content_Below_DownloadersList=RichTextUploadingField(blank=True)
    Recently_Downloaded=models.TextField(blank=True)
    Updatedon=models.DateTimeField(auto_now=True,blank=True)
    def __str__(self):
        return 'HomePage'
class Downloader(models.Model):
    CHOICES=(('Yes','Yes'),('No','No'))
    Name=models.CharField(max_length=60,blank=False)
    Enable=models.CharField(max_length=6,choices=CHOICES,default='No')
    Slug=models.SlugField(max_length=200,allow_unicode=True, blank=True,unique=True)
    Meta_Title=models.CharField(max_length=80,blank=True)
    Meta_Description=models.CharField(max_length=200,blank=True)
    Featured_Image=models.ImageField(upload_to='uploads/featuredimages/', blank=True)
    Logo=models.ImageField(upload_to='uploads/logos/', blank=True)
    Body_Title=models.CharField(max_length=80,blank=True)
    Content_Above_InputField=RichTextUploadingField(blank=True)
    Content_Below_InputField=RichTextUploadingField(blank=True)
    Recently_Downloaded=models.TextField(blank=True)
    Updatedon=models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.Name
    def save(self,*args, **kwargs):
        if not self.Slug:
            self.Slug = slugify(self.Name,allow_unicode=True)
        return super().save(*args,**kwargs)
class RenderTxt(models.Model):
    pageid=models.IntegerField(default=101)
    Robots=RichTextField(blank=True)
    Ads=RichTextField(blank=True)
class HeaderCode(models.Model):
    pageid=models.IntegerField(default=101)
    Header_Codes=models.TextField(blank=True)
    def __str__(self):
        return "Header"



