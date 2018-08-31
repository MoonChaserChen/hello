package me.chin.stomp.pojo.message;

/**
 * Created by Allen on 2018/8/24.
 */
public class Response {
    private String content;

    public Response(String content) {
        this.content = content;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
}
