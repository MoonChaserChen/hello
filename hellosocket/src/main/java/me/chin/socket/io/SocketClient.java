package me.chin.socket.io;

import me.chin.socket.MessageBuilder;
import org.apache.commons.lang3.RandomUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.Socket;

/**
 * Created by Allen on 2018/9/4.
 */
public class SocketClient {
    protected static final Logger logger = LoggerFactory.getLogger(SocketClient.class);

    public static void main(String[] args) throws IOException {
        Socket client = new Socket(SocketServer.HOST, SocketServer.PORT);
        // client.setSoTimeout(10000);
        new Thread(new MessageSender(client)).start();
        new Thread(new MessageReceiver(client)).start();
    }

    private static class MessageSender implements Runnable {
        private Socket client;

        public MessageSender(Socket client) {
            this.client = client;
        }

        @Override
        public void run() {
            try {
                PrintStream out = new PrintStream(client.getOutputStream());
                // BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
                boolean stopFlag = false;
                while (!stopFlag) {
                    // String message = input.readLine();
                    String message = MessageBuilder.getRandomMessage("Client-");
                    out.println(message);
                    if ("BYE".equalsIgnoreCase(message)) {
                        stopFlag = true;
                    }
                    long sleepTime = 1000 * RandomUtils.nextInt(5, 15);
                    logger.info("===== sleep = {}", sleepTime);
                    Thread.sleep(sleepTime);
                }
            } catch (IOException | InterruptedException e) {
                e.printStackTrace();
            } finally {
                try {
                    client.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    private static class MessageReceiver implements Runnable {
        private Socket client;

        public MessageReceiver(Socket client) {
            this.client = client;
        }

        @Override
        public void run() {
            try {
                BufferedReader br = new BufferedReader(new InputStreamReader(client.getInputStream()));
                while (true) {
                    String info = br.readLine();
                    logger.debug("===== Client receive message: " + info);
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
