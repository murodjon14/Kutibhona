from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=50)
    kurs = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"

        unique_together = ('ism', 'guruh', 'kurs')

    def __str__(self):
        return self.ism


class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=10, choices=[
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    ])
    t_sana = models.DateField()
    kitob_soni = models.PositiveSmallIntegerField()
    tirik = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=50)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return self.nom


class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=255)
    ish_vaqti = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Kutubxonachi"
        verbose_name_plural = "Kutubxonachilar"

    def __str__(self):
        return self.ism


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)
    olgan_sana = models.DateField(auto_now_add=True)
    qaytarish_sana = models.DateField(null=True, blank=True)
    qaytardi = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Rekord"
        verbose_name_plural = "Rekordlar"

    def __str__(self):
        return f"{self.talaba.ism}: {self.kitob}"

class Student(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.IntegerField()
        