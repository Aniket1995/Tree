
import java.util.ArrayList;
import java.util.Collections;

class LeftView {

    static int maxLvl = 0;

    public static void main(String[] args) {
        int[] ia = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 };
        Node root = Node.formTree(null, ia, 0);
        leftView(root);
        maxLvl = 0;
        rightView(root.right);

        // topView(root);
    }

    static void topView(Node root) {
        if(root == null){
            return;
        }
        printLeft(root.left);
        System.out.print(root.data + " ");
        printRight(root.right);
    }

    static void printLeft(Node root) {
        if (root == null) {
            return;
        }
        printLeft(root.left);
        System.out.print(root.data + " ");
    }

    
    static void printRight(Node root) {
        if (root == null) {
            return;
        }

        System.out.print(root.data + " ");
        printRight(root.right);
    }

    static void leftView(Node root) {
        ArrayList<Integer> lv = new ArrayList<>();
        if (root != null) {
            getLeftView(root, lv, 1);
        }
        Collections.reverse(lv);
        lv.forEach(e -> System.out.print(e + " "));
    }

    static void rightView(Node root) {
        if (root != null) {
            getRightView(root, 1);
        }
    }

    static void getLeftView(Node root, ArrayList<Integer> lv, int lvl) {
        if (root == null) {
            return;
        }

        if (maxLvl < lvl) {
            lv.add(root.data);
            maxLvl = lvl;
        }

        getLeftView(root.left, lv, lvl + 1);
        getLeftView(root.right, lv, lvl + 1);
    }

    static void getRightView(Node root, int lvl) {
        if (root == null) {
            return;
        }

        if (maxLvl < lvl) {
            System.out.print(root.data + " ");
            maxLvl = lvl;
        }

        getRightView(root.right, lvl + 1);
        getRightView(root.left, lvl + 1);
    }

    public static void printTree(Node root) {
        if (root == null)
            return;
        System.out.println(root.data);
        printTree(root.left);
        printTree(root.right);
    }
}
