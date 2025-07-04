package Question4;

import javax.swing.JOptionPane;

public class Solution {
    
    public static void main(String[] args) {
        int n;
        try {
            n = Integer.parseInt(JOptionPane.showInputDialog("Enter diamond size: "));
            if(n < 0){
                JOptionPane.showMessageDialog(null, "AssertionError is captured: Size should be > 0.");
            }
            else{
                JOptionPane.showMessageDialog(null, drawDiamond(n));
            }
        } catch (Exception e) {
                JOptionPane.showMessageDialog(null, "Input is not integer");
        }
    }

    static String drawDiamond(int n){
        int space = n - 1;
        StringBuffer s = new StringBuffer();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < space; j++){
                s.append(" ");
            }
            for(int j = 0; j <= i; j++){
                s.append("* ");
            }
            s.append("\n");
            space--;
        }
        space = 0;
        for(int i = n; i > 0; i--){
            for(int j = 0; j < space; j++){
                s.append(" ");
            }
            for(int j = 0; j <= i; j++){
                s.append("* ");
            }
            s.append("\n");
            space++;
        }
        return s.toString();
    }
    
}
