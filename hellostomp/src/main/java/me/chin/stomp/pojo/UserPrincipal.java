package me.chin.stomp.pojo;

import javax.security.auth.Subject;
import java.security.Principal;

/**
 * Created by Allen on 2018/9/3.
 */
public class UserPrincipal implements Principal {
    private String name;

    public UserPrincipal(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public boolean implies(Subject subject) {
        return false;
    }
}
