import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.Map.Entry;

class TreeNode {
    public int data = 0;
    public TreeNode left = null;
    public TreeNode right = null;

    public TreeNode(int data) {
        this.data = data;
    }
}

class Pair{
    int first = 0;
    int second = 0;

    public Pair(int a, int b){
        this.first = a;
        this.second = b;
    }
}

public class PrintTree2d {
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

    static int COUNT = 10;

    public static void main(String[] args) {
        int[] data = {1,2,3,4,5,6,7};
        TreeNode root = construct(data);
        inorder(root);
        print2D(root, 0);
        List<Integer> leftView = new ArrayList<>();
        leftView(root, leftView,1);
        
        List<Integer> rightView = new ArrayList<>();
        rightView(root, rightView,1);

        TreeMap<Integer, Pair> topView = new TreeMap<>();
        topView(root,topView,0,0);
        System.out.println("leftView: " + leftView);
        System.out.println("rightView: " + rightView);
        System.out.println("topView: " + topView);

        for(Entry<Integer, Pair> e: topView.entrySet()){
            System.out.print(e.getValue().first + " ");
        }   
    }

    
    private static void topView(TreeNode root, TreeMap<Integer,Pair> topView, int vLvl, int lvl) {
        if(root == null){
            return;
        }

        if(topView.containsKey(vLvl) && lvl < topView.get(vLvl).second){
            topView.put(vLvl, new Pair(root.data, lvl));
        }else if(topView.get(vLvl) == null){
            topView.put(vLvl, new Pair(root.data, lvl));
        }

        topView(root.left, topView, vLvl - 1,lvl + 1);
        
        topView(root.right, topView, vLvl + 1, lvl + 1);

    }

    private static void rightView(TreeNode root, List<Integer> rightView, int lvl) {
        if(root == null){
            return;
        }

        if(rightView.size() < lvl){
            rightView.add(root.data);
        }

        rightView(root.right,rightView,lvl+1);
        rightView(root.left,rightView,lvl+1);
    }

    private static void leftView(TreeNode root, List<Integer> leftView, int lvl) {
        if(root == null){
            return;
        }

        if(leftView.size() < lvl){
            leftView.add(root.data);
        }

        leftView(root.left,leftView,lvl+1);
        leftView(root.right,leftView,lvl+1);
    }

    private static void print2D(TreeNode root, int space) {
        if(root == null){
            return ;
        }


        space += COUNT;

        print2D(root.right, space);

        System.out.println();
        for(int i=COUNT; i<space;++i){
            System.out.print(" ");
        }
        System.out.println(root.data);

        print2D(root.left, space);
    }
}

