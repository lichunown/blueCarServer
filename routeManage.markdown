# 路线管理模块

**必须是司机用户才可操作**

## 创建路线

POST `/route/create`

| key   | example      | info   |
| ----- | ------------ | ------ |
| token | “dscw3dewaw” | token值 |
| name  | “xidian”     | 路线名称   |
| type  | “park        | shanxi |
| data  | “...”        | 路线数据   |


### 注册成功返回

```python
  {
          'action':'createroute',
          'result':'succeed',
          'name':name,
   }
```
### 名称冲突返回

```python
  {
          'action':'createroute',
          'result':'error',
          'errorResult':'nameExist',
   }
```

### 用户权限受限返回

```python
  {
          'action':'createroute',
          'result':'error',
          'errorResult':'userLimit',
   }
```


## 删除路线

POST `/route/modify`

| key   | example      | info   |
| ----- | ------------ | ------ |
| token | “dscw3dewaw” | token值 |
| name  | “xidian”     | 路线名称   |

### 成功返回

```python
  {
          'action':'deleteRoute',
          'result':'succeed',
   }
```
### 用户权限受限返回

```python
  {
          'action':'deleteRoute',
          'result':'error',
          'errorResult':'userLimit',
   }
```
### 路线不存在返回

```python
  {
          'action':'deleteRoute',
          'result':'error',
          'errorResult':'nameNotExist',
   }
```
## 修改路线
**只能由创建线路的用户修改**
POST `/route/modify`

| key   | example      | info   |
| ----- | ------------ | ------ |
| token | “dscw3dewaw” | token值 |
| name  | “xidian”     | 路线名称   |
| data  | “...”        | 新的路线数据 |
| type  | “park        | 新的路线类型 |

## 获取路线信息

POST `/route/getdata`

| key   | example      | info   |
| ----- | ------------ | ------ |
| token | “dscw3dewaw” | token值 |
| name  | “xidian”     | 路线名称   |
### 成功返回

```python
  {
                'action':'getRouteData',
                'result':'succeed',
                'type':route.type,
                'data':route.data,
   }
```
## 获取路线列表

POST or GET `/route/list`
```python
  {
        'action':'getRouteList',
        'result':'succeed',
        'list':RouteTypeDicts,
   }
```
