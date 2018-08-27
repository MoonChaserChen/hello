package me.allen.websocket.config;

import org.springframework.context.ApplicationListener;
import org.springframework.context.annotation.Configuration;
import org.springframework.messaging.simp.stomp.StompHeaderAccessor;
import org.springframework.web.socket.messaging.SessionConnectedEvent;

import java.util.List;

/**
 * Created by Allen on 2018/8/24.
 */
@Configuration
public class MySessionConnectedEvent implements ApplicationListener<SessionConnectedEvent> {
    @Override
    public void onApplicationEvent(SessionConnectedEvent event) {
        System.out.println("===== " + event.toString());
//        StompHeaderAccessor headers = StompHeaderAccessor.wrap(event.getMessage());
        StompHeaderAccessor headers = StompHeaderAccessor.wrap(event.getMessage());
        Object my_key1 = headers.getHeader("my_key");
        System.out.println("=====" + my_key1);
        String my_key = headers.getFirstNativeHeader("my_key");
        System.out.println("=====" + my_key);
        List<String> my_user = headers.getNativeHeader("my_key");
        System.out.println("=====" + my_user.get(0));
    }
}
