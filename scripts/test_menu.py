import maya.cmds as cmds
import reloadable_menu; reload(reloadable_menu)

@reloadable_menu.reloadable_menu('test_menu')
def test_menu():
    print 'test1'
    cmds.menuItem(label='Character',tearOff=True,subMenu=True)
    cmds.menuItem(label='blendShapeI/O', command='import pegasus_blendshapeio; pegasus_blendshapeio.main()')
    cmds.menuItem(label='blendShapeI/O', command='import pegasus_blendshapeio; pegasus_blendshapeio.main()')
    cmds.menuItem(label='test', command='import pegasus_blendshapeio; pegasus_blendshapeio.main()')
    cmds.menuItem(label='b', command='import pegasus_blendshapeio; pegasus_blendshapeio.main()')
    cmds.setParent('..', menu=True)

@reloadable_menu.reloadable_menu('test_menu2')
def test_menu2():
    print 'test2'
    cmds.menuItem(label='Character',tearOff=True,subMenu=True)
    cmds.menuItem(label='blendShapeI/O', command='import pegasus_blendshapeio; pegasus_blendshapeio.main()')
    cmds.menuItem(label='blendShapeI/O', command='import pegasus_blendshapeio; pegasus_blendshapeio.main()')
    cmds.menuItem(label='test', command='import pegasus_blendshapeio; pegasus_blendshapeio.main()')
    cmds.menuItem(label='b', command='import pegasus_blendshapeio; pegasus_blendshapeio.main()')
    cmds.setParent('..', menu=True)

def show():
    test_menu()
    test_menu2()
