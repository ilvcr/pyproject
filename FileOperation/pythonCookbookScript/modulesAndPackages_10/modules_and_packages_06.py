#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 03 May 2018 02:33:28 PM CST
# File Name: modules_and_packages_06.py
# Description:  自定义导入的方法是编写一个钩子直接嵌入到 sys.path 变量中去，识别某些目录命名模式
"""

#urlimport.py
#... include previous code above ...
# Path finder class for a URL

class UrlPathFinder(importlib.abc.PathEntryFinder):
    def __init__(self, baseurl):
        self._links = None
        self.loader = UrlModuleLoader(baseurl)
        self._baseurl = baseurl


    def find_loader(self, fullname):
        log.debug('find_loader: %r', fullname)
        parts = fullname.split('.')
        basename = parts[-1]
        #Check link cache
        if self._links is None:
            self._links = []  #See discussion
            self._links = _get_links(self._baseurl)

        #Check if it's a package
        if basename in self._links:
            log.debug('find_loader: trying package %r', fullname)
            fullurl = self._baseurl + '/' + basename
            #Attempt to load the package (which accesses __init__.py)
            loader = UrlPackageLoader(fullurl)

            try:
                loader.load_module(fullname)
                log.debug('find_loader: package %r loaded', fullname
            except ImportError as e:
                log.debug('find_loader: %r is a namespace package', fullname)

            return (loader, [fullurl])


        #A normal module
        filename = basename + '.py'
        if filename in self._links:
            log.debug('find_loader: module %r found', fullname)
            return (self.loader, [])
        else:
            log.debug('find_loader: module %r not found', fullname)
            return (None, [])



    def invalidate_caches(self):
        log.debug('invalidating link cache')
        self._links = None



#Check path to see if it looks like a URL
_url_path_cache = {}
def handle_url(path):
    if path.startseith(('http://', 'https://')):
        log.debug('Handle path? %s. [Yes]', path)
        if path in _url_path_cache:
            finder = _url_path_cache[path]
        else:
            finder = UrlPathFinder(path)
            _url_path_cache[path] = finder
        return finder
    else:
        log.debug('Handle path? %s. [No]', path)


def install_path_hook():
    sys.path_hooks.append(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Installing handle_url')


def remove_path_hok():
    sys,path_hooks.remove(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Removing handle_url')



