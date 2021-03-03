#encoding: utf-8
import maya.utils
import maya.cmds as cmds
import test_commands_menu

# メニュー作成
maya.utils.executeDeferred(test_commands_menu.create_menu)
