from setuptools import setup
import py2exe, sys, os

modulos = [sys.argv[1]]
sys.argv[1] = "py2exe"

opcoes = {}
opcoes['py2exe'] = {}
opcoes['py2exe']['excludes'] = \
    ["pywin", "pywin.debugger", "pywin.debugger.dbgcon", "pywin.dialoga", "pywin.dialoga.list"]
opcoes['py2exe']['packages'] = ["encodings", "webview", "screeninfo"]
descricao = "Custom webbrowser to access a specific page"
versao = '1.0'
name = "econnect"

setup(
    name=name,
    console=modulos,
    zipfile="lib/shared.zip",
    description=descricao,
    version='1.0'
)
