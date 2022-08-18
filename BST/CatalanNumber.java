package BST;

public class CatalanNumber {

        //Function to return the total number of possible unique BST.
    static long numTrees(int N)
    {
        if(N == 1 || N == 0){
            return 1;
        }
        
        long[] cat = new long[N+2];
        
        cat[0] = 1;
        
        cat[1] = 1;
        
        for(int i=2; i<=N;++i){
            for(int j=0;j<i;++j){
                cat[i] += (cat[j] * cat[i-j-1]);
                cat[i] = cat[i] % 1000000007;
            }
        }
        return cat[N];
    }

    public static void main(String[] args) {
        for(int i=0;i<=384;++i){
            System.out.println(i+" => "+numTrees(i));
        }
        
    }
    
}
