package UDPSocket;
import java.io.*;
import java.net.*;

/**
 * This program demonstrates a UDP server
 * @author jl922223
 * @version 1.0
 * @since 2020-12-12
 */

public class UDPServer {
	/**
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		// set the client address (IP) and send/receive ports
		InetAddress serverIP = InetAddress.getLocalHost(); // local IP address
		int sendPort = 7076;
		int recvPort = 7077;
			
		// Set the client address (IP) and send/receive ports from user input (in case you export the program as JAR)
		if (args.length > 0) {
			serverIP = InetAddress.getByName(args[0]);
			sendPort = Integer.parseInt(args[1]);
			recvPort = Integer.parseInt(args[2]);
		}
		
		new UDPServer().start(serverIP, sendPort, recvPort);
	}
 
	/**
	 * Starts the UDP server with 2 threads (Send Thread and Receive Thread)
	 * @param serverIP
	 * @param sendPort
	 * @param recvPort
	 * @throws SocketException
	 */
	private void start(InetAddress serverIP, int sendPort, int recvPort) throws SocketException {
		// Initiating the server Send Thread
		ServerSendThread send = new ServerSendThread(serverIP, sendPort);
		new Thread(send).start();
		
		// Initiating the server Receive Thread
		ServerRecvThread receive = new ServerRecvThread(recvPort);
		new Thread(receive).start();
	}
	
	/**
	 * ServerSendThread class for server sending messages
	 */
	class ServerSendThread implements Runnable {
	    private InetAddress serverAddress;
	    private int sendPort;
	    
		/**
		 * ServerSendThread constructor
		 * 
		 * @param serverIP
		 * @param sendPort
		 * @throws SocketException
		 */
		public ServerSendThread(InetAddress serverIP, int sendPort){
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
		 * sendMsg method send messages to client socket
		 * @throws IOException
		 */		
		void sendMsg() throws IOException {
			System.out.println("-- Running UDP Server at " + InetAddress.getLocalHost() + " --");
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

		/**
		 * sendMsgBack method can be called to respond to a client message
		 * @param msgToUpperCase
		 * @throws IOException
		 */
		public void sendMsgBack(String msgToUpperCase) throws IOException {
			//Initiating DatagramSocket and DatagramPacket similar to sendMsg method
			DatagramSocket udpSocket = new DatagramSocket();
			DatagramPacket pkt = new DatagramPacket(msgToUpperCase.getBytes(), msgToUpperCase.getBytes().length, new InetSocketAddress(serverAddress, sendPort));
		}
	}
 
	
	/**
	 * ServerRecvThread class for server messages receiving
	 */
	class ServerRecvThread implements Runnable {
	    private int recvPort;
	    
	    
		/**
		 * ServerRecvThread constructor
		 * @param recvPort
		 */ 
		public ServerRecvThread(int recvPort) {
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
		 * recvMsg method listen to the server socket for messages sent from client
		 * @throws IOException
		 */
		void recvMsg() throws IOException {
			// add your code to complete this method
			// Listen to the server receive port for new messages from client
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
				System.out.printf("Received client [IP:%s] message: %s %n", dpacket.getAddress().getHostAddress(), msg);
	
			// Close the DatagramSocket
				udpSocket.close();

			
			// Send response to client using ServerSendThread class and sendMsgBack message
				ServerSendThread send = new ServerSendThread(dpacket.getAddress(), 7076);
				send.sendMsgBack(msg.toUpperCase());
			}
		}
	}
}
