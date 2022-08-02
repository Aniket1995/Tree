import java.util.Stack;

class Node{
    int data;
    Node left,right;

    public Node(int data){
        this.data = data;
        this.left = this.right = null;
    }
}



class isFullBT{

    public static boolean isFull(Node root){
        if(root == null){
            return true;
        }
        if(root.left == null && root.right == null){
            return true;
        }
        if(root.left == null || root.right == null){
            return false;
        }
        return true;
    }

    public static boolean isFullBt(Node root){
        if(root == null){
            return true;
        }
        Stack<Node> s= new Stack<>();
        s.push(root);

        while(!s.isEmpty()){
            Node n = s.pop();
            if(!isFull(n)){
                return false;
            }
            if(n.left != null){
                s.push(n.left);
            }
            if(n.right != null){
                s.push(n.right);
            }
        }
        return true;
    }
    public static void print(boolean b){
        System.out.println(b);
    }
    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        
        root.right.left = new Node(4);
        print(isFullBt(root));
    }
}
