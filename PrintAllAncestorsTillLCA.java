
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Node{
    int data;
    Node left,right;

    public Node(int data){
        this.data = data;
    }
}

public class PrintAllAncestorsTillLCA {
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

    public static Node lca(Node root, int a, int b){
        
        if(root == null || root.data == a || root.data == b){
            return root;
        }

        Node left = lca(root.left, a, b);

        Node right = lca(root.right, a, b);

        if(left != null && right != null){
            return root;
        }

        return left != null ? left : right;

    }

    public static void distance(Node root, int a, int b){
        if(root == null){
            return;
        }
        Node lca = lca(root,a,b);
        List<String> res = new ArrayList<>();
        getAllAnc(root, lca, res, "");
        System.out.println(res);

    }

    private static void getAllAnc(Node root, Node lca, List<String> list, String path) {
        if(root == null){
            return;
        }

        path += root.data + " ";

        if(root == lca){
            list.addAll(List.of(path.split(" ")));
        }

        getAllAnc(root.left, lca, list, path);
        
        getAllAnc(root.right, lca, list, path);

    }

    public static void main(String[] args) {
        int[] data1= {1,2,3,4,5,6,7,8,9};

        Node root = construct(data1);
    
        // inorder(root);
        
        System.out.println();
        
        distance(root,2,3);
        
        distance(root,4,5);
        
        distance(root,5,9);

        distance(root,1,9);

        distance(root,1,99);
    }

}

