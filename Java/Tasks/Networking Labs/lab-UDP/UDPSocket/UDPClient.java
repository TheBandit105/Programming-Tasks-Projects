package UDPSocket;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.Scanner;

/**
 * This program demonstrates a UDP client
 * @author at015244
 * @version 1.0
 * @since 2020-12-12
 */
public class UDPClient {
    private InetAddress ipAddress;
    private int sendPort;
    private int recvPort;
    
    /**
    *@param serverAdress
    *@param serverPort
    *@param clientPort
    *@throws Exception
    */

    private UDPClient(InetAddress serverAddress, int sendPort, int recvPort) throws Exception {
        this.ipAddress = serverAddress;
        this.sendPort = sendPort;
        this.recvPort = recvPort;
    }
    
    /**
     * The start method initiates the communication by sending datagram to the server
     * @throws IOException
     */
    private void start() throws IOException {
    	// Initiate the Datagram Socket 
    	DatagramSocket udpSocket = new DatagramSocket();
    	
    	//Take user input using, e.g., useing scanner 
    	System.out.println("Type your message here: ");
    	Scanner textin = new Scanner(System.in);
    	String typing = textin.nextLine();
        
		/* Encapsulate user input in a Datagram Packet using DatagramPacket
		 * for DatagramPacket you need Parameters:
		 * send packet. 
		 * data.length = packet length.
		 * address = destination address (IP and port).
		 */
		DatagramPacket packet = new DatagramPacket(typing.getBytes(), typing.getBytes().length, new InetSocketAddress(ipAddress, sendPort));
        
        // Send the packet using DatagramSocket Initiated object
        udpSocket.send(packet);
		
        // Close the DatagramSocket
        udpSocket.close();
        
        // Call listenToServer to listen to incoming messages from the server
        listenToServer();
    }
    
	/**
	 * The listenToServer method listen to the client port for incoming messages from the server
	 * @throws IOException
	 */
	private void listenToServer() throws IOException {
		// Initiating the Datagram Socket on receive port
        DatagramSocket udpSocket = new DatagramSocket(recvPort);
		
		byte[] buf = new byte[256];
		/* Initiating DatagramPacket - Parameters are:
		 * 1-buffer for holding the incoming datagram.
		 * 2-length the number of bytes to read.
		 */
		DatagramPacket packet = new DatagramPacket(buf, buf.length);
        
        // Fetch the packet data using DatagramSocket object receive method
        udpSocket.receive(packet);
        
        // Print the message contents
        String msg = new String(packet.getData()).trim();
        System.out.println("Message from Server: " + msg);
        
        // Close the DatagramSocket
        udpSocket.close();
	}

	public static void main(String[] args) throws Exception {
		// set the client address (IP) and send/receive ports
		System.out.println("-- Running UDP Client at " + InetAddress.getLocalHost() + " --");
		InetAddress ipAddress = InetAddress.getLocalHost();  // local IP address
		int sendPort = 7077; // use to send datagram out to server
		int recvPort = 7076; // use to listen to datagram sent from server
		UDPClient client = new UDPClient(ipAddress, sendPort, recvPort);
		client.start();
	}
}
