package demo;

import org.python.core.PyFunction;
import org.python.core.PyInteger;
import org.python.core.PyObject;
import org.python.util.PythonInterpreter;

public class pythonCaller {

	public String CallPython() {

		try {
			
			PythonInterpreter interpreter = new PythonInterpreter();
			interpreter.execfile("externalFile/hello.py");
			PyFunction func = (PyFunction) interpreter.get("caller", PyFunction.class);

			// int a = 2010, b = 2;
			// PyObject pyobj = func.__call__(new PyInteger(a), new PyInteger(b));

			PyObject pyobj = func.__call__();
			System.out.println("anwser = " + pyobj.toString());
			interpreter.close();
			return pyobj.toString();

		} // main

		catch (Exception e) {
			System.out.println(e);

			return "error";
		}

	}
}