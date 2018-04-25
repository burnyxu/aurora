package demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AuroraDemo2Application {

	public static void main(String[] args) {
		
		SpringApplication.run(AuroraDemo2Application.class, args);
		
		System.out.println("Let's inspect the beans provided by Spring Boot:.............");

	}
}
