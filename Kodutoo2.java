import java.math.*;
import java.util.Random;

public class Kodutoo2 {

    public static void main (String[] args) {

        long startTime = System.currentTimeMillis();
        BigInteger testValue = new BigInteger("10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000039508120821");
        boolean isPrime = false;
        long test = 1;

        while (!isPrime) {
            System.out.println("Test " + test + "\tNumber: " + testValue);
            isPrime = testPrime(testValue);
            if (!isPrime)
                isPrime = testPrime(testValue);
            if (isPrime) {
                System.out.println("\tIS PRIME! Time: " + ((double)((System.currentTimeMillis() - startTime)))/1000 + " s");
            }
            testValue = testValue.add(BigInteger.valueOf(100000000000L));
            test++;
        }
    }

    // Tests if the number is a prime number or not (Euler-Fermat' test)
    private static boolean testPrime(BigInteger value) {

        // Create a random number less than the number tested
        BigInteger randomValue;
        do {
            randomValue = new BigInteger(512, new Random());
        } while (randomValue.compareTo(value) != -1 || randomValue.compareTo(BigInteger.ONE) != 1);

        // Get greatest common divisor of number tested and random number
        BigInteger greatestCommonDivisor = value.gcd(randomValue);

        if (greatestCommonDivisor.compareTo(BigInteger.ONE) != 0)
            return false;

        if (randomValue.modPow(value.subtract(BigInteger.ONE), value).compareTo(BigInteger.ONE) == 0)
            return true;

        return false;

    }
}
