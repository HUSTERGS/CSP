# CSP

一部分CCF-CSP 的拉跨代码 Python版本 持续更新?



由于是在测试时运行，所以部分题目必然超时，可以尝试使用C/C++重写进行验证。其中[note.md](https://github.com/HUSTERGS/CSP/blob/master/note.md)为刷题过程中遇到的一些小的知识点。


:x: 错误    :hourglass: 超时   :heavy_check_mark: 正确 :warning: 运行时错误

|        | 第一题 | 第二题 | 第三题    | 第四题    | 第五题   |
| ------ | ------ | ------ | --------- | --------- | -------- |
| 202006 | :heavy_check_mark: | 60:hourglass: |  | 3​2:hourglass: |  |
| 201912 | :heavy_check_mark:    | :heavy_check_mark:    | 90 :hourglass: |           | 20 :hourglass: |
| 201909 | :heavy_check_mark:    | :heavy_check_mark:    | 40 :hourglass: | 20 :hourglass: |          |
| 201903 | :heavy_check_mark:    | :heavy_check_mark:    | 20 :x: | 80 :hourglass: | 0 :hourglass: |
| 201812 | :heavy_check_mark:    | :heavy_check_mark:    | 80 :hourglass: | :heavy_check_mark: |          |
| 201809 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark: | 70 :hourglass: | 10 :hourglass: |
| 201803 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark:       |           |          |
| 201712 | :heavy_check_mark:    | :heavy_check_mark:    | 10 :hourglass: |           |          |
| 201709 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark:       | 75 :hourglass: | 30 :hourglass: |
| 201703 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark:       | 80 :hourglass: |          |
| 201612 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark:       |           |          |
| 201609 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark:       | 0 :x: |          |
| 201604 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark:       | 10:hourglass: |          |
| 201512 | :heavy_check_mark:    | :heavy_check_mark:    | 90 :hourglass: | :heavy_check_mark: |          |
| 201509 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark:       | :heavy_check_mark: |          |
| 201503 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark:       | :heavy_check_mark: |          |
| 201412 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark: | :heavy_check_mark: |          |
| 201409 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark:       | 70 :hourglass: |          |
| 201403 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark:       | :heavy_check_mark: |          |
| 201312 | :heavy_check_mark:    | :heavy_check_mark:    | :heavy_check_mark:       | :heavy_check_mark: |          |


#### 为何使用Python

1. 本人C/C++/Java太菜
2. Python内置大数，不用担心溢出问题
3. 字符串处理非常给力

#### 为何不建议使用Python

1. 某些夏令营/复试 机试可能不支持Python，但是必定支持C/C++
2. Python运行时间着实不太行，虽然实际考试时的内存以及时间限制均为C/C++的十倍
3. 大多数算法相关的书籍以及网上找到的题解均为C/C++，而Python和Java较少
4. Python存在下述递归问题

#### Tips
1. 建议了解的包

   - `heapq`
   - `collections`
   - `itertools`
   - `re`

2. python递归层数极限为1000，可使用`sys.setrecursionlimit(100000)`提升到4000左右，再高需要改为非递归算法，递归爆栈时会显示**运行错误**。

   > 来自[该仓库](https://github.com/soyan1999/ccf-csp-python)

更多tips可以查看本人[相关博客](https://hustergs.github.io/categories/Programming-Language/Python/)



### 相关仓库

- [ccf-csp-python](https://github.com/soyan1999/ccf-csp-python) Python 帮助很大
- [CCF-CSP-and-PAT-solution](https://github.com/richenyunqi/CCF-CSP-and-PAT-solution)  C++





