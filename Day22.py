    def getHeight(self,root):
        #Write your code here
        if root is None:
            return -1
        else:
            lDepth = self.getHeight(root.left)
            rDepth = self.getHeight(root.right)
            if(lDepth>rDepth):
                return lDepth+1
            else:
                return rDepth+1
       