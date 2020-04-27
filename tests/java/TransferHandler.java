/********************************************************************************
* date		Eng	 SCR		Description
* 2019-09-11    morrisf  SYSSAT-448     Created for testing - copied from DEMS/src 
*********************************************************************************/
package testmft;

import java.util.Properties;
import java.util.logging.Logger;
import java.io.IOException;
import java.io.File;
import java.io.StringWriter;
import java.io.PrintWriter;
import java.io.InputStreamReader;

/**
 * This is the handler that manages all transferring files.
 * 
 * @author Franke Morris
 * @version 1.0
 */
public class TransferHandler {
    private static Properties transProperties = new Properties();
    private static final Logger ALOGGER = Logger.getLogger(TransferHandler.class.getName());

    public TransferHandler(Properties aPropertiesFile) {
    //public TransferHandler() {
        super();
	transProperties = aPropertiesFile;
    }

    public static void transferFiles(String transferID) throws Exception{
	Process proc = null;
        try{

	    String propertiesFile = transProperties.getProperty("properties.file.name");
	    String fileTransferPath = transProperties.getProperty("filetransferPath");
	    ALOGGER.info("propertiesFile:" +  propertiesFile);
	    ALOGGER.info("fileTransferPath:" + fileTransferPath);
            // Transfer products
	    String cmd = fileTransferPath + " " + propertiesFile + " " + transferID;
            proc = Runtime.getRuntime().exec(cmd);                        
            if (proc.waitFor() == 0){
	    	if (proc.exitValue() != 0){
			throw new Exception("transferFiles failed to transfer files - check logs.");
	    	}
	    }else{
			throw new InterruptedException("transferFiles process was Interrupted - check logs.");
	    }
		
        } catch (Exception e) {
            //ALOGGER.severe(e.getMessage());
	    throw e;
        } finally {
            if (proc != null){
	        proc.destroy();	
	    }
	}
    }
}
