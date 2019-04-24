# LIST_learning1
# 剔除重复项的，导出查询数据的sql语句
SELECT distinct id,title,links,desc_contents  FROM List_learning1.java1 into outfile "/home/lk/Recoding_Java1/all_java.xls" ;
