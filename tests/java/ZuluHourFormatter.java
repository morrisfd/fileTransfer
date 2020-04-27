/********************************************************************************
* date          Eng      SCR          Description
* 2019-09-11    morrisf  SYSSAT-448   Created for testing - copied from DEMS/src
*********************************************************************************/
package testmft;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.logging.Formatter;
import java.util.logging.LogRecord;


/**
 * Generates the time stamp to be used in the logging functionality.
 * 
 *  @author HQ AFWA/SCS 
 *  @since MDrive_dirc  1.0  
 *  @version   1.0  Jul 13, 2006
 */
public class ZuluHourFormatter extends Formatter {

    
    public ZuluHourFormatter() {
        super();

    }

    /** 
     *  @param aRecord
     *  @return
     *  @see java.util.logging.Formatter#format(java.util.logging.LogRecord)
     */
    public String format(LogRecord aRecord) {
        Throwable t = aRecord.getThrown();
        String tempError = "";
        while (t != null) {
            tempError += t.getMessage() + " ";
            t = t.getCause();
        }
        
        SimpleDateFormat mySDF = new SimpleDateFormat("E MMM dd HH:mm:ss z yyyy");
        StringBuffer sb = new StringBuffer();
        Date myDate = new Date(aRecord.getMillis());
        if (aRecord.getThrown() != null) {
            sb.append("EXCEPTION STUFF:" + tempError);
        }
        String date = mySDF.format(myDate);
        date = date.replace(date.split(" ")[4], date.split(" ")[4].substring(0, 3));
        sb.append(date).append(" - ");
        //sb.append(mySDF.format(myDate)).append(" ");
        //sb.append(aRecord.getSourceClassName()).append(" ");
        //sb.append(aRecord.getSourceMethodName()).append(" ");
        //sb.append(aRecord.getLevel().getLocalizedName()).append(": ");
        sb.append(aRecord.getMessage()).append(" \n");
        return sb.toString();
    }

}
