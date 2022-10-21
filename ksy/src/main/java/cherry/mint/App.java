package cherry.mint;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader; 
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.json.simple.parser.ParseException;
import org.apache.commons.io.FileUtils;

import com.google.api.client.json.GenericJson;
import com.google.api.client.json.gson.GsonFactory;
import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;


public class App {

    static String convertJsonToString(GenericJson json, Boolean isPretty){
        try {
            return isPretty ? json.toPrettyString() : json.toString();
        }
        catch(Exception e) {
            e.printStackTrace();
            return "";
        }
    }

    static String jsonString(GenericJson json) {
        return convertJsonToString(json, true); // 기존 false에서 true로 변경
    }

    /**
    * Map을 GenericJson으로 변경
    */
    static GenericJson mapToJson(Map map) {
        try {
            return new GsonFactory().createJsonParser(new Gson().toJson(map))
                                        .parse(GenericJson.class);
        }
        catch(Exception e) {
            e.printStackTrace();
            return null;
        }    
    }

    public static void copy_files(int dup, String src_path, String tgt_path, List<String> s_file_names, 
                                List<String> s_file_exts, int start_index, int serial, String numbering) throws IOException {
        int dup_n = dup;

        // Path dir = Paths.get(tgt_path);
        // if(!Files.isDirectory(dir)){
        //     Files.createDirectory(dir); //ksy_test 디렉토리가 없으면 생성 < done
        // }
        // 파일 담을 dev 디렉토리가 없으면 생성하기
        Path dev = Paths.get("/data2/nft/ksy_test/dev/");
        if(!Files.isDirectory(dev)){
            Files.createDirectory(dev);
        }
    
        for( int i=0; i<s_file_names.size(); i++ ){
            for( int k=0; k < dup_n; k++ ){
                serial = serial + 1;

                for(int j=0; j<s_file_exts.size(); j++){
                    String png = s_file_exts.get(j);
                    String s_file_path = src_path + s_file_names.get(i) +  "." + png; //s_file_path::/data2/nft/ksy_test/files/제목테스트3 #.png
                    String t_file_path = tgt_path + "dev/" + numbering + "." + png; //t_file_path::/data2/nft/ksy_test/00249.png
                    System.out.println("s_file_path::"+ s_file_path);
                    System.out.println("t_file_path::"+ t_file_path);

                    File a = new File(s_file_path);
                    File b = new File(t_file_path);
                    
                    FileUtils.copyFile(a, b);
                }
            }
        }
    
    }

    // 데이터 값을 생성하고 바꾸는 메소드
    public static List<String> attributes_meta(){
        List<String> list = new ArrayList<>();
        Map<String, String> attr_map = new LinkedHashMap<>();
        Map<String, String> attr_map2 = new LinkedHashMap<>();

        attr_map.put("trait_type", "이름111111");
        attr_map.put("value", "111111");
        attr_map2.put("trait_type", "이름222222");
        attr_map2.put("value", "222222");

        list.add(0, attr_map.toString());
        list.add(1, attr_map2.toString());

        return list;
    }
    public static Map<String, Object> properties_meta(){
        Map<String, Object> props = new LinkedHashMap<String, Object>();
        List<String> files_list = new ArrayList<>();
        List<String> creators_list = new ArrayList<>();
        Map<String, String> files = new LinkedHashMap<>();
        Map<String, Object> creators_1 = new LinkedHashMap<String, Object>();
        Map<String, Object> creators_2 = new LinkedHashMap<String, Object>();

        files.put("uri", "501.png");
        files.put("type", "image/jpg");
        creators_1.put("address", "9nnGAh8QnYLNmCgf8JP6J7VH7mxg3zgh8BoZei1MxEWX");
        creators_1.put("share", 100);
        creators_2.put("address", "C98EGsTDSPZCaWQRKtsrpRD5WsyWmnu7LbRiWYTDaKiC");
        creators_2.put("share", 0);

        files_list.add(0, files.toString());
        creators_list.add(0, creators_1.toString());
        creators_list.add(1, creators_2.toString());

        props.put("files", files_list);
        props.put("category", "image");
        props.put("creators", creators_list);

        return props;
    }
    public static Map<String, Object> collection_meta(){
        Map<String, Object> collection = new LinkedHashMap<String, Object>();
        collection.put("name", "사회적협동조합");
        collection.put("family", "위마켓웰페어");

        return collection;
    }
    /** [png 용 메타데이터]
     * : mp3나 html 버전을 따로 만들어야함, 커버이미지가 필요.
     * 
     * // 배열 객체 셀렉 완료 
        System.out.println("=== jo > " 
        + jo.getAsJsonArray("attributes").get(1).getAsJsonObject().get("trait_type"));
        // attributes array 셀렉
        jo.getAsJsonArray("attributes");
        System.out.println("=== jo > " + jo.getAsJsonArray("attributes"));
        // 값 세팅
        jo.getAsJsonArray("attributes").get(1).getAsJsonObject().addProperty("trait", "rkskekfk");
        // 값 출력
        System.out.println("=== jo > " + jo.getAsJsonArray("attributes").get(1).getAsJsonObject());
     */
    public static void make_meta(int dup, String src_path, String tgt_path, List<String> s_file_names,
                                List<String> s_file_exts, int start_index, int nft_name_serial_fill, String numbering, String sname) throws IOException, ParseException{
        int dup_n = dup;
        
        Reader reader = new FileReader("/data2/sykim/test_file_java/ksy/src/main/java/cherry/resources/metadata.json");
        JsonParser parser = new JsonParser();
        JsonObject jo = (JsonObject) parser.parse(reader);

        // attributes 
        List<String> _attr = attributes_meta();
        // properties 
        Map<String, Object> _prop = properties_meta();
        // collections
        Map<String, Object> _collection = collection_meta();

        // 메타데이터 세팅
        Map<String, Object> document = new LinkedHashMap<String, Object>();
        document.put("name", "고흐의 별이 빛나는 밤");
        document.put("symbol", "VAN");
        document.put("description","이 캠페인의 설명 입니다.");
        document.put("seller_fee_basis_points", 1000);
        document.put("image", "https://www.naver.com");
        document.put("external_url", "https://www.naver.com");
        document.put("attributes", _attr);
        document.put("properties", _prop);
        document.put("collection", _collection);
        // Map > GenericJson > String
        String optInfo = jsonString(mapToJson(document));
        System.out.println("=== result > " + optInfo);

        //json to file
        // String path = "/data2/sykim/test_file_java/ksy/src/main/java/cherry/resources/test.json";
        // FileWriter f = new FileWriter(path);
        // f.write(optInfo);
        // f.close();
    }

    public static void main( String[] args ) throws IOException, ParseException {
        int dup = 10;
        int start_index = 0;
        int serial = start_index;
        int nft_name_serial_fill = 3;
        String numbering = String.format("%05d", serial); //nft_file_serial_fill
        String sname = "title #";

        String s_path = "/data2/nft/ksy_test/files/";
        String t_path = "/data2/nft/ksy_test/";
        List<String> s_file_names = new ArrayList<String>();
        s_file_names.add("러브스토리");
        s_file_names.add("앤디워홀");
        s_file_names.add("프렌즈");
        List<String> s_file_exts = new ArrayList<String>();
        s_file_exts.add("png");

        // copy_files(
        //     dup, 
        //     s_path, 
        //     t_path, 
        //     s_file_names,
        //     s_file_exts,
        //     start_index,
        //     serial,
        //     numbering
        // );

        make_meta(
            dup, 
            s_path, 
            t_path, 
            s_file_names,
            s_file_exts,
            start_index,
            nft_name_serial_fill,
            numbering,
            sname
        );
    }
}
