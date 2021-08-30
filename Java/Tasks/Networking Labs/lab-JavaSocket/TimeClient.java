import java.io.*;
import java.net.*;
/**
*This program is a socket client application that connects to a time server to get the current date time.
* @author jl922223
*/
public class TimeClient{

  public static void main(String[] args) throws Exception{
    String hostname = "time.nist.gov"; // remote server host-name
    int port = 13; // remote server port number that client can access

    // creating a connection request to remote server using the hostname and the port
    Socket socket = new Socket(hostname, port);

    //InputStream object from the client socket to read data from the server
    InputStream input = socket.getInputStream();
    // Wrap the InputStream object in an InputStreamReader or BufferedReader to read data at higher level
    // using InputStreamReader:

    InputStreamReader reader = new InputStreamReader(input);
    // or using BufferedReader:
    // BufferedReader buffReader = new BufferedReader(new InputStreamReader(input));
    // String line = buffReader.readLine();
    // build the output message

    int character;
    StringBuilder data = new StringBuilder();
    while ((character = reader.read()) != -1) {
      data.append((char) character);
    }
    System.out.println(data);
  }
}
