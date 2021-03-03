import maya.cmds as cmds
import reloadable_menu; reload(reloadable_menu)

@reloadable_menu.reloadable_menu('test_menu1')
def test_menu():
    print 'test1'
    # cmds.menuItem(label='Character',tearOff=True,subMenu=True)
    cmds.menuItem(label='test1_1', command='print("exec_test1-1")')
    cmds.menuItem(label='test1_2', command='print("exec_test1-2")')
    # cmds.setParent('..', menu=True)

@reloadable_menu.reloadable_menu('test_menu2')
def test_menu2():
    print 'test2'
    cmds.menuItem(label='parent_menu',tearOff=True,subMenu=True)
    cmds.menuItem(label='test2_1', command='print("exec_test2-1")')
    cmds.menuItem(label='test2_2', command='print("exec_test2-2")')
    cmds.setParent('..', menu=True)

def show():
    test_menu()
    test_menu2()
