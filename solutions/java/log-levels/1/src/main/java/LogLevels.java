public class LogLevels {
    
    public static String message(String logLine) {
        String subStringLog = logLine.substring(logLine.indexOf(" "));
        return subStringLog.trim();        
    }

    public static String logLevel(String logLine) {
        String subStringLog = logLine.substring(logLine.indexOf("[") + 1, logLine.indexOf("]"));
        return subStringLog.toLowerCase();
    }

    public static String reformat(String logLine) {
        StringBuilder initialzer = new StringBuilder(message(logLine));
        initialzer.append(" (");
        initialzer.append(logLevel(logLine));
        initialzer.append(")");
        return initialzer.toString();
    }
}
