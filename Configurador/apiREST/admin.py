# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from apiREST.models import *

# Register your models here.

# ---------------------------------- STAGE ----------------------------------

admin.site.register(Teacher)
admin.site.register(Question)
admin.site.register(Alternative)
admin.site.register(Stage)
admin.site.register(StageConfiguration)

# ---------------------------------- CHARACTER ----------------------------------   


admin.site.register(Velocity)
admin.site.register(Resistance)
admin.site.register(Jump)
admin.site.register(Health)
admin.site.register(SuperMode)
admin.site.register(DamageLevel)
admin.site.register(Character)
admin.site.register(Player)