# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import os
# Create your models here.

# ---------------------------------- STAGE ----------------------------------

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=30)
    image = models.CharField(max_length=200)

class Question(models.Model):
    description = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

class Alternative(models.Model):
    description = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Stage(models.Model):
    STATUS_CHOICES = (
        ('EASY','FÁCIL'),
        ('MEDIUM','MEDIO'),
        ('HARD','DIFÍCIL'),
    )
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=200)
    dificulty = models.CharField(max_length=10, choices=STATUS_CHOICES, default='EASY')
    teacher = models.ForeignKey(Teacher,on_delete = models.CASCADE)
    quantity_question = models.IntegerField(default=1)
    time_question = models.IntegerField(default=30)

class StageConfiguration(models.Model):
    stage = models.ForeignKey(Stage, on_delete= models.CASCADE)

# ---------------------------------- CHARACTER ----------------------------------

class Velocity(models.Model):
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "{quantity} ".format(quantity = self.quantity)

class Resistance(models.Model):
    quantity = models.IntegerField(default=3)

    def __str__(self):
        return "{quantity} ".format(quantity = self.quantity)

class Jump(models.Model):
    distance = models.IntegerField(default=1)

    def __str__(self):
        return "{distance} ".format(distance = self.distance)

class Health(models.Model):
    quantity = models.IntegerField(default=3)

    def __str__(self):
        return "{quantity} ".format(quantity = self.quantity)

class SuperMode(models.Model):
    duration = models.IntegerField(default=30)
    image = models.CharField(max_length=200)

    def __str__(self):
        return "{duration} ".format(duration = self.duration)

class DamageLevel(models.Model):
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "{quantity} ".format(quantity = self.quantity)

class Character(models.Model):
    name = models.CharField(max_length=30)
    velocity = models.ForeignKey(Velocity, on_delete=models.CASCADE)
    resistance = models.ForeignKey(Resistance, on_delete=models.CASCADE)
    jump = models.ForeignKey(Jump, on_delete=models.CASCADE)
    health = models.ForeignKey(Health, on_delete=models.CASCADE)
    super_mode = models.ForeignKey(SuperMode, on_delete=models.CASCADE)
    damage_level = models.ForeignKey(DamageLevel, on_delete=models.CASCADE)
    photo_normal = models.CharField(max_length=200)
    photo_super = models.CharField(max_length=200)
    photo_ultra = models.CharField(max_length=200)

    def __str__(self):
        return "{name} {super_mode}".format(name = self.name, super_mode = self.super_mode)

class Player(models.Model):
    character = models.ForeignKey(Character)
    name = models.CharField(max_length=40)
    entrant = models.CharField(max_length=10)
    graduate = models.CharField(max_length=10)
    score = models.IntegerField(default=0)

    def __str__(self):
        return "{character} {name} {score}".format(character = self.character, name = self.name, score = self.score)
