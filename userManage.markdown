[TOC]

## 用户管理

*测试服务器http://lcyown.cn:2000/*

以`POST`形式传输信息



| 网址            | 类别     |      |
| ------------- | ------ | ---- |
| /user/signup  | 用户注册   |      |
| /user/login   | 用户登录   |      |
| /user/logout  | 用户登出   |      |
| /user/modify  | 用户数据修改 |      |
| /user/getdata | 获取用户数据 |      |

### 注册

POST `/user/signup`

| key      | example  | info |
| -------- | -------- | ---- |
| username | "string" | 用户名  |
| password | "string" | 密码   |

#### 注册成功返回

```python
  {
          'action':'signup',
          'result':'succeed',
          'username':'usernameExist',
   }
```

  ​

#### 用户名冲突返回

```python
  {
          'action':'signup',
          'result':'error',
          'errorResult':'usernameExist',
  }
```

### 用户登录
POST `/user/login`

| key      | example  | info |
| -------- | -------- | ---- |
| username | "string" | 用户名  |
| password | "string" | 密码   |

#### 注册成功返回

```python
  {
          'action':'signin',
          'result':'succeed',
          'token':token,
   }
```

**注册成功返回token值。以后的用户管理等所有操作均由token完成**

#### 用户名不存在返回

```python
  {
          'action':'signin',
          'result':'error',
          'errorResult':'usernameNotExist',
  }
```

#### 密码错误返回

```python
  {
          'action':'signin',
          'result':'error',
          'errorResult':'passwordError',
  }
```

  ### 用户登出

  ​POST `/user/logout`

| key   | example                       | info   |
| ----- | ----------------------------- | ------ |
| token | "e32ry3928rfh23o9tw9fhr92t3g" | token值 |

#### 成功返回

```python
  {
          'action':'logout',
          'result':'succeed',
          'username':'myname',
  }
```

#### 失败返回

```python
  {
          'action':'logout',
          'result':'error',
          'errorResult':'keyError',
  }
```

  ### 用户数据修改

  ​POST `/user/modify`

| key        | example                                  | info   |
| ---------- | ---------------------------------------- | ------ |
| token      | "e32ry3928rfh23o9tw9fhr92t3g"            | token值 |
| modifydata | '{"college":"newcollege","studentid":"newstudentid"}' | 修改的数据  |
**modifydata以字典的形式传入**
*eg:*
```javascript
  {
      "college":"newcollege",
      "studentid":"newstudentid",
      "truename":"newName"
  }
```
##### json格式错误返回
```python
  {
          'action':'modify',
          'result':'error',
          'errorResult':error,
  }
```
#### 成功返回

```python
  {
          'action':'modify',
          'result':'succeed',
  }
```

#### 失败返回

```python
  {
          'action':'modify',
          'result':'error',
          'errorResult':errorResult,
  }
```
##### 失败原因
| errorResult       | info      |
| ----------------- | --------- |
| 'tokenDoNotExist' | 没有传入token |
| 'userDoNotExist'  | 用户不存在     |

### 获取用户数据
获取他人信息，与获取自己的信息不同。登录用户获取自身信息将会获取更全面的信息。
但API的调用相同。
  ​POST `/user/getdata`

| 是否必须 | key             | example                       | info   |
| ---- | --------------- | ----------------------------- | ------ |
|      | token           | "e32ry3928rfh23o9tw9fhr92t3g" | token值 |
| *    | getdatausername | "username"                    | 用户名    |