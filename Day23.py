    def levelOrder(self,root):
        #Write your code here
        d = [root]
        while any(d):
            print(*map(lambda n: n.data, d), sep=' ', end=' ')
            c = sum([[a.left, a.right] for a in d], [])
            d = list(filter(bool, c))
        