package me.chin.stomp.controller;

import com.alibaba.fastjson.JSONObject;
import me.chin.stomp.pojo.message.Request;
import me.chin.stomp.pojo.message.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.util.HtmlUtils;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by Allen on 2018/8/24.
 */
@Controller
public class HelloController {
    @Autowired
    private SimpMessagingTemplate simpMessagingTemplate;

    @MessageMapping("/hello")
    @SendTo("/topic/greetings")
    public Response greeting(Request message) throws Exception {
        Thread.sleep(1000); // simulated delay
        return new Response("Hello, " + HtmlUtils.htmlEscape(message.getName()) + "!");
    }

    /**
     * 主动发送消息
     * @return
     */
    @RequestMapping(value="/send")
    @ResponseBody
    public String send(){
        Response response = new Response("Hello Stranger!");
        String jsonString = JSONObject.toJSONString(response);
        //Send message to anyone who has subscribe this "topic": stompClient.subscribe('/topic/greetings', function (data) {});  ---> code in app.js
        Map<String, Object> header = new HashMap<>();
        // can not cover an exist header(header:subscription will not be changed!)
        header.put("subscription", "sub-0XXX");
        header.put("not exit", "sub-0XXX");
        simpMessagingTemplate.convertAndSend("/topic/greetings", jsonString, header);
//        simpMessagingTemplate.convertAndSendToUser("sub-0","/topic/greetings", jsonString);
        return "OK";
    }
}
