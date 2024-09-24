#import libclang
from clang import cindex

# Initialize the Clang index
cindex.Config.set_library_file("/Library/Developer/CommandLineTools/usr/lib/libclang.dylib")
index = cindex.Index.create()

# Parse the C++ source file
translation_unit = index.parse('example.cpp')

# Recursive function to traverse the AST and print details
def traverse_ast(node, level=0):
    indent = '  ' * level
    print(f"{indent}{node.kind} - {node.spelling or node.displayname}")

    # Check if the node is a function or class
    if node.kind == cindex.CursorKind.CLASS_DECL:
        print(f"{indent}Class: {node.spelling}")
    elif node.kind == cindex.CursorKind.FUNCTION_DECL:
        print(f"{indent}Function: {node.spelling}")
    elif node.kind == cindex.CursorKind.FOR_STMT:
        print(f"{indent}For Loop")
    elif node.kind == cindex.CursorKind.IF_STMT:
        print(f"{indent}If Condition")

    # Recursively traverse child nodes
    for child in node.get_children():
        traverse_ast(child, level + 1)

# Start traversing the AST from the root
traverse_ast(translation_unit.cursor)
