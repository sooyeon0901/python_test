package cherry.mint;

public class QrUrl {

  public static void setQrUrl(String[] mintAdreses) {
    for(int i=0; i<mintAdreses.length; i++){
      String url = "https://solscan.io/token/" + mintAdreses[i];
      System.out.println(url);
    }
  }

  public static void main(String[] args) {
    String[] mintAdreses = {
      "aaa", "bbb"
    };
    
    setQrUrl(mintAdreses);
  }

  
}
