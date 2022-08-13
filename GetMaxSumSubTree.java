import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

class Node{
    int data = 0;
    Node left, right;

    public Node(int data){
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

public class GetMaxSumSubTree{

    public static void print(int data) {
        System.out.print(data + " ");
    }

    public static Node construct(int[] data) {
        Queue<Node> q = new LinkedList<>();
        Queue<Integer> qData = new LinkedList<>();
        for (int i : data) {
            qData.add(i);
        }
        Node root = new Node(qData.poll());
        q.add(root);
        while (!q.isEmpty()) {
            Node n = q.poll();
            if (n.left == null && !qData.isEmpty()) {
                if (qData.peek() == -1) {
                    qData.poll();
                } else {
                    n.left = new Node(qData.poll());
                    q.add(n.left);
                }
            }
            if (n.right == null && !qData.isEmpty()) {
                if (qData.peek() == -1) {
                    qData.poll();
                } else {
                    n.right = new Node(qData.poll());
                    q.add(n.right);
                }
            }
        }

        return root;
    }

    public static void inorder(Node node) {
        if (node == null) {
            return;
        }
        inorder(node.left);
        print(node.data);
        inorder(node.right);
    }

    public static int getTreeSum(Node root, int[] max){
        if(root == null){
            return 0;
        }

        int currSum = root.data + getTreeSum(root.left, max) + getTreeSum(root.right, max);

        if(max[0] < currSum){
            max[0] = currSum;
        }
        return currSum;
    }

    

    public static int getTreeSum(Node root, Integer max){
        if(root == null){
            return 0;
        }

        int currSum = root.data + getTreeSum(root.left, max) + getTreeSum(root.right, max);

        if(max < currSum){
            max = currSum;
        }
        return currSum;
    }

    public static void main(String[] args) {
        int[] data = {1,2,3,4,5,6,7};
        Node root = construct(data);
        inorder(root);
        System.out.println();
        int[] max = new int[1];
        Integer i = Integer.valueOf(0);
        getTreeSum(root, i);
        System.out.println(i);
    }
} 

