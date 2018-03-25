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

| ID | 标题 | 正文 | 作者 | 创建时间 | 修改时间 | 分类 | 标签 |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| int | CharField | TextField | User | DateTimeField | DateTimeField | Category | Tag |