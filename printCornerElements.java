
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

class TreeNode {
    public int data = 0;
    public TreeNode left = null;
    public TreeNode right = null;

    public TreeNode(int data) {
        this.data = data;
    }
}

public class printCornerElements {
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

    public static void main(String[] args) {
        int[] data = { 7,6,5,4,3,2,1};
        TreeNode root = construct(data);
        inorder(root);
        // List<Integer> res = printCornerNodeAtEachLevel(root);
        // System.out.println(res);
        TreeMap<Integer, Set<Integer>> map = new TreeMap<>();
        populateLevels(root, map, 0);
        System.out.println(map);
    }

    private static void populateLevels(TreeNode root, TreeMap<Integer, Set<Integer>> map, int lvl){
        if(root == null){
            return;
        }

        if(map.containsKey(lvl)){
            map.get(lvl).add(root.data);
        }else{
            Set<Integer> sortedSet = new TreeSet<>();
            sortedSet.add(root.data);
            map.put(lvl, sortedSet);
        }
        populateLevels(root.left, map, lvl+1);
        populateLevels(root.right, map, lvl+1);
    }

    private static List<Integer> printCornerNodeAtEachLevel(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        ArrayList<Integer> res = new ArrayList<>();
        int d = -1000;
        q.add(root);
        q.add(new TreeNode(d));
        // res.add(root.data);
        TreeNode lvlStart = null;
        TreeNode lvlEnd = null;
        while (q.size() > 1) {
            TreeNode n = q.poll();
            if (n != null) {
                if (n.data == d) {
                    q.add(n);
                    if (lvlStart != null) {
                        res.add(lvlStart.data);
                    }
                    if (lvlEnd != null && lvlEnd != lvlStart) {
                        res.add(lvlEnd.data);
                    }
                    lvlEnd = lvlStart = null;
                } else {
                    if (lvlStart == null) {
                        lvlStart = n;
                    } else {
                        lvlEnd = n;
                    }
                    if (n.left != null) {
                        q.add(n.left);
                    }
                    if (n.right != null) {
                        q.add(n.right);
                    }
                }
            }
        }
        res.add(lvlStart.data);
        res.add(lvlEnd.data);
        return res;
    }

}
