import java.math.BigInteger;
public class Main {
	public static void main(String[] args) {
        BigInteger x = BigInteger.valueOf(1);
        BigInteger y = BigInteger.valueOf(1);
        BigInteger z = BigInteger.valueOf(0);
        BigInteger holder;
		int counter = 2;
		while (z.toString(10).length() < 1000) {
		    z = x.add(y);
		    holder = y;
		    y = z;
		    x = holder;
		    counter += 1;
        }
        System.out.println(counter);		
	}
}