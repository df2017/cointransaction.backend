from django.db import models
from django.contrib import admin



class Block(models.Model):
    index = models.IntegerField()
    hash_block =models.CharField(max_length=500)
    previous_hash= models.CharField(max_length=500, blank=True)
    tx_count = models.IntegerField() 
    timestamp= models.DateTimeField(auto_now_add=True)
    proof= models.IntegerField(), 
    difficulty= models.IntegerField()

    def __str__(self):
        return self.hash_block

    class Meta:
        get_latest_by = "-index"

class BlockAdmin(admin.ModelAdmin):
    list_display = ('hash_block', 'index', 'previous_hash', 'tx_count', 'timestamp')