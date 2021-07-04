class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def pathExists(root: TreeNode, pathNumber: int, treeHeight: int) -> bool:
            current = root
            for level in range(0, treeHeight - 1):
                current = current.left if (pathNumber & (1 << (treeHeight - 2 - level))) == 0 else current.right
                if not current:
                    return False
            return True
            
        if not root:
            return 0
        
        count = 0;
        
        # Node count without last level
        hcurrent = root.left
        levelCount = 1
        height = 1
        while hcurrent:
            height += 1
            count += levelCount
            levelCount *= 2
            hcurrent = hcurrent.left
        
        # Find node count in the last level using binary search
        # encode last level node number:
        # going from the root to node and adding bits: 0bit - on going left, 1bit - on going right,
        # so first node bits is 0...0 (left) and last node bits is 1...1 (right)  
        left = 0
        right = levelCount - 1
        
        if pathExists(root, right, height):
            return count + right + 1
        
        while True:
            mid = (left + right) // 2
            if pathExists(root, mid, height):
                left = mid
            else:
                right = mid
            if right - left <= 1:
                break

        return count + left + 1
