import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def preorder(node):
    if node == '.':
        return
    else:
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])
        return


def inorder(node):
    if node == '.':
        return
    else:
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])
        return


def postorder(node):
    if node == '.':
        return
    else:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')
        return


N = int(input())
tree = dict()

for i in range(N):
    node, l, r = input().split()
    tree[node] = [l, r]

preorder('A')
print()
inorder('A')
print()
postorder('A')
