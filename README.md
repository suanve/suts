
# sus

工具集合

## 安装
```shell
pip install suts


git clone https://github.com/suanve/suts \
cd suts && python setup.py install

```

## misc


## lib
### flask
1. fscm
管理flask session cookie
```python
import suts
print(suts.fscm("1",'{"a":"123"}',1))
print(suts.fscm("1",'eyJhIjoiMTIzIn0.YxWzUA.eXmLa8ID6TJPKmAKd0stjH6P2xw',0))
```


[x] 1