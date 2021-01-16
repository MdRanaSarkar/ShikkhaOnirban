from django.db import models
from django.utils.safestring import mark_safe
from django.shortcuts import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm, TextInput, NumberInput, EmailInput
# Create your models here.


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = models.TextField()
    address_short = models.CharField(max_length=200)
    phone = models.IntegerField()
    fax = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=50)
    smptserver = models.CharField(max_length=100)
    smtpemail = models.EmailField(blank=True, null=True, max_length=50)
    smptpassword = models.CharField(blank=True, max_length=50)
    smptport = models.CharField(blank=True, max_length=100)
    icon = models.ImageField(blank=True, null=True, upload_to='icon/')
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    address = models.TextField()
    contact = models.TextField()
    reference = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def IconURL(self):
        if self.icon:
            return self.icon.url
        else:
            return ""


class Category(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='category/')
    status = models.CharField(max_length=20, choices=status)
    description = models.TextField()
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))

    def get_absolute_url(self):
        return reverse('category_element', kwargs={'slug': self.slug})

    def imageurl(self):
        if self.image:
            return self.image.url


class SlideImages(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    detail = models.TextField()
    image = models.ImageField(blank=True, upload_to='slide_images/')
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=status)

    def __str(self):
        return self.title

    def imageurl(self):
        if self.image:
            return self.image.url

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
    image_tag.short_description = 'Image'


class Course(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='course/')
    new_price = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    old_price = models.DecimalField(decimal_places=2, max_digits=15)
    amount = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=3)
    detail = models.TextField()
    status = models.CharField(max_length=20, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_element', kwargs={'slug': self.slug})

    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return " "


class CourseImages(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='course/')

    def __str(self):
        return self.title

    def imageurl(self):
        if self.image:
            return self.image.url


class Event(models.Model):
    status = (
        ('upcoming', 'upcoming'),
        ('done', 'done'),)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    detail = models.TextField()
    image = models.ImageField(blank=True, upload_to='event_images/')
    location = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    starting_time = models.TimeField()
    finishing_time = models.TimeField()
    slug = models.SlugField(null=True, unique=True)
    status = models.CharField(max_length=20, choices=status)

    def __str(self):
        return self.title

    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
    image_tag.short_description = 'Image'


class EventImages(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='event_images/')

    def __str(self):
        return self.title

    def imageurl(self):
        if self.image:
            return self.image.url


class About(models.Model):
    title = models.CharField(max_length=200, blank=True)
    detail = models.TextField()
    image = models.ImageField(blank=True, upload_to='about/')
    choosing_reason = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    vission = models.TextField(blank=True)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str(self):
        return self.title

    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return ''

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
    image_tag.short_description = 'Image'







class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),

    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=200, blank=True)
    message = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    ip = models.CharField(max_length=100, blank=True)
    Note = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name & Sure name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Write your email'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Wrte your Subjects'}),
            'message': TextInput(attrs={'class': 'input', 'placeholder': 'Write your messages'}),
        }






class Subject(models.Model):
    subject=models.CharField(max_length=200)
    interested=models.BooleanField()


    def __str__(self):
        return self.subject