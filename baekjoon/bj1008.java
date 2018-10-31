import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double a, b;
        a = input.nextDouble();
        b = input.nextDouble();
        System.out.printf("%.9f\n", a/b);
    }
}
