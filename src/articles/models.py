# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Article(models.Model):
    playerScript = models.TextField()
    file = models.TextField()
    playerId = models.TextField()

    def _str_(self):
        return self.file
