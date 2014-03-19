from django.db import models

# Create your models here.

POSICIONES = (
    ('arquero','Arquero'),
    ('defensa','Defensa'),
    ('volante','Volante'),
    ('delantero','Delantero'),
)

class Continente(models.Model):
    nombreContinente = models.CharField(max_length=50)
    def __unicode__(self):
        return unicode(self.nombreContinente)
 
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    continente = models.ForeignKey(Continente)
    tecnico = models.CharField(max_length=60)
    def __unicode__(self):
        return unicode(self.nombre)

class Jugador(models.Model):
    nombreJugador = models.CharField(max_length=50)
    posicion = models.CharField(max_length=20)
    equipo = models.ForeignKey(Equipo)
    estatura = models.FloatField()
    pieHabil = models.CharField(max_length=20)
    tarjetaAmarilla = models.IntegerField()
    tarjetaRoja = models.IntegerField()
    lesionado = models.BooleanField()
    titular = models.BooleanField()
    goles = models.IntegerField()
    #foto = models.ImageField()
    def __unicode__(self):
        return unicode(self.nombreJugador)















