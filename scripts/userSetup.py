#encoding: utf-8
import maya.utils
import maya.cmds as cmds
import reloadable_menu

def show_message(message):
    print(message)
    cmds.inViewMessage(assistMessage=message,
                        position='midCenter',
                        fade=True,
                        # fadeStayTime=3000,
                        )


# メニュー定義
@reloadable_menu.reloadable_menu('test commands')
def create_menu_():
    # cmds.setParent('MayaWindow')
    # cmds.menu(label='test commands', tearOff=True)
    cmds.menuItem(l='test command 1', command='show_message("test command 1")')
    cmds.menuItem(l='test command 2', command='show_message("test command 2")')

# メニュー作成
maya.utils.executeDeferred(create_menu_)

print create_menu_.__module__, '---'