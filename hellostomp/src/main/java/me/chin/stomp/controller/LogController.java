package me.chin.stomp.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import java.security.Principal;

/**
 * Created by Allen on 2018/9/3.
 * HttpServletRequest#login不是这种用法
 */
@RestController
public class LogController {
    @RequestMapping(value="/login")
    public String login(HttpServletRequest request) {
        try {
            request.login("my_username", "my_password");
        } catch (ServletException e) {
            e.printStackTrace();
        }
        return "OK";
    }

    @RequestMapping(value="/logout")
    public String logout(HttpServletRequest request) {
        try {
            request.logout();
        } catch (ServletException e) {
            e.printStackTrace();
        }
        return "OK";
    }

    @RequestMapping(value="/getUserInfo")
    public String getUserInfo(HttpServletRequest request) {
        String remoteUser = request.getRemoteUser();
        System.out.println("===== remoteUser = " + remoteUser);
        Principal userPrincipal = request.getUserPrincipal();
        if (userPrincipal != null) {
            String name = userPrincipal.getName();
            System.out.println("===== name = " + name);
        }
        return "OK";
    }
}
