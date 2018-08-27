package me.allen.websocket.pojo.message;

import javax.websocket.server.ServerEndpoint;

/**
 * Created by Allen on 2018/8/24.
 */
@ServerEndpoint("")
public class Request {
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
