#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from Qt import QtWidgets
from NodeGraphQt import NodeGraph, BaseNode, BackdropNode, setup_context_menu

# create a example node object with a input/output port.
class MyNode(BaseNode):
    """example test node."""

    # unique node identifier domain. ("com.chantasticvfx.MyNode")
    __identifier__ = "com.chantasticvfx"

    # initial default node name.
    NODE_NAME = "My Node"

    def __init__(self):
        super(MyNode, self).__init__()
        self.add_input("foo", color=(180, 80, 0))
        self.add_output("bar")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # create the node graph controller.
    graph = NodeGraph()

    # set up default menu and commands.
    setup_context_menu(graph)

    # register backdrop node. (included in the NodeGraphQt module)
    graph.register_node(BackdropNode)

    # register example node into the node graph.
    graph.register_node(MyNode)

    # create nodes.
    node_a = graph.create_node("com.chantasticvfx.MyNode", name="Node A")
    node_b = graph.create_node(
        "com.chantasticvfx.MyNode", name="Node B", color="#5b162f"
    )
    backdrop = graph.create_node("nodeGraphQt.nodes.BackdropNode", name="Backdrop")

    # wrap "backdrop" node around "node_a" and "node_b"
    backdrop.wrap_nodes([node_a, node_b])

    # connect "node_a" input to "node_b" output.
    node_a.set_input(0, node_b.output(0))

    # auto layout nodes.
    graph.auto_layout_nodes()

    # show the node graph widget.
    graph_widget = graph.widget
    graph_widget.show()

    app.exec_()
