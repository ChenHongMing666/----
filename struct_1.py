class ParaPositonNotRightError (Exception):
        
    """创建一个异常来处理Screen对象中showPara参数传递不正确"""

    def __init__(self, errorPos : str) -> None:

        """
        __init__(self, errorPos) -> None \n 
        此函数用于传递错误的位置参数 \n 
        errorPos : 错误的位置参数
        """

        self.filename = __file__ # __file__ 变量存储了该文件的名称及路径
        self.errorPos = errorPos
        

    def __str__(self,) -> str:

        """
        __str__(self) -> str \n 
        此函数用于返回错误信息
        """

        return f"File {self.filename} , Position {self.errorPos} is not correct. But we have 'left' , 'center' and 'right' ."




class Screen :

    """此类描述了一个字符输出的区域且提供了字符输出的方法"""

    def __init__(self, width : int , hight :int ) -> None:

        """
        __init__(self, width : int , hight :int ) -> None \n
        此函数为屏幕对象的初始化函数\n
        width : 屏幕显示字符的宽度\n
        hight : 屏幕显示字符的高度\n
        空返回值
        """

        self.width = width
        self.hight = hight


    def setWide(self , newWidth : int ) -> None :

        """
        setWide(self , newWidth : int ) -> None \n
        此函数为重设屏幕宽度的函数\n
        newWidth : 新的宽度\n
        空返回值
        """

        self.width = newWidth


    def setHight(self , newHight : int ) -> None :

        """
        setHight(self , newHight : int ) -> None \n
        此函数为重设屏幕高度的函数\n
        newHight : 新的高度\n
        空返回值
        """

        self.hight = newHight


    def showPara(self , *text : str , pos="left" , fillchar=" ") -> None :

        """
        showPara(self , *text : str ) -> None \n
        此函数为让字符以段落的形式呈现\n
        *text    : 接受所有的实参,并逐一输出 \n
        pos      : 字符显示的位置 \n
        fillchar : 空白部分填充的字符 \n
        空返回值
        """

        for line in text :

            if pos == "left" :
                outText = line.ljust(self.width , fillchar)
            
            elif pos == "right" :
                outText = line.rjust(self.width , fillchar)
            
            elif pos == "center" :
                outText = line.center(self.width , fillchar)
            
            else :
                raise ParaPositonNotRightError(pos)

            input(outText)
    

    def _listToStr(self , inlist : list) -> str:

        """
        _listToStr(self , inlist : list) -> str \n
        此函数为辅助方法, 将输入的列表转化为字符串 \n 
        inlist : 输入的列表 \n 
        返回应的字符串
        """

        outText = ""

        for line in inlist :
            outText += line + "\n"
        
        return outText



    def bigChar(self , charlib : dict[ str , str ], chars : str ) -> None:

        """
        bigChar(self , charlib : dict[ str , str ], chars : str ) -> None \n
        此函数为标题大字输出器,支持高位5的英文字母 \n 
        charlib : 大字的索引表 \n 
        chars   : 要输出的字或句 \n
        返回一个长字符串
        """

        outText = [ "" for line in range(5) ]

        for char in chars :
            bigCharTemp = charlib[char].split("\n")
            for line in range(5) :
                outText[line] += bigCharTemp[line]

        return self._listToStr(outText)

    


#此为程序入口,__name__变量是一个特殊变量,只有当该文件为主文件运行时,__name__ 为 __main__, 类似于c++中的 int main
if __name__ == "__main__" :

    charlib = {
        "h":
        """*     *   
*     *   
*******   
*     *   
*     *   
"""
    }

    screen = Screen(100 , 20)
    print(screen.bigChar(charlib , "hh"))
