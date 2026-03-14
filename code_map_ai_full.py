import ast
import os
import networkx as nx
import matplotlib.pyplot as plt

# Folder z projektami
FOLDER = os.path.dirname(os.path.abspath(__file__))

def extract_functions_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()
    tree = ast.parse(code)
    functions = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            calls = [e.func.id for e in ast.walk(node)
                     if isinstance(e, ast.Call) and hasattr(e.func, 'id')]
            functions[func_name] = calls
    return functions

# Zbieramy wszystkie pliki .py
all_functions = {}
for root, dirs, files in os.walk(FOLDER):
    for file in files:
        if file.endswith(".py") and file != "code_map_ai_full.py":
            path = os.path.join(root, file)
            funcs = extract_functions_from_file(path)
            for f, c in funcs.items():
                all_functions[f] = c

# Tworzymy graf
G = nx.DiGraph()
for func, calls in all_functions.items():
    G.add_node(func)
    for c in calls:
        G.add_edge(func, c)

# Rysujemy graf
plt.figure(figsize=(10,8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, arrowstyle='-|>', arrowsize=20)
plt.title("Full Code Map AI - Function Dependencies")
plt.show()
