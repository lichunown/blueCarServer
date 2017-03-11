[TOC]

## 用户坐标管理

| url                         | description |
| --------------------------- | ----------- |
| /position/send              | 发送用户自己的坐标   |
| /position/getcars           | 获取车辆坐标      |
| /position/getpeoples        | 获取等车人坐标     |
| /position/callcar           | 呼叫车辆        |
| /position/getcallcarpeoples | 获取呼叫车辆的人位置  |
| /position/saveposition      | 保存自己的位置     |
| /position/getpositions      | 获取用户保存的位置   |

### 发送坐标

POST `/position/send`

| key       | example                       | info   |
| --------- | ----------------------------- | ------ |
| token     | "e32ry3928rfh23o9tw9fhr92t3g" | token值 |
| latitude  | 100                           | 纬度     |
| longitude | 100                           | 经度     |





### 获取车辆坐标

POST `/position/send`

| key   | example                       | info   |
| ----- | ----------------------------- | ------ |
| token | "e32ry3928rfh23o9tw9fhr92t3g" | token值 |

####  返回数据

```javascript
{
        'action':'getpeoples',
        'result':'succeed',
        'positions':[
        		[100,100],
        		[50,50],
        		[64,54]
        	]
}
```





### 获取其他人坐标

POST `/position/getpeoples`

| key   | example                       | info   |
| ----- | ----------------------------- | ------ |
| token | "e32ry3928rfh23o9tw9fhr92t3g" | token值 |

####  返回数据

```javascript
{
        'action':'getpeoples',
        'result':'succeed',
        'positions':[
        		[100,100],
        		[50,50],
        		[64,54]
        	]
}
```





### 呼叫车辆

POST `/position/callcar`

|    key    |            example            |  info  |  必须  |
| :-------: | :---------------------------: | :----: | :--: |
|   token   | "e32ry3928rfh23o9tw9fhr92t3g" | token值 |  *   |
| latitude  |              100              |   纬度   |  *   |
| longitude |              100              |   经度   |  *   |

####  返回数据

```javascript
{
          'action':'callcar',
          'result':'succeed',
}
```




### 获取呼叫车辆所有人位置

POST `/position/getcallcarpeoples`

|  key  |            example            |  info  |  必须  |
| :---: | :---------------------------: | :----: | :--: |
| token | "e32ry3928rfh23o9tw9fhr92t3g" | token值 |  *   |


####  返回数据

```javascript
{
        'action':'getcallcarpeoples',
        'result':'succeed',
        'positions':[
        		[100,100],
        		[50,50],
        		[64,54]
        	]
}
```





### 保存位置

POST `/position/saveposition`

|    key    |            example            |    info     |  必须  |
| :-------: | :---------------------------: | :---------: | :--: |
|   token   | "e32ry3928rfh23o9tw9fhr92t3g" |   token值    |  *   |
| latitude  |              100              |     纬度      |  *   |
| longitude |              100              |     经度      |  *   |
|    tag    |            "home"             | 标签，表明保存坐标原因 |      |


####  返回数据

```javascript
{
          'action':'saveposition',
          'result':'succeed',
}
```





### 获取用户保存的坐标

POST `/position/getpositions`

|   key   |            example            |    info     |  必须  |
| :-----: | :---------------------------: | :---------: | :--: |
|  token  | "e32ry3928rfh23o9tw9fhr92t3g" |   token值    |  *   |
| getuser |            "qwer"             |   获取的用户名    |      |
|   tag   |            "home"             | 标签，表明保存坐标原因 |      |

**注1：测试阶段只能允许获取用户自己保存的坐标，无法获取他人信息**

**注2：getuser空时默认获取用户自身**

####  返回数据

```javascript
{
                'action':'getposition',
                'result':'succeed',
                'positions':[
                 	{
                        'latitude':100.0,
                        'longitude':100.0,
                        'tag':"home",
                        'time':"2017-03-11 06:38:42.904000+00:00"
                 	},
                  	{
                        'latitude':100.0,
                        'longitude':100.0,
                        'tag':"None",
                        'time':"2017-03-11 06:38:42.904000+00:00"                      
                  	}
                ]
}
```