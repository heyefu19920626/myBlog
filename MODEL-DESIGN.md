### 模型设计

- Category 分类表 ,由管理员提供,一篇文章只能有一个分类

| ID | 分类名 |
|:---:|:---|
| int | CharFieled |

- Tag 标签表,一篇文章具有多个标签

| ID | 标签名 |
|:---:|:---:|
| int | CharField |

- Article 博客文章表

| ID | 标题 | 正文 | 作者 | 创建时间 | 修改时间 | 分类 | 标签 | 访问量 | 赞数 | 贬数 | 评论数 |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:---:|:---:|:---:|:---:|
| int | CharField | TextField | User | DateTimeField | DateTimeField | Category | Tag | page_view | praise | censure | comments |

- Comments 评论表

| ID | 文章ID | 内容 | 作者 | 创建时间 |
|:---:|:---:|:---:|:---:|:---:|
| int |Article ID | TextFiled | User | DateTimeField |

- User 用户表

| ID | 用户名 | 密码 | 邮箱 | 昵称 | 注册时间 | 发表博文 | 头像 | 
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| int | CharField | CharField | CharField | CharField | DateTimeField | int | CharField |

- 文章 -> 标签表

| 文章ID | 标签ID |
|:---:|:---:|
| int | int |
