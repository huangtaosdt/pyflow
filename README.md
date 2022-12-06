# 项目名称
 类sql python链式操作

## 快速开始
目前仅支持python2  

### 处理tuple、list等iterable对象
```
>>> from common_utils.pyflow import seq
>>> seq([1, 2, 3]).map(lambda x: x+1).get() => [2, 3, 4] 
``` 

### 文件读取
seq.open(path, mode='r', encoding='utf8', n_limit=None, process_hint=None)
- path: 文件路径
- mode: 打开方式
- encoding: 编码
- n_limit: 读取行数；默认None, 即加载全部内容
- process_hint: 整型，表示每隔n行打印一次读取进度；默认None，即不打印

#### 读取整个文件
```
>>> seq.open('your_file_name', *args).map(...).get()
``` 
#### 读取前n行
```
>>> seq.open('your_file_name', n_limit=n, *args)
```

## 测试
如何执行自动化测试

## 如何贡献
贡献patch流程、质量要求

## 讨论
  

