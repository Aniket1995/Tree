import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode{
    public int data = 0;
    public TreeNode left = null;
    public TreeNode right = null;

    public TreeNode(int data){
        this.data = data;
    }
}

public class PrintNodeAtKDistFromLeaf {

    public static void print(int data){
        System.out.print(data + " ");
    }

    public static void inorder(TreeNode node){
        if(node == null){
            return ;
        }
        inorder(node.left);
        print(node.data);
        inorder(node.right);
    }
    public static TreeNode construct(int[] data){
        Queue<TreeNode> q = new LinkedList<>();
        Queue<Integer> qData = new LinkedList<>();
        for(int i : data){
            qData.add(i);
        }
        TreeNode root = new TreeNode(qData.poll());
        q.add(root);
        while(!q.isEmpty()){
            TreeNode n = q.poll();
            if(n.left == null && !qData.isEmpty()){
                if(qData.peek() == -1){
                    qData.poll();
                }else{
                    n.left = new TreeNode(qData.poll());
                    q.add(n.left);
                }
            }
            if(n.right == null && !qData.isEmpty()){
                if(qData.peek() == -1){
                    qData.poll();
                }else{
                    n.right = new TreeNode(qData.poll());
                    q.add(n.right);
                }
            }
        }

        return root;
    }

    public static int height(TreeNode root){
        if(root == null){
            return 0;
        }

        int lh = height(root.left) + 1;
        int rh = height(root.right) + 1;

        return lh > rh ? lh : rh;

    }

    public static void leafPaths(TreeNode root,String s){
        if(root == null){
            return ;
        }
        s += root.data + " ";
        if(root.left == null  && root.right == null){
            System.out.println(s);
        }
        leafPaths(root.left, s);
        leafPaths(root.right, s);
    }

    public static void printNodesAtKDistance(TreeNode root, int k, int pathLen, int[] path, boolean[] visited, int[] counter){
        if(root == null){
            return ;
        }
        path[pathLen] = root.data;
        visited[pathLen] = false;
        pathLen++;

        if(root.left == null && root.right == null){
            if(pathLen - k - 1 >= 0 && visited[pathLen -k - 1] == false){
                counter[0]++;
                visited[pathLen - k - 1] = true;
                return ;
            }
        }

        printNodesAtKDistance(root.left, k, pathLen, path, visited, counter);
        printNodesAtKDistance(root.right, k, pathLen, path, visited, counter);
    }

    public static void main(String[] args) {
        int[] data = {1,2,3,4,5,6,7,8};
        int k = 1;
        TreeNode root = construct(data);
        inorder(root);
        System.out.println();
        // leafPaths(root,"");
        int[] path = new int[1000];
        boolean[] visited = new boolean[1000];
        System.out.println("height: "+height(root));
        int[] counter = new int[1];

        printNodesAtKDistance(root, k, 0, path, visited, counter);
        print(counter[0]);
    }

    
}
