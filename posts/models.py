from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم التصنيف")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "التصنيف"
        verbose_name_plural = "التصنيفات"


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'مسودة'),
        ('published', 'منشور'),
    )
    title = models.CharField(max_length=200, verbose_name="العنوان")
    content = models.TextField(verbose_name="المحتوى")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ النشر")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="الكاتب")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="الحالة")
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='post', 
        verbose_name="التصنيف"
    )
    image = models.ImageField(upload_to='post_images/',blank=True, null=True, verbose_name='الصورة')
    class Meta:
        ordering = ['-date_created']
        verbose_name = 'مقال'
        verbose_name_plural = 'المقالات'


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.text