import java.util.LinkedList;
import java.util.Queue;

class Node{
    int data;
    Node left,right;

    public Node(int data){
        this.data = data;
    }
}

public class CountSubTreesHavingKSum {
    public static boolean isLeaf(TreeNode root){
        return root != null && root.left == null && root.right == null;
    }

    public static void print(int data) {
        System.out.print(data + " ");
    }

    public static void inorder(TreeNode node) {
        if (node == null) {
            return;
        }
        inorder(node.left);
        print(node.data);
        inorder(node.right);
    }

    public static TreeNode construct(int[] data) {
        Queue<TreeNode> q = new LinkedList<>();
        Queue<Integer> qData = new LinkedList<>();
        for (int i : data) {
            qData.add(i);
        }
        TreeNode root = new TreeNode(qData.poll());
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n.left == null && !qData.isEmpty()) {
                if (qData.peek() == -1) {
                    qData.poll();
                } else {
                    n.left = new TreeNode(qData.poll());
                    q.add(n.left);
                }
            }
            if (n.right == null && !qData.isEmpty()) {
                if (qData.peek() == -1) {
                    qData.poll();
                } else {
                    n.right = new TreeNode(qData.poll());
                    q.add(n.right);
                }
            }
        }
        return root;
    }
    
    public static int findSumSubTrees(TreeNode root, int[] cnt, int X){
        if(root == null){
            return 0;
        }    
        
        if(isLeaf(root) && root.data == X){
            cnt[0]++;
            return root.data;
        }
        
        int leftSum = findSumSubTrees(root.left,cnt,X);
        
        int rightSum = findSumSubTrees(root.right,cnt,X);
        
        int tot = leftSum + rightSum + root.data;
        
        if(tot == X){
            cnt[0]++;
        }
        return tot;
    }
    
    public static int countSubtreesWithSumX(TreeNode root, int X)
    {
        int[] cnt = new int[1];
        cnt[0] = 0;
        findSumSubTrees(root,cnt,X);
        return cnt[0];
    }
    
    public static void main(String[] args) {
        int[] data= {1,2,3,4,5,6,7};
        constructTree(data);
        int[] data1 = {5,-10,3,9,8,-4,7};
        constructTree(data1);
    }

    public static void constructTree(int[] data){
        TreeNode root = construct(data);

        inorder(root);

        System.out.println();

        System.out.println(countSubtreesWithSumX(root, 7));
    }
}
