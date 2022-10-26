from django.db import models


class Staff(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="ФИО")
    position = models.CharField(max_length=50, null=True, blank=True, verbose_name="Должность")
    employment_date = models.DateField(null=True, verbose_name="Дата приема на работу")
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name="Размер заработной платы")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.SET_NULL)

    def __str__(self):
        return self.full_name

    def as_tree(self):
        children = list(self.children.all())
        branch = bool(children)
        yield branch, self
        for child in children:
            for next in child.as_tree():
                yield next
        yield branch, None

    class Meta:
        verbose_name_plural = "Сотрудники"
