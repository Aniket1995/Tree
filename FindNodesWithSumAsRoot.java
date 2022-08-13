import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

public class FindNodesWithSumAsRoot {

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

    public static void printNodesWithSumAsRoot(TreeNode root, HashSet<Integer> map, int rootData){
        if(root == null){
            return;
        }

        if(map.contains(Math.abs(root.data - rootData))){
            System.out.println(root.data +","+Math.abs(root.data - rootData));
        }else{
            map.add(root.data);
        }
        printNodesWithSumAsRoot(root.left, map, rootData);
        printNodesWithSumAsRoot(root.right, map, rootData);
        map.remove(root.data);
    }

    public static void main(String[] args) {
        int[] data = {7,6,5,1,2,2,3};
        TreeNode root = construct(data);
        inorder(root);
        System.out.println();
        printNodesWithSumAsRoot(root, new HashSet<Integer>(), root.data);
    }
}
