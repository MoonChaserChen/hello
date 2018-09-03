package me.chin.stomp.config;

import me.chin.stomp.pojo.UserPrincipal;
import org.springframework.context.annotation.Configuration;
import org.springframework.messaging.Message;
import org.springframework.messaging.MessageChannel;
import org.springframework.messaging.simp.config.ChannelRegistration;
import org.springframework.messaging.simp.config.MessageBrokerRegistry;
import org.springframework.messaging.simp.stomp.StompCommand;
import org.springframework.messaging.simp.stomp.StompHeaderAccessor;
import org.springframework.messaging.support.ChannelInterceptorAdapter;
import org.springframework.messaging.support.MessageHeaderAccessor;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.web.socket.config.annotation.EnableWebSocketMessageBroker;
import org.springframework.web.socket.config.annotation.StompEndpointRegistry;
import org.springframework.web.socket.config.annotation.WebSocketMessageBrokerConfigurer;

import java.security.Principal;

/**
 * Created by Allen on 2018/8/24.
 */
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {

    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        // enable a simple memory-based message broker to carry the greeting messages back to the client on destinations prefixed with "/topic"

        config.enableSimpleBroker("/topic"); // enable simple broker
        //config.enableStompBrokerRelay("/topic", "/queue"); // use stomp broker relay

        // "/app/hello" is the endpoint that the HelloController.greeting() method is mapped to handle.
        // stompClient.send("/app/hello", {}, "message") will be send to HelloController.greeting(). code in app.js.
        // stompClient.send(ApplicationDestinationPrefixes + @MessageMapping, ...)
        config.setApplicationDestinationPrefixes("/app");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/gs-guide-websocket").withSockJS();
    }

    @Override
    public void configureClientInboundChannel(ChannelRegistration registration) {
        registration.setInterceptors(new ChannelInterceptorAdapter() {
            @Override
            public Message<?> preSend(Message<?> message, MessageChannel channel) {
                StompHeaderAccessor accessor = MessageHeaderAccessor.getAccessor(message, StompHeaderAccessor.class);
                if (StompCommand.CONNECT.equals(accessor.getCommand())) {
                    LinkedMultiValueMap nativeHeaders = (LinkedMultiValueMap) message.getHeaders().get("nativeHeaders");
                    String userId = (String) nativeHeaders.getFirst("userId"); // access authentication header(s)
                    Principal user = new UserPrincipal(userId);
                    accessor.setUser(user);
                }
                return message;
            }
        });
    }
}