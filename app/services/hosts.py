#!/usr/local/env python
# -*- coding: utf-8 -*-

from . import Base
from app.models import Host

class HostService(Base):
    __model__ = Host

hosts = HostService()