import java.net.*;
import java.io.*;
/**
* This program demostrates a client socket application that connects
* to a Whois server to get information about a domain name.
* @author jl922223
*/
public class WhoisClient {

  public static void main(String[] args) throws Exception {
    String hostname = "whois.internic.net";
    int port = 43;

    String whoIsDomainName = "google.com";
    Socket socket = new Socket(hostname, port);
    // To send data to the server, get the OutputStream object from the socket first.
    OutputStream output = socket.getOutputStream();
    PrintWriter writer = new PrintWriter(output, true);
    writer.println(whoIsDomainName);

    // InputStream object from the client socket to read data from the server.
    InputStream input = socket.getInputStream();
    BufferedReader reader = new BufferedReader(new InputStreamReader(input));
    String line;
    while ((line = reader.readLine()) != null){
      System.out.println(line);
    }
  }
}
