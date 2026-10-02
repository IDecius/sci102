#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: Robin Lebon
# Description: SCI102 Labo2 A2026
#
# Copyright (c) 2026 Robin Lebon
# All rights reserved. No warranty, explicit or implicit, provided.

from datetime import date

def age(annee):
    _age_ = date.today().year - annee
    return _age_

def salutations(_nom_):
    return "Bonjour " + _nom_ + "."