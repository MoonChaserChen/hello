package me.chin.socket;

import org.apache.commons.lang3.RandomStringUtils;

/**
 * Created by Allen on 2018/9/4.
 */
public class MessageBuilder {
    public static final int MESSAGE_LEN = 10;
    public static String getRandomMessage(String prefix) {
        return prefix + RandomStringUtils.randomAlphabetic(10);
    }
}
