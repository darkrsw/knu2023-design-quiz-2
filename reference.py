from ast import NodeVisitor
import ast
import os
import json

from glob import glob

def getAST(path: str):
    with open(path, "r") as f:
        source = f.read()
    return ast.parse(source)

class ClassCollector(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.classes = {}

    def visit_ClassDef(self, node):
        self.classes[node.name] = node
        return super().generic_visit(node)

class MethodCollector(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.methods = {}

    def visit_function(self, node):
        self.methods[node.name] = node

    def visit_FunctionDef(self, node):
        self.visit_function(node)
        return super().generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.visit_function(node)
        return super().generic_visit(node)

class SelfInvocationCollector(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.selfcalls = []

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "self":
                self.selfcalls.append(node.func.attr)


def collect_uninvoked_methods(path):
    pyfiles = list(glob(path+"/**/*.py", recursive=True))

    classcollector = ClassCollector()

    uninvokedmap = {}

    # collect classes
    for pyfile in pyfiles:
        myast = getAST(pyfile)
        classcollector.visit(myast)

    # collect methods for class
    for cname, cnode in classcollector.classes.items():
        mcollector = MethodCollector()
        mcollector.visit(cnode)
        # for each method
        callcollector = SelfInvocationCollector()
        uninvoked = []
        for mname, mnode in mcollector.methods.items():
            callcollector.visit(mnode)

        for mname, mnode in mcollector.methods.items():
            if mname not in callcollector.selfcalls:
                uninvoked.append(mname)

        uninvokedmap[cname] = set(uninvoked)

    return uninvokedmap
