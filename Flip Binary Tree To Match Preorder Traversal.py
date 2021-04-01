
class Solution:
    def flipMatchVoyage(self, root, voyage):
        res = []
        self.ind = 0

        def do_rec(node):
            
            if not node or self.ind == len(voyage): 
                return
            if node.val != voyage[self.ind]:
                res.append(None)
                return
            dir = 1
            self.ind += 1
            
            if node.left and node.left.val != voyage[self.ind]:
                res.append(node.val)
                dir = -1
                
            for child in [node.left, node.right][::dir]:
                do_rec(child)
                
        do_rec(root)
        return [-1] if None in res else res
