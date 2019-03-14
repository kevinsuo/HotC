/*
 * javac test.java
 * java test
 *
 * for alpine linux
 * apk add --no-cache openjdk8
 * add the following to path
 * ENV JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
 * ENV PATH="$JAVA_HOME/bin:${PATH}"
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


