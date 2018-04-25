package demo;


	import java.io.BufferedReader;
	import java.io.IOException;
	import java.io.InputStreamReader;
	import java.util.concurrent.atomic.AtomicLong;
	import org.springframework.web.bind.annotation.RequestMapping;
	import org.springframework.web.bind.annotation.RequestParam;
	import org.springframework.web.bind.annotation.RestController;

	@RestController
	public class greetingController {

	    private static final String template = "Hello, %s!";
	    private final AtomicLong counter = new AtomicLong();

	    @RequestMapping("/greeting")
	    public greeting greeting(@RequestParam(value="name", defaultValue="World3") String name) {
	        return new greeting(counter.incrementAndGet(),
	                            String.format(template, name));
	    }
	    

	    @RequestMapping("/callpy")
	    public String callPy() {
	    	pythonCaller caller = new pythonCaller();
	    	String s = caller.CallPython();
	    	return s;
	    	//return "test";
	    }
	    
	    @RequestMapping("/callpredict")
	    public String Callpredict(@RequestParam(value="desc", defaultValue="World3") String desc) {
	    	
	    	try {


	    		//String input = String.format(template, desc);
	            String[] callAndArgs= {"python","externalFile/hello2.py",desc};

	            Runtime rt = Runtime.getRuntime();

	            Process proc = rt.exec(callAndArgs);

	            BufferedReader stdInput = new BufferedReader(new 
	                 InputStreamReader(proc.getInputStream()));

	            BufferedReader stdError = new BufferedReader(new 
	                 InputStreamReader(proc.getErrorStream()));

	            // read the output from the command
	            System.out.println("Here is the standard output of the command:\n");
	            String s = null;
	            while ((s = stdInput.readLine()) != null) {
	                System.out.println(s);
	                return s;
	            }

	            // read any errors from the attempted command
	            System.out.println("Here is the standard error of the command (if any)");
	            while ((s = stdError.readLine()) != null) {
	                System.out.println(s);
	                return s;
	            }

	        }

	        catch (IOException e) {

	            System.out.println("exception occured");

	            e.printStackTrace();

	            System.exit(-1);

	        }
	    	
	    	return null;
	    }
	}