import java.util.*;


class CaesarCipher
{
    
    public static StringBuffer encrypt(String given, int shift)  //this is the encryptor function
    {
        StringBuffer encrypted= new StringBuffer();
 
        for (int i=0; i<given.length(); i++)
        {
            if (Character.isUpperCase(given.charAt(i)))
            {
                char add = (char)(((int)given.charAt(i) + shift - 65) % 26 + 65);
                                  
                encrypted.append(add);
            }
            else
            {
                char add1= (char)(((int)given.charAt(i) + shift - 97) % 26 + 97);
                                  
                encrypted.append(add1);
            }
        }
        return encrypted;
    }
 
 
    public static void main(String[] args) //this is the driver method to implement the above string
    {
        Scanner sc=new Scanner(System.in); //input streaming using scanner class from java.util library
        
        System.out.println("Enter the text you want to convert");//text to be encrypted
        String given=sc.nextLine();
        
        System.out.println("Enter your shift");//shift value
        int shift = sc.nextInt();
        System.out.println("Text  : " + given);
        System.out.println("Shift : " + shift);
        System.out.println("The cipher is: " + encrypt(given, shift));
    }
}