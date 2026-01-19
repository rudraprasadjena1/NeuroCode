#parser\python_parser.py
import ast

class CallVisitor(ast.NodeVisitor):
    def __init__(self):
        self.calls = []

    def visit_Call(self, node):
        name = self._get_call_name(node.func)
        if name:
            self.calls.append(name)
        self.generic_visit(node)

    def _get_call_name(self, node):
        if isinstance(node, ast.Name):
            return node.id

        if isinstance(node, ast.Attribute):
            parts = []
            while isinstance(node, ast.Attribute):
                parts.append(node.attr)
                node = node.value
            if isinstance(node, ast.Name):
                parts.append(node.id)
                return ".".join(reversed(parts))

        return None


def parse_python_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    functions = []
    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        elif isinstance(node, ast.Import):
            for n in node.names:
                imports.append(n.name)

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)

    visitor = CallVisitor()
    visitor.visit(tree)

    return functions, imports, visitor.calls
