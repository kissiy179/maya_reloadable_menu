# -*- coding: utf-8 -*-
import importlib
import functools
import json
import maya.cmds as cmds
import maya.utils

self_module_name = __name__

reload_code = '''
import {0}; reload({0});
{0}.reload_menu('{1}', '{2}')
'''
def reloadable_menu(menu_name='testMenu'):
    '''
    再読み込み可能なメニューを作成するデコレータ
    メニュールートと、最下部にリロードアイテムを作成する
    menu_nameでメニュールートの名前を指定する
    '''

    def actual_decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # メニュールート作成
            create_menuroot(menu_name)

            # メニュー本体作成関数の実行
            rtn = func(*args, **kwargs)

            # リロードボタン追加
            add_reload_menuitem(module_name=func.__module__, func_name=func.__name__)
            return rtn

        return wrapper

    return actual_decorator

def create_menuroot(menu_name, label=None, parent='MayaWindow', tear_off=True):
    '''
    メニュールートを作成
    すでにある場合は一度削除してから作成
    '''
    label = label if label else menu_name

    try:
        cmds.deleteUI(menu_name)

    except:
        pass

    cmds.menu(menu_name, label=label, parent=parent, tearOff=tear_off)

def add_reload_menuitem(module_name, func_name, label='reload'):
    '''
    リロード用メニューアイテムを追加
    '''
    cmds.menuItem(divider=True)
    cmd = reload_code.format(self_module_name, module_name, func_name)
    cmds.menuItem(label=label, command=cmd)

def reload_menu(module_name, func_name):
    '''
    メニューをリロード
    モジュール、関数名を指定してメニュー作成関数を再実行する
    メニュー作成関数には reloadable_menu デコレータを使用すること
    menuItemのcmd引数から実行できるようにするため、モジュール、関数は文字列で受け取る
    '''

    # メニュー登録関数の親モジュールをリロード
    module = importlib.import_module(module_name)

    if not module:
        return

    reload(module)

    # メニュー登録関数を実行
    func = module.__dict__.get(func_name)
    maya.utils.executeDeferred(func)

