静态分析：针对每笔交易的合约进行静态手工分析，序号对应交易的地址，及相关合约源码存储路径见**analysis\static-analysis-results\手动逐合约分析-ERC20-信息排序.csv**。

# 1
这是一个接口合约，声明了很多接口方法，首先是ConfigInterface接口类，其次是TokenInterface接口类，然后是TokenSalesInterface接口类，这些接口类只有方法声明，没有方法定义。

后面是Badge类和Token类，这两个类有具体实现.

Badge类 
- 总变量访问次数：83  
    ifOwner(2) + Badge(2) + safeToAdd(2) + addSafely(3) + safeToSubtract(2) + subtractSafely(2) + balanceOf(2) + transfer(19) + transferFrom(28) + approve(9) + mint(10) + setOwner(2)
- 有效变量访问次数（排除了辅助函数中的一些参数设定）：74  
    ifOwner(2) + Badge(2) + balanceOf(2) + transfer(19) + transferFrom(28) + approve(9) + mint(10) + setOwner(2)
- 状态变量访问次数：33  
    ifOwner(2) + Badge(2) + balanceOf(1) + transfer(9) +  transferFrom(11) + approve(3) + mint(4) + setOwner(1)

===> 状态变量访问率：33/70*100% = 47.14% 

Token类
- 总变量访问次数：  114
    ifSales(2) + ifOwner(2) + ifDao(2) + Token(9) + safeToAdd(2) + addSafely(3) + safeToSubtract(2) + balanceOf(2) + transfer(19) + transferFrom(19) + approve(9) + allowance(4) +  mint(8) + mintBadge(3) + registerDao(4) + setDao(2) + isSeller(2) + registerSeller(2) + unregisterSeller(2) + setOwner(6)

- 有效变量访问次数（排除了辅助函数中的一些参数设定）：107
    ifSales(2) + ifOwner(2) + ifDao(2) + Token(9) + balanceOf(2) + transfer(19) + transferFrom(19) + approve(9) + allowance(4) + mint(8) + mintBadge(3) + registerDao(4) + setDao(2) + isSeller(2) + registerSeller(2) + unregisterSeller(2) + setOwner(6)

- 状态变量访问次数：50
    ifSales(2) + ifOwner(2) + ifDao(2) + Token(5) + balanceOf(1) + transfer(9) + transferFrom(11) + approve(3) + allowance(1) + mint(4) + mintBadge(1) + registerDao(3) + setDao(1) + isSeller(1) + registerSeller(1) + unregisterSeller(1) + setOwner(2)

===> 状态变量访问率：50/107*100% = 46.73%


# 2 
