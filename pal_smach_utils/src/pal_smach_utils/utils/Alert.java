import javax.swing.JOptionPane; 

public class Alert{
	public static void main(String argv[]){
        JOptionPane.showMessageDialog (null, (argv.length > 0) ? argv[0]: "Alert"); 
	}
}
