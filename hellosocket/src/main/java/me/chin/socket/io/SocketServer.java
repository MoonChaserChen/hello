package me.chin.socket.io;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Created by Allen on 2018/9/4.
 */
public class SocketServer {
    protected static final Logger logger = LoggerFactory.getLogger(SocketServer.class);

    public static final String UTF8 = "UTF-8";
    public static final String HOST = "127.0.0.1";
    public static final String GOOD_BYE_MESSAGE = "BYE";
    public static final int PORT = 20000;

    public static void main(String[] args) {
        try {
            ServerSocket server = new ServerSocket(SocketServer.PORT);
            while(true) {
                Socket client = server.accept();
                new Thread(new ServerHandler(client)).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static class ServerHandler implements Runnable {
        private Socket client;

        public ServerHandler(Socket client) {
            this.client = client;
        }

        @Override
        public void run() {
            try {
                PrintStream out = new PrintStream(client.getOutputStream());
                 BufferedReader buf = new BufferedReader(new InputStreamReader(client.getInputStream()));
                boolean stopFlag = false;
                while (!stopFlag) {
                    String message = buf.readLine();
                    logger.debug("===== Server receive message: " + message);
                    out.println("hello, " + message);
                    stopFlag = GOOD_BYE_MESSAGE.equalsIgnoreCase(message);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }finally {
                try {
                    client.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
