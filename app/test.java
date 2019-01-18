/*
 * javac test.java
 * java test
 */

public class test {
	public static void main(String[] args) {
		long n = 0;
		for (long i = 0; i < 10000000; i++) {
			n=n+i;
		}
		System.out.println(n);
	}
}


