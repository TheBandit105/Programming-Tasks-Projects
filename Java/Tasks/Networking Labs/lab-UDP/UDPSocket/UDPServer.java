package UDPSocket;
import java.io.IOException;
import java.net.*;

/**
 * This program demonstrates a UDP server
 * @author at015244
 * @version 1.0
 * @since 2020-12-12
 */
public class UDPServer {
    private int sendPort;
    private int recvPort;

    /**
     * @param serverPort
     * @param clientPort
     * @throws SocketException
     * @throws IOException
     */

    public UDPServer(int sendPort, int recvPort) throws SocketException, IOException {
        this.sendPort = sendPort;
        this.recvPort = recvPort;
    }
    /**
     * The start method listen to incoming messages from the client
     * @throws IOException
     */
    private void start() throws Exception {
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
        System.out.println("Message from Client: " + msg);

        // Close the DatagramSocket
        udpSocket.close();

        // send a reply to client
        replyToClient(packet.getAddress(), msg.toUpperCase());
    }

    /**
	 * The replyToClient method use to reply to client
     * @param clientAddress
     * @param msgtoUpperCase
     * @throws IOException
     */
    private void replyToClient(InetAddress clientAddress, String msgtoUpperCase) throws IOException {
    	// Initiate the Datagram Socket
		DatagramSocket udpSocket = new DatagramSocket();

		/* Encapsulate user input in a Datagram Packet using DatagramPacket
		 * for DatagramPacket you need Parameters:
		 * send packet.
		 * data.length = packet length.
		 * address = destination address (IP and port).
		 */
	   DatagramPacket packet = new DatagramPacket(msgtoUpperCase.getBytes(), msgtoUpperCase.getBytes().length, new InetSocketAddress(clientAddress, sendPort));

        // Send the packet using DatagramSocket Initiated object
        udpSocket.send(packet);
        // Close the DatagramSocket
        udpSocket.close();
	}

	public static void main(String[] args) throws Exception {
		// set the server address (IP) and send/receive ports
		System.out.println("-- Running UDP Server at " + InetAddress.getLocalHost() + " --");
		InetAddress ipAddress = InetAddress.getLocalHost();  // local IP address
		int sendPort = 7076; // use to send datagram out to server
		int recvPort = 7077; // use to listen to datagram sent from server
        UDPServer server = new UDPServer(sendPort, recvPort);
        server.start();
    }
}
