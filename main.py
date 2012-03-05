#!/usr/bin/python

from jinja2 import Environment, FileSystemLoader
import os
from os import path

path.sep = '/'

q_root = r"." 

templates_dirs = [os.path.join(q_root, "templates/queries"), os.path.join(q_root, "templates/common")]
path2templates = os.path.join(q_root,"templates/queries")
path2result = q_root


env = Environment(loader = FileSystemLoader( templates_dirs ))

def render(tmpl):

  print tmpl[2]
  template = env.get_template( tmpl[1] )
  res = template.render()  

  open(tmpl[0], 'w' ).write( res )

def get_templates(tmpl_path):

  for path, _, filelist in os.walk(tmpl_path):
    for name in filelist:

      report = os.path.split(path)[1]
      yield [report, os.path.join(report,name), name]


def mkdir(where, templates):

  if not hasattr( mkdir, '_deleted' ):
      mkdir._deleted = []

  for tmpl in templates:

    import shutil
    path = os.path.join(where, tmpl[0])

    if path not in mkdir._deleted:        
        shutil.rmtree(path, ignore_errors=True)
        os.makedirs( path )
        mkdir._deleted.append( path )            

    tmpl[0] = os.path.join( path, tmpl[2] )

    yield tmpl


templates =  get_templates(path2templates)
for x in mkdir(path2result, templates): render(x)
    
    
