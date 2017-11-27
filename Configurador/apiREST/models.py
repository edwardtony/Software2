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
    presentation = models.CharField(max_length=70)
    description = models.CharField(max_length=50)

    def as_dict(self):
        result = dict(
            name = self.name,
            course = self.course,
            question = [question.as_dict() for question in self.question_set.all()],
            image = self.image,
            presentation = self.presentation,
            description = self.description
        )
        return result

    def __str__(self):
        return "{name} {course}".format(name = self.name, course = self.course)

class Question(models.Model):
    description = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def as_dict(self):
        result = dict(
            description = self.description,
            alternative = [alternative.as_dict() for alternative in self.alternative_set.all()]
        )
        return result

    def __str__(self):
        return "{description} {teacher}".format(description = self.description, teacher = self.teacher)

class Alternative(models.Model):
    description = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_true = models.BooleanField(default=False)

    def as_dict(self):
        result = dict(
            description = self.description,
			is_true = self.is_true
        )
        return result

    def __str__(self):
        return "{description} {question}".format(description = self.description, question = self.question)

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
    order = models.IntegerField(default=1)

    def as_dict(self):
        result = dict(
            name = self.name,
            image = self.image,
            dificulty = self.dificulty,
            teacher = self.teacher.as_dict(),
            quantity_question = self.quantity_question,
            time_question = self.time_question
        )
        return result

    def __str__(self):
        return "{name} {pk}".format(name = self.name, pk = self.pk)


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

    def as_dict(self):
        result = dict(
            duration = self.duration,
			image = self.image
        )
        return result

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

    def as_dict(self):
        result = dict(
            name = self.name,
            velocity = self.velocity.quantity,
            resistance = self.resistance.quantity,
            jump = self.jump.distance,
            health = self.health.quantity,
			super_mode = self.super_mode.as_dict(),
			damage_level = self.damage_level.quantity,
			photo_normal = self.photo_normal,
			photo_super = self.photo_super,
			photo_ultra = self.photo_ultra
        )
        return result

    def __str__(self):
        return "{name}".format(name = self.name)

class Player(models.Model):
    name = models.CharField(max_length=40)
    initial_year = models.CharField(max_length=10, default="2017-01")
    finish_year = models.CharField(max_length=10, default="2017-01")
    score = models.IntegerField(default=0)
    character = models.ForeignKey(Character)

    def as_dict(self):
        result = dict(
            name = self.name,
            initial_year = self.initial_year,
            finish_year = self.finish_year,
            score = self.score,
            character = self.character.as_dict()
        )
        return result

    def __str__(self):
        return "{name} {score} {character}".format(name = self.name, score = self.score, character = self.character)

# ---------------------------------- EXTRA ----------------------------------
class Message(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    scenario = models.IntegerField(default=0)
    position = models.IntegerField(default=0)

    def as_dict(self):
        result = dict(
            name = self.name,
            description = self.description,
            scenario = self.scenario,
            position = self.position,
        )
        return result

    def __str__(self):
        return "{name} {description} {scenario} {position}".format(name = self.name,
                                                                   description = self.description,
                                                                   scenario = self.scenario,
                                                                   position = self.position)
