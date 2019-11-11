# coding:utf-8
from __future__ import unicode_literals
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

if __name__ == "__main__":
    from xyscripts.base import ScriptShell
    s = ScriptShell()
    s.execute()


