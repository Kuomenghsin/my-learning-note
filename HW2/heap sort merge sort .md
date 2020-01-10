Heap Sort (堆積排序法)

利用在資料結構中二元樹的堆積樹來做資料排序，以改善選擇排序需要做的執行次數。

其中堆積樹又區分為 Max-heap、Min-heap、Min-max heap 及 Deap 四種，

一般我們要做 heap sort 的時候拿Max-heap 或 Min-heap 來用就可以了 ( 取決於你想要從大排到小，還是從小排到大 )。

堆積樹(Heap Tree)：又叫堆、累堆 二元樹的一種 ⇒ 每個父節點最多兩個子節點 堆積樹為完全二元樹(Complete Binary Tree)的一種 

最小堆積(Min Heap)：父節點的值小於子節點 樹根(root)一定最所有節點的最小值

最大堆積(Max Heap)：父節點的值大於子節點 樹根(root)一定最所有節點的最大值 

兄弟節點的大小不重要 堆積排序法為選擇排序法的改良

Max Heap 將數列轉換成Max Heap 排序 (最大堆積樹(Max Heap)的樹根一定是最大值) 

將樹根(最大值)與最後一個節點調換，將最後一個節點(原樹根)取出，並加入已排序數列 

相當於對Max Heap Tree作Delete MaxNode 對整棵樹重新調整為最大堆積樹 ⇒ 調整後樹根為Max Node

Min Heap 將數列轉換成Min Heap 排序 (最小堆積樹(Min Heap)的樹根一定是最小值) 

將樹根(最小值)與最後一個節點調換，將最後一個節點(原樹根)取出，並加入已排序數列 

相當於對Min Heap Tree作Delete MinNode 對整棵樹重新調整為最小堆積樹 ⇒ 調整後樹根為Min Node

合併排序法(歸併排序法)的概念 將2個已排序的陣列合併，只需要N次比對的線性時間(Linear Time) 

比對次數最多為：左子數列長度 + 右子數列長度 - 1 將數列分成左、右子數列，分別對其作排序及合併 

合併排序作法： 將數列對分成左子數列、右子數列 分別對左子數列、右子數列作上一個步驟 ⇒ 遞迴(Recursive) 直到左子數列、

右子數列被分割成只剩一個元素為止 將僅剩的一個元素作為遞迴的結果回傳 對回傳的左子數列、

右子數列依大小排列合併 將合併的結果作為遞迴的結果回傳 

合併作法：：將左子數列及右子數列依大小合併成一個新的數列

若左子數列的數值都已填到新的數列 ⇒ 將右子數列中未填過的最小值填入新數列

若右子數列的數值都已填到新的數列 ⇒ 將左子數列中未填過的最小值填入新數列 將左子數列及右子數列中，

未填過的最小值填到新的數列 需執行⌈log 2n⌉回合 時間複雜度(Time Complexity)

Best Case：Ο(n log n)

Worst Case：Ο(n log n)

Average Case：Ο(n log n)

T(n) = MergeSort(左子數列) + MergeSort(右子數列) + Merge

 = T(n/2) + T(n/2) + c×n = O(n log2n)
 
空間複雜度(Space Complexity)：Ο(n)

需要暫時性的暫列存放每回合Merge後的結果 穩定性(Stable/Unstable)：穩定(Stable)
