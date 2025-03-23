from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField("სათაური", max_length=18, null=False, blank=False)
    author = models.CharField("ავტორი", max_length=18, null=False, blank=False)
    published_date = models.DateField()
    genres = models.ManyToManyField("Genre")  
    
    borrowed_by = models.CharField("მომხმარებელი", max_length=100, blank=True, null=True)  
    borrow_date = models.DateTimeField("აღების თარიღი", blank=True, null=True)  

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def is_borrowed(self):
        return bool(self.borrowed_by)
    
    def borrow(self, borrower_name):
        if not self.is_borrowed():
            self.borrowed_by = borrower_name
            self.borrow_date = timezone.now()
            self.save()
            return True
        return False
    
    def return_book(self):
        self.borrowed_by = None
        self.borrow_date = None
        self.save()
        return True

    def __str__(self):
        return self.title

class Genre(models.Model):  
    name = models.CharField("ჟანრი", max_length=50, null=False, blank=False)
    description = models.TextField("აღწერა", blank=True, null=True)  

    def __str__(self):
        return self.name
