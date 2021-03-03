#encoding: utf-8

import maya.cmds as cmds
import maya.cmds as cmds
import reloadable_menu

def show_message(message):
    print(message)
    cmds.inViewMessage(assistMessage=message,
                        position='midCenter',
                        fade=True,
                        # fadeStayTime=3000,
                        )

@reloadable_menu.reloadable_menu('Test Commands')
def create_menu_():
    # cmds.setParent('MayaWindow')
    # cmds.menu(label='Test Commands', tearOff=True)
    cmds.menuItem(l='Test Command 1', command='import test_commands_menu; test_commands_menu.show_message("Test Command 1")')
    cmds.menuItem(l='Test Command 2', command='import test_commands_menu; test_commands_menu.show_message("Test Command 2")')

