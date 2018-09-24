from django.db import models

class Human(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Todo(models.Model):
    text=models.CharField(max_length =100)
    created=models.DateTimeField()
    dueon=models.DateTimeField()
    owner=models.ForeignKey(Human,on_delete=models.CASCADE)
    mark=models.BooleanField(default=False)

    def __str__(self):
        return "{1},{2},{3},{4},{5}".format(self.text,self.created,self.dueon,self.owner,self.mark)

