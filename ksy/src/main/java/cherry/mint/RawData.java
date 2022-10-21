package cherry.mint;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.IntStream;


public class RawData {

  public static void parsing() throws FileNotFoundException {
    List<String> a = new ArrayList<>();
    List<Map<String, Object>> b = new ArrayList<>();
    Map<String, Object> sep = new LinkedHashMap<String, Object>();
    Map<String, Object> c1 = new LinkedHashMap<String, Object>();
    Map<String, Object> c2 = new LinkedHashMap<String, Object>();
    Map<String, Object> c3 = new LinkedHashMap<String, Object>();
    Scanner scanner = new Scanner(new File("/data2/sykim/test_file_java/ksy/src/main/java/cherry/resources/raw_data.txt"));
    
    while (scanner.hasNext()) {
        String str = scanner.next();
        a.add(str);
        // System.out.println(str);
    }
    // System.out.println("=== 0 >" + a.get(6)); 

    for(int i=0; i<a.size(); i++){
      if(i % 6 == 3){
        c1.put("trait_type", "배경");
        c1.put("value", a.get(i));
        b.add(c1);
        System.out.println("=== attr1 >" + a.get(i)); 
        System.out.println("=== c1 >" + c1); 
      } else if(i % 6 == 4){
        c2.put("trait_type", "캐릭터");
        c2.put("value", a.get(i));
        b.add(c2);
        System.out.println("=== attr2 >" + a.get(i)); 
        System.out.println("=== c2 >" + c2); 
      } else if(i % 6 == 5){
        c3.put("trait_type", "프레임");
        c3.put("value ", a.get(i));
        b.add(c3);
        System.out.println("=== attr3 >" + a.get(i)); 
        System.out.println("=== c3 >" + c3); 
      }
    }
    System.out.println("=== b0 >" + b.get(0)); 
    System.out.println("=== b1 >" + b.get(1)); 
    System.out.println("=== b2 >" + b.get(2)); 
    
    int setSize = 0;
    
    for(int i=0; i<b.size(); i++){
      List<Map<String, Object>> d = b.subList(0, 3);
      sep.put("attributes", d);
    }
  }

  public static void main(String[] args) throws FileNotFoundException {
    parsing();
  }
}
