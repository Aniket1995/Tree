//{ Driver Code Starts

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

class Node {
    int data;
    Node left, right;
    
    public Node(int data){
        this.data = data;
        left = right = null;
    }
}

class GFG {
    
    public static void inorder(Node root){
        if(root == null)
            return;
        
        inorder(root.left);
        System.out.print(root.data+" ");
        inorder(root.right);
    }
    
    public static void po(Object o){
        System.out.println(o);
    }
    
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-- > 0){
		    HashMap<Integer, Node> map = new HashMap<>();
		    
		    int n = sc.nextInt();
             
            Node root = null;
            Node parent;
		    while(n-- > 0){
		        int p = sc.nextInt();
		        if(!map.containsKey(p)){
		            root = new Node(p);
		            map.put(root.data, root);
		        }
		        parent = map.get(p);
		        
		        int ch = sc.nextInt();
		        Node child = new Node(ch);
		        
		        char c = sc.next().charAt(0);
		        if(c == 'L')
		            parent.left = child;
		        else if(c == 'R')
		            parent.right = child;
		            
		        map.put(ch, child);
		    }
		    
		    //inorder(root);
		    //System.out.println();
		    Solution obj = new Solution();
			po(obj.pairs(root));
		}
	}
}


// } Driver Code Ends



class Solution {
    /*
    The structure of the node class is:
    class Node {
    int data;
    Node left, right;
        public Node(int data){
            this.data = data;
        }
    }
    */
    
    public int merge(int[] arr, int[] tmp, int st, int mid, int end){
        
        int i = st;
        int j = mid;
        
        int k = st;
        int inv = 0;
        while(i <= (mid-1) && j <= end){
            if(arr[i] <= arr[j]){
                tmp[k++]=arr[i++];
            }else{
                tmp[k++]=arr[j++];
                inv += (mid - i);
            }
        }
        
        while(i <= (mid-1)){
            tmp[k++]=arr[i++];
        }
        
        while(j <= end){
            tmp[k++]=arr[j++];
        }
        
        for(int x=st;x<=end;x++){
            arr[x] = tmp[x];
        }
        
        return inv;
        
    }
    
    public int mergeSort(int[] arr, int [] tmp, int st, int end){
        int inv=0;
        if(st < end){
            int mid = (st + end)/2;
            
            inv = mergeSort(arr, tmp, st, mid);
            inv += mergeSort(arr, tmp, mid+1, end);
            
            inv += merge(arr, tmp, st, mid+1, end);
        }
        return inv;
    }
    
    public int countNode(Node root){
        if(root == null){
            return 0;
        }
        
        return 1 + countNode(root.left) + countNode(root.right);
    }
    
    public void inorder(Node root, int[] arr, int[] i){
        if(root == null){
            return;
        }
        
        inorder(root.left, arr, i);
        arr[i[0]++]=root.data;
        inorder(root.right, arr, i);
    }
    
    public int pairs(Node root){
        int n = countNode(root);
        int[] tmp = new int[n];
        int[] i = new int[1];
        int[] arr = new int[n];
        
        inorder(root, arr, i);
        
        return mergeSort(arr, tmp, 0, n-1);
    }

}