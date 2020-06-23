from django.db import models

language_choice = [('english','english'),('hindi','hindi'),('urdu','urdu'),('marathi','marathi')]
condition_choice = [('good','good'),('bad','bad'),('very_good','very good'),('very_bad','very bad')]
subject_choice = [('Question_bank','Question bank'),('Handbook','Handbook'),('Worksheet','Worksheet')]



class BookCategories(models.Model):
    category_choice = (
        ('Engineering','Engineering'),
        ('Medical','Medical'),
        ('AIEEE','AIEEE'),
        ('NEET','NEET'),
        ("CAT",'CAT'),
        ('PHYSICS','PHYSICS')
    )
    title = models.CharField(max_length=200,choices=category_choice)

    def __str__(self):
        return self.title

class Book(models.Model):
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category_id = models.ManyToManyField(BookCategories)
    book_type = models.CharField(max_length=200,choices=(('used','used'),('donated','donated')))
    publication = models.CharField(max_length=50)
    binding_cover = models.CharField(max_length=200,choices=(('paperback','paperback'),('hardback','hardback')))
    book_condition = models.CharField(max_length=200,choices=condition_choice)
    subject = models.CharField(max_length=200,choices=subject_choice)
    languages = models.CharField(max_length=200,choices=language_choice)
    price = models.FloatField()
    image = models.FileField()
    slug = models.SlugField(unique=True)

    class Meta:
        unique_together = ('title','slug')

    def __str__(self):
        return self.title






