package UDPSocket;
import java.io.*;
import java.net.*;

/**
 * This program demonstrates a UDP client
 * @author at015244
 * @version 1.0
 * @since 2020-12-12
 */

public class UDPClient {
	/**
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		// set the client address (IP) and send/receive ports
		InetAddress serverIP = InetAddress.getLocalHost(); // local IP address
		int sendPort = 7077;
		int recvPort = 7076;
		
		// Set the client address (IP) and send/receive ports from user input (in case you export the program as JAR)
		if (args.length > 0) {
			serverIP = InetAddress.getByName(args[0]);
			sendPort = Integer.parseInt(args[1]);
			recvPort = Integer.parseInt(args[2]);
		}
		
		new UDPClient().start(serverIP, sendPort, recvPort);
	}
 
	/**
	 * Starts the UDP client with 2 threads (Send Thread and Receive Thread)
	 * @param serverIP
	 * @param sendPort
	 * @param recvPort
	 * @throws SocketException
	 */
	private void start(InetAddress serverIP, int sendPort, int recvPort) throws SocketException {
		// Initiating the Client Send Thread
		ClientSendThread send = new ClientSendThread(serverIP, sendPort);
		new Thread(send).start();
		
		// Initiating the Client Receive Thread
		ClientRecvThread receive = new ClientRecvThread(recvPort);
		new Thread(receive).start();
		// add your code here
	}
 	
	/**
	 * ClientSendThread class for client sending messages
	 */
	class ClientSendThread implements Runnable {
	    private InetAddress serverAddress;
	    private int sendPort;
	    
		/**
		 * ClientSendThread constructor
		 * 
		 * @param serverIP
		 * @param sendPort
		 * @throws SocketException
		 */
		public ClientSendThread(InetAddress serverIP, int sendPort) throws SocketException {
	        serverAddress = serverIP;
	        this.sendPort = sendPort;
		}

		
		/**
		 * When an object implementing interface Runnable is used to create a thread,
		 * starting the thread causes the object's run method to be called in that separately executing thread. 
		 */
		@Override
		public void run() {
			try {
				sendMsg();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		/**
		 * sendMsg method send messages to server socket
		 * @throws IOException
		 */
		void sendMsg() throws IOException {
			System.out.println("-- Running UDP Client at " + InetAddress.getLocalHost() + " --");
			System.out.println("Enter message >");
			
			// Initiating the Datagram Socket 
			DatagramSocket udpSocket = new DatagramSocket();
			String input = "";

			// Listen to user input and encapsulated in a Datagram Packet
			do{
				// Take user input using e.g, BufferedReader
				BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
				input = br.readLine();

				/* Encapsulate user input in a Datagram Packet using DatagramPacket
				 * for DatagramPacket you need Parameters:
				 * send packet. 
				 * data.length = packet length.
				 * address =e destination address.
				 */
	            DatagramPacket packet = new DatagramPacket(input.getBytes(), input.getBytes().length, new InetSocketAddress(serverAddress, sendPort));
				
	            // Send the packet using DatagramSocket Initiated object
				udpSocket.send(packet);
				
			} while(!input.equals("exit"));
			
			// Close the DatagramSocket
			udpSocket.close();
		}
	}
	
	
	/**
	 * ClientRecvThread class for client messages receiving
	 */
	class ClientRecvThread implements Runnable {
	    private int recvPort;
	    
		/**
		 * ClientRecvThread constructor
		 * @param recvPort
		 */
		public ClientRecvThread(int recvPort) {
	        this.recvPort = recvPort;
		}

		/**
		 * When an object implementing interface Runnable is used to create a thread,
		 * starting the thread causes the object's run method to be called in that separately executing thread. 
		 */
		@Override
		public void run() {
			try {
				recvMsg();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		/**
		 * recvMsg method listen to the client socket for messages sent from server
		 * @throws IOException
		 */
		void recvMsg() throws IOException { 
			// add your code to complete this method
			// Listen to the client receive port for new messages from server 
			String msg;
			while(true) {
			
			// Initiating the Datagram Socket on receive port
				DatagramSocket udpSocket = new DatagramSocket(recvPort);
				
				byte[] buf = new byte[1024];
			
			/* Initiating DatagramPacket - Parameters are:
			 * 1-buffer for holding the incoming datagram.
			 * 2-length the number of bytes to read.
			 */
				DatagramPacket dpacket = new DatagramPacket(buf, buf.length);
			
			// Fetch the packet data using DatagramSocket object receive method
				udpSocket.receive(dpacket);
			
			// Print the message contents
				msg = new String(dpacket.getData()).trim();
				System.out.printf("Received server [IP:%s] message: %s %n", dpacket.getAddress().getHostAddress(), msg);

			// Close the DatagramSocket	
			udpSocket.close();
			}
		}
	}
}
