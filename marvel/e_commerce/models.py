from django.contrib.auth.models import User
from django.db import models

# NOTE: Para poder utilizar el modelo "user" que viene por defecto en Django,
# Debemos importarlo previamente:
# from django.contrib.auth.models import User    


# Create your models here.
class Comic(models.Model):
    '''
    Esta clase hereda de Django models.Model y crea una tabla llamada
    e_commerce_comic. Las columnas toman el nombre especificado de cada objeto.
    '''
    id = models.BigAutoField(db_column='ID', primary_key=True)
    marvel_id = models.PositiveIntegerField(
        verbose_name='marvel id', null=False, blank=False, unique=True
    )
    title = models.CharField(
        verbose_name='Título', max_length=120, default=''
    )
    description = models.TextField(verbose_name='description', default='')
    price = models.FloatField(
        verbose_name='Precio', max_length=5, default=0.00
    )
    stock_qty = models.PositiveIntegerField(
        verbose_name='Cantidad de stock', default=0
    )
    picture = models.URLField(verbose_name='Imagen', default='')

    class Meta:
        '''
        Con "class Meta" podemos definir atributos de nuestras entidades como el nombre de la tabla.
        '''
        db_table = 'e_commerce_comics'
        verbose_name = 'comic'
        verbose_name_plural = 'comics'

    def __str__(self):
        '''
        El método __str__ cumple una función parecida a __repr__ en SQL Alchemy, 
        es lo que retorna cuando llamamos al objeto.
        '''
        return f'{self.title} - {self.id}'

class WishList(models.Model):

    #* id
    id = models.BigAutoField (primary_key=True)
    #* user (Este campo debe ser un Foreign Key relacionando con el modelo **User** que ofrece Django).
    user = models.ForeignKey (
        User, verbose_name='Usuario', on_delete=models.CASCADE, null=False, blank=False, unique=True
    )
    #* comic (Este campo debe ser un Foreign Key relacionando con el Modelo **Comic**).
    comic = models.ForeignKey (
        Comic, verbose_name='Comic', on_delete=models.CASCADE, null=False, blank=False, unique=True
    )
    #* favorite
    favorite = models.BooleanField(
        verbose_name='Tiene favoritos?', null=False, blank=True
    )
    #* cart
    cart = models.BooleanField(
        verbose_name='Está en el carrito?', null=False, blank=True
    )
    #* wished_qty
    wished_qty = models.PositiveIntegerField(
        verbose_name='Cantidad de deseados', null=False, blank=False
    )
    #* bought_qty 
    bought_qty = models.PositiveIntegerField(
        verbose_name='Cantidad de adquiridos', null=False, blank=False
    )

    class Meta:
        db_table = 'e_commerce_wish_list'
        verbose_name = 'wish_list'
        verbose_name_plural = 'wish_lists'

    def __str__(self):
        
        return f'{self.id} - {self.user} - {self.wished_qty}'