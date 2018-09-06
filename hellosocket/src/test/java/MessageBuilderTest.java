import me.chin.socket.MessageBuilder;
import org.junit.Test;

/**
 * Created by Allen on 2018/9/4.
 */
public class MessageBuilderTest {
    @Test
    public void testBuild(){
        System.out.println(MessageBuilder.getRandomMessage("Client-"));
    }
}
