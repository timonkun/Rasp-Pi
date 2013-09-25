#!/usr/bin/env python
# -*- coding: utf-8 -*-

gbkStr = '@K_K鲲'
print type(gbkStr)
print gbkStr

#unicodeStr = gbkStr.decode('utf-8')
utext = unicode(gbkStr, "utf-8")
print type(utext)
print utext
