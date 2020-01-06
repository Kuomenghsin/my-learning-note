Linked list(連結串列)是一種常見的資料結構，其使用node(節點)來記錄、表示、儲存資料(data)，並利用每個node中的pointer指向下一個node，
藉此將多個node串連起來，形成Linked list，並以NULL來代表Linked list的終點
若實際打開每個node的內部，至少會包含(1)data來代表資料，與(2)pointer指向下一個node，見圖一(b)：

Node1：
以int的data，記錄正整數7。
本身的記憶體位置為0x1001042f0。
以「node之pointer」，記錄(指向)下一個node之記憶體位置(0x100104300)。
Node2：
以int的data，記錄正整數3。
本身的記憶體位置為0x100104300。
由於在Node1中的「node之pointer」指向了Node2之記憶體位置，因此，便能夠經由Node1「找到」Node2。
以「node之pointer」，記錄(指向)下一個node之記憶體位置(0x100104310)。
Node3：
以int的data，記錄正整數14。
本身的記憶體位置為0x100104310。
由於在Node2中的「node之pointer」指向了Node3之記憶體位置，因此，便能夠經由Node2「找到」Node3。
以「node之pointer」，記錄(指向)NULL，表示Linked list的最後一個node。
通常在面對一個Linked list時，能夠公開存取(access)的node只有「第一個node」，以ListNode *first表示，
不過因為node中有pointer記錄下一個node的記憶體位置
，便能夠讀取下一個node的data與pointer，換句話說，有了node中的pointer就可以在Linked list中「移動(traversal)」，
更進一步，便能進行諸如「新增節點」、「刪除節點」、「印出Linked list」等等的資料處理，這些函式將在後續文章一一介紹。




以兩個class(類別)表示Linked list
若以C++的class(類別)來實作Linked list，可以利用兩個class，使得node的資料不會被任意更動(也就是封裝(Encapsulation)的概念)。
使用struct來代表node也是常見的做法，差別在於，struct的資料成員(data member)一定是公開的(public)。

class ListNode的private data有兩項，一項代表著資料項目(在此以int示範)，一項是「指向型別(type)為ListNode之指標」，
以ListNode *next表示，用來記錄「下一個node」的記憶體位置。

在class LinkedList的private data中，最基本一定會有代表「第一個node」的ListNode *first，其餘資料項目可以視情況增加
，像是int size用來記錄Linked list的長度等等。
