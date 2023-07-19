import xlrd
import pandas as pd


class OptCsv():

    def read_excel(self, path, sheet):
        """
        传入读取文件的地址
        返回xlsx文件中的数据，格式[{},{}]，每行对应一个map
        """

        # 打开文件
        workbook = xlrd.open_workbook(path)
        # 获取所有的sheet
        #sheet_name = workbook.sheet_names(sheet)
        sheet_name = workbook.sheet_by_name(sheet)

        # 根据sheet索引得到sheet内容
        sheet = workbook.sheet_by_index(0)
        print(sheet.name, sheet.nrows, sheet.ncols)
        # 获取整行或者整列内容
        rows = sheet.row_values(0) #查看第二行，第一行是标题
        #cols = sheet.col_values(2)
        
        res = []

        for rown in range(1, sheet.nrows):
            rowdata = sheet.row_values(rown)
            table = {}
            for i in range(len(rowdata)):
                table[rows[i]] = rowdata[i]
            res.append(table)

        print('-' * 20)
        print(res)
        print('-' * 20)
        return res

    def InsertdataCsv(self, data, path, sheet):
        """ReadCsv.py
            更新文件，参数为文件路径path,以及data。
            data是一个list,里面嵌套的是map        
        """
        print(data)
        df = pd.read_excel(path)
        
        exampledata = data[0]
        keys = exampledata.keys()
        keylist = []
        for k in (keys):
            keylist.append(k)
        valuelist = []
        for i in range(len(data)):
            mapdata = data[i]
            values = mapdata.values()
            templist = []
            for v in values:
                templist.append(v)
            valuelist.append(tuple(templist))

        dataframe = pd.DataFrame(valuelist, columns=keylist)
        df_new = df.append(dataframe, ignore_index=True)
        df_new.to_excel(path,sheet_name=sheet,index=False,engine="openpyxl")

    def UpdataCsv(self, data, path, sheet):
        """ReadCsv.py
        更新现有xlsx数据中的某一行数据，根据data传来的设备管理序号来进行更新
        """
        df = pd.read_excel(path)
        exampledata = data[0]
        keys = exampledata.keys()
        keylist = []
        for k in (keys):
            keylist.append(k)

        for tempdata in data:
            index_num = tempdata['设备管理序号']
            df.loc[index_num] = tempdata
        
        df.to_excel(path,sheet_name=sheet,index=False,header=True)


if __name__ == '__main__':
    opt = OptCsv()
    path = 'test.xlsx'
    res = opt.read_excel(path, sheet='sheet1')
    data = [{'设备管理序号': 5.0, '设备概要': '有', '库存': 200.0, '存放地点': '北京', '备注': '无'},
            {'设备管理序号': 6.0, '设备概要': '无', '库存': 150.0, '存放地点': '北京', '备注': '无'}]
    #opt.InsertdataCsv(data,path)
    #opt.UpdataCsv(data,path,sheet='sheet1')
    #print("done")
