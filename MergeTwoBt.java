import java.util.LinkedList;
import java.util.Queue;

class Node{
    int data;
    Node left,right;

    public Node(int data){
        this.data = data;
    }
}

public class MergeTwoBt {
    public static boolean isLeaf(Node root){
        return root != null && root.left == null && root.right == null;
    }

    public static void print(int data) {
        System.out.print(data + " ");
    }

    public static void inorder(Node node) {
        if (node == null) {
            return;
        }
        inorder(node.left);
        print(node.data);
        inorder(node.right);
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
    
    public static int findSumSubTrees(Node root, int[] cnt, int X){
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

    public static Node merge(Node a, Node b){
        if(a == null){
            return b;
        }

        if(b == null){
            return a;
        }

        a.data += b.data;

        a.left = merge(a.left, b.left);
        a.right = merge(a.right,b.right);

        return a;
    }

    public static void main(String[] args) {
        int[] data1= {2,1,4,5};
        int[] data2= {3,6,1,-1,2,-1,7};

        Node root1 = construct(data1);
        
        Node root2 = construct(data2);

        inorder(root1);
        System.out.println();
        
        inorder(root2);
        System.out.println();

        root1 = merge(root1,root2);

        inorder(root1);
        System.out.println();
        
    }

}
