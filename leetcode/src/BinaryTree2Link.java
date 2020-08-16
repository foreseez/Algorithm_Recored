import javax.xml.soap.Node;
//https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/
public class BinaryTree2Link {


    /*
    *
    * 将排序二叉树转化为双向链表
    *
    *
    * */

    Node pre, head;

    public Node treeToList(Node root) {
        if (root == null)
            return null;
        dfs(root);
        head.left = pre;
        pre.right = head;
        return head;
    }

    void dfs(Node cur) {
        if (cur == null)
            return;
        if (pre != null)
            pre.right = cur;
        else
            head = cur;

        cur.left = pre;
        pre = cur;
        dfs(cur.right);
    }
}
