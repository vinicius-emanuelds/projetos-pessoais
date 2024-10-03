
import java.util.Locale;
import java.util.Scanner;

public class ContaTerminal {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);

        System.out.println("Por favor, diga seu nome: ");
        String nome = scanner.next();

        System.out.println("Agora, digite o número da Agência: ");
        String agencia = scanner.next();

        System.out.println("Digite o número da conta: ");
        int conta = scanner.nextInt();

        System.out.println("Qual é seu saldo atual? ");
        double saldo = scanner.nextDouble();

        scanner.close();

        System.out.println("Olá " +  nome + ", obrigado por criar uma conta em nosso banco! Sua nova agência é a " + agencia + ", conta nº " + conta + ". Seu saldo de " + saldo +"já está disponível para saque");
    }
}
