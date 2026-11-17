from django.db import models

# Create your models here.

# Створення моделей портфоліо
#
# Модель Project (назва, опис, технології, дата, зображення, GitHub посилання)
# Модель Skill (назва, рівень володіння, категорія)
# Модель Experience (посада, компанія, період, опис)
# Створення та застосування міграцій

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Project Title")
    description = models.TextField( verbose_name="Project Description")
    technology = models.TextField(max_length=200, verbose_name="Project Technology")
    date = models.DateField(auto_now_add=True, verbose_name="Project Date")
    image = models.ImageField( upload_to="images/", verbose_name="Project Image")
    github = models.URLField(blank=True, null=True, verbose_name="Project Github")


    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title




class Skill(models.Model):
    title = models.CharField(max_length=200, verbose_name="Project Title")
    level = models.CharField( max_length=200, verbose_name="level users")
    category = models.CharField( max_length=200, verbose_name="Skill Category")

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=200, verbose_name="Role")
    company = models.CharField( max_length=200, verbose_name="Company")
    period = models.CharField( max_length=200, verbose_name="Period")
    description = models.TextField(verbose_name="Project Description")

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return self.title



