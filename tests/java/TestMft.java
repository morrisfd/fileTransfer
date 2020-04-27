/********************************************************************************
* date		Eng	 SCR	      Descript
* 2019-09-11    morrisf  SYSSAT-448   Created for testing python call from java.
*********************************************************************************/
package testmft;

import java.io.File;
import java.io.IOException;
import java.util.Enumeration;
import java.util.Iterator;
import java.util.List;
import java.util.Properties;
import java.util.Timer;
import java.util.logging.Logger;
import java.util.logging.Level;
import java.io.StringWriter;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * 
 * 
 * @author Franke Morris
 * @version 1.0
 */
public final class TestMft {
    
    
    private static Properties myPropertiesFile = new Properties();
    private static final Logger ALOGGER = Logger.getLogger(TestMft.class.getPackage().getName());
    static {
	InputStream input = ClassLoader.getSystemResourceAsStream("config/TESTMFT.properties");
        try {
            myPropertiesFile.load(input);
            TransferHandler myTransferHandler = new TransferHandler(myPropertiesFile);
            File myDirectory = new File(myPropertiesFile.getProperty("logger.directory", "."));
            Level logLevel = Level.parse(myPropertiesFile.getProperty("logger.level", "."));
            LogHandler myLogHandler = new LogHandler(myDirectory);
            ALOGGER.addHandler(myLogHandler);
            ALOGGER.setLevel(logLevel);
        } catch (IOException e) {
            throw new ExceptionInInitializerError(e);
        } finally {
	    try {
		    if(input != null){
			input.close();
		   }
	    } catch (IOException e) {
	    	throw new ExceptionInInitializerError(e);
            } 
	}
    }

     /**
     * default constructor for TestMft
     */
    private TestMft() {
        super();
    }

    /**
     * Kicks off
     */
    private void startProcessing(String transferID) {
        // Tranfer fdm test
        try{
            ALOGGER.info("MFT Started " + transferID);		
	    TransferHandler.transferFiles(transferID);
	    ALOGGER.info("MFT Finished " + transferID);
        } catch (Exception e) {
            ALOGGER.severe("TestMft failed to transfer files - check logs");
            StringWriter error = new StringWriter();
            e.printStackTrace(new PrintWriter(error));
            ALOGGER.severe(error.toString());
        }

    }
    
     /**
     * main
     * @param args main class for TESTMFT
     */
    public static void main(String[] args) {
	TestMft myTestMft = new TestMft();        
	for(int i = 0; i < args.length; i++){
	    System.out.println(args[i]);
	    myTestMft.startProcessing(args[i]);    
        }
    }
}
