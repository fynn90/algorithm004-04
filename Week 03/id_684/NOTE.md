# NOTE



作业：使用二分查找，寻找一个半有序数组[4, 5, 6, 7, 0, 1, 2]中间无序的地方
说明：同学们可以将自己的思路、代码写在第3周的学习总结中

class Solution(object):

    def find_roate_index(self,nums):
        """
        寻找选择数组的分割点
        :param nums:
        :return:
        """
        if not nums:return 0
        left,right = 0 , len(nums) -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid -1]:
                return mid
            else:
                if nums[mid] < nums[right]:
                    right = mid -1
                else:
                    left = mid + 1
        return 0


一、广度优先搜索和深度优先搜索
1、广度优先搜索（breadth-first-search）是一种“地毯式”层层推进的搜索策略，即先查找离起始顶点最近的，然后是次近的，
依次往外搜索，属于盲目搜索。
2、﻿深度优先搜索（depth-first-search）沿着树的深度遍历树的节点，尽可能深的搜索树的分支。当节点v的所在边都己被探寻过，
搜索将回溯到发现节点v的那条边的起始节点。这一过程一直进行到已发现从源节点可达的所有节点为止。如果还存在未被发现的节点，
则选择其中一个作为源节点并重复以上过程，整个进程反复进行直到所有节点都被访问为止。属于盲目搜索。
3、时间复杂度和空间复杂度
﻿广度优先的时间复杂度是O(V+E),空间复杂度O(V+E)，V表示顶点的个数，E表示边的个数。
﻿深度优先搜索算法的时间复杂度是O(E)，E表示边的个数，空间复杂度是O(V)，V是顶点个数。

二、贪心算法
1、定义：贪心算法是指，在对问题求解时，总是做出在当前看来是最好的选择。 也就是说，不从整体最优上加以考虑，
他所做出的是在某种意义上的局部最优解。
2、使用贪心算法的情况：
1）针对一组数据，我们定义了限制值和期望值，希望从中选出几个数据，在满足限制的情况下，期望值最大。
2）每次选择当前情况下，在对限制值同等贡献量的情况下，对期望值贡献最大的数据。
3）大部分情况下，举几个例子验证一下就可以了。严格的证明贪心算法的正确性是非常复杂的，需要涉及较多的数学推理。
而且，从实践角度来说，大部分能用贪心算法解决的问题，贪心算法的正确性都是显而易见的，也不需要严格的数学推导证明。
实际上，用贪心算法解决问题的思路，并不总能给出最优解。

三、二分查找
1、什么是二分查找？
二分查找是针对一个有序的数据集合，每次通过跟区间中间的元素对比，将待查找的区间缩小为之前的一般，
直到找到要查找的元素，或者区间缩小为0。
2、实现二分查找注意事项：
1）循环退出的条件是：low <= high，不是low < high。
2）mid的取值，使用mid=low+(high-low)/2，而不是mid=(low+high)/2，因为如果low和high比较大的话，求和可能会发生int类型的值超出最大范围。
3）low 和 high 的更新：low = mid +1，high = mid + 1，若直接写成low = mid，high = mid就肯能发生死循环。
3、使用条件
1）二分查找依赖的是顺序表结构，即数组。
2）二分查找针对的是有序数据，因此只能用在插入、删除操作不频繁，一次排序多次查找的过程中。
3）数据量太小不适合二分查找，与直接遍历数组相比效率不明显。但是有一个例外，就是数据之间的比较操作非常耗时，
比如数组中存储的都是长度超过300的字符串，那这还是尽量减少比较 操作使用二分查找。
4）数据量太大也不适合二分查找，因为数组需要连续的空间，若数据量太大，往往找不到存储如此大规模数据的连续内存空间。



