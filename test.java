import static org.junit.Assert.*;

import org.junit.Test;

public class HelloWorld {
	
	public String HelloWorld(){
		return "Hello World";
	}

	@Test
	public void test_helloworld(){
		assertEquals("Hello World", HelloWorld());
	}

}
