#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os, re, sqlite3
from bs4 import BeautifulSoup, NavigableString, Tag

# example: /Users/teki/Library/Application Support/doc2dash/DocSets/djbook.docset/Contents/Resources/docSet.dsidx
docset_db = '/Users/teki/Library/Application Support/doc2dash/DocSets/djbook.docset/Contents/Resources/docSet.dsidx'

# example: /Users/teki/Library/Application Support/doc2dash/DocSets/djbook.docset/Contents/Resources/Documents
docpath = '/Users/teki/Library/Application Support/doc2dash/DocSets/djbook.docset/Contents/Resources/Documents'

db = sqlite3.connect(docset_db)
cur = db.cursor()

try: cur.execute('DROP TABLE searchIndex;')
except: pass
cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

page = open(os.path.join(docpath,'genindex.html')).read()
soup = BeautifulSoup(page)

any = re.compile('.*')
for tag in soup.find_all('a', {'href':any}):
    name = tag.text.strip()
    if len(name) > 1 and u"метод" in name:
        path = tag.attrs['href'].strip()
        if path.split('#')[0] not in ('index.html', 'py-modindex.html'):
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Method', path))
            print 'METHOD: name: %s, path: %s' % (name, path)
    if len(name) > 1 and u"класс" in name:
        path = tag.attrs['href'].strip()
        if path.split('#')[0] not in ('index.html', 'py-modindex.html'):
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Class', path))
            print 'CLASS: name: %s, path: %s' % (name, path)
    if len(name) > 1 and u"модуль" in name:
        path = tag.attrs['href'].strip()
        if path.split('#')[0] not in ('index.html', 'py-modindex.html'):
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Module', path))
            print 'MODULE: name: %s, path: %s' % (name, path)
    if len(name) > 1 and u"атрибут" in name:
        path = tag.attrs['href'].strip()
        if path.split('#')[0] not in ('index.html', 'py-modindex.html'):
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Attribute', path))
            print 'ATTRIBUTE: name: %s, path: %s' % (name, path)
    if len(name) > 1 and "setting" in name:
        path = tag.attrs['href'].strip()
        name = path.split("std:setting-")[-1]
        if path.split('#')[0] not in ('index.html', 'py-modindex.html'):
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Settings', path))
            print 'SETTINGS: name: %s, path: %s' % (name, path)
    if len(name) > 1 and u"встроенная функция" in name:
        path = tag.attrs['href'].strip()
        if path.split('#')[0] not in ('index.html', 'py-modindex.html'):
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'func', path))
            print 'FUNCTION: name: %s, path: %s' % (name, path)
    if len(name) > 1 and "django-admin command-line option" in name:
        path = tag.attrs['href'].strip()
        name = path.split("#django-admin-option-")[-1]
        if path.split('#')[0] not in ('index.html', 'py-modindex.html'):
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Options', path))
            print 'OPTIONS: name: %s, path: %s' % (name, path)
    if len(name) > 1 and "template tag" in name:
        path = tag.attrs['href'].strip()
        name = path.split("std:templatetag-")[-1]
        if path.split('#')[0] not in ('index.html', 'py-modindex.html'):
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Tags', path))
            print 'TAGS: name: %s, path: %s' % (name, path)
    if len(name) > 1 and "django-admin command" in name and "option" not in name:
        path = tag.attrs['href'].strip()
        name = path.split("#django-admin-")[-1]
        if path.split('#')[0] not in ('index.html', 'py-modindex.html'):
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Commands', path))
            print 'COMMANDS: name: %s, path: %s' % (name, path)

db.commit()
db.close()
