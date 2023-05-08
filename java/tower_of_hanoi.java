public class tower_of_hanoi{

    public static void func_tower_of_hanoi(int n, char source, char destination, char intermediate){
        if( n >= 1){
            func_tower_of_hanoi(n-1, source, intermediate, destination);
            String print =  n + " " + source + " " + destination;
            System.out.println(print);
            func_tower_of_hanoi(n-1, intermediate, destination, source);
        }
    }
    
    public static void main(String [] args){
        int n = 2;
        char source = 'A';
        char intermediate = 'B';
        char destination = 'C';

        func_tower_of_hanoi(n, source, destination, intermediate);

    }
}