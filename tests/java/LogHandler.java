/********************************************************************************
* date          Eng      SCR          Description
* 2019-09-11    morrisf  SYSSAT-448   Created for testing - copied from DEMS/src
*********************************************************************************/
package testmft;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogRecord;
import java.util.logging.Logger;

/**
 * Turns over the log file at the end of each day with the new days DTG
 * 
 * @author Jason L. Rance
 * @version 1.2
 */
public class LogHandler extends Handler {
    private static final Logger ALOGGER = Logger.getLogger(LogHandler.class.getName());

    private static final SimpleDateFormat LDF = new SimpleDateFormat("yyyyMMdd");

    private Date myDate = new Date();

    private File myLocalLogDir;

    private FileWriter myFileWriter;

    /**
     * Default constructor for LogHandler
     * 
     * @param aLogDir directory to write log file to
     */
    public LogHandler(File aLogDir) {
        super();
        ALOGGER.setLevel(Level.INFO);
        myLocalLogDir = aLogDir;
        this.setFormatter(new ZuluHourFormatter());
        try {
            myFileWriter = new FileWriter(new File(aLogDir, "LOG" + LDF.format(myDate) + ".log"), true);
        } catch (IOException e) {
            ALOGGER.warning("TESTMFT failed to create a log file with the correct date");
            e.printStackTrace();
        }
    }

    /**
     * @see java.util.logging.Handler#close()
     */
    public void close() {
        try {
            myFileWriter.close();
        } catch (IOException e) {
            ALOGGER.warning("TESTMFT failed to close the file - " + myFileWriter.toString());
            e.printStackTrace();
        }
    }

    /**
     * flushes the log file 
     *
     * @see java.util.logging.Handler#flush()
     */
    public void flush() {
        try {
            myFileWriter.flush();
        } catch (IOException e) {
            ALOGGER.warning("failed to flush the log file from memory");
            e.printStackTrace();
        }
    }

    /**
     * implements java.util.logging.Handler.publish
     *
     * @see java.util.logging.Handler#publish(java.util.logging.LogRecord)
     */
    public synchronized void publish(LogRecord arg0) {
        try {
            if (switchLogDate()) {
                this.myDate = new Date();
                myFileWriter.close();
                myFileWriter = new FileWriter(new File(myLocalLogDir, "LOG" + LDF.format(myDate) + ".log"), true);
            }
            if (this.getLevel().intValue() <= arg0.getLevel().intValue()) {
                String myOutputString = getFormatter().format(arg0);
                myFileWriter.write(myOutputString);
            }
        } catch (IOException e1) {
            // Consider removing logging to prevent infinit loop possibility.
            ALOGGER.warning("Log date for TESTMFT was not added to TESTMFT's log file - 300");
            ALOGGER.warning(e1.getMessage());
        } finally {
            this.flush();
        }
    }

    /**
     * changes to the newest date
     * 
     * @return boolean
     */
    private boolean switchLogDate() {
        Date currentDate = new Date();
        return !LDF.format(myDate).equals(LDF.format(currentDate));
    }
}
