-- 进入数据库
mysql -uroot -p
-- 输入密码 在终端中是没有显示的

-- 查询mysql中有哪些数据库
show databases;


-- 进入到指定数据库
use 数据库名称;

-- 查询当前数据库中有哪些表
show tables;


-- 退出数据库
exit;


-- 创建数据库
create database python charset=utf8;

-- 删除指定数据库
drop database python;


-- 在指定的数据库中去创建一个班级表
-- 当前班级表中有两个字段
    -- 主键
    -- 班级名称

create table classes(
    -- 主键 unsigned: 整型无符号(没有负数)
    id int unsigned primary key auto_increment not null,
    name varchar(10)
    -- 在创建表字段时, 最后一个字段不能添加逗号
)

-- 查询表结构
desc 表名;

desc classes;


-- 创建学生表
create table students(
    -- 主键非空无符号并自动增长
    id int unsigned primary key auto_increment not null,
    -- 字符串 最大字节数为20 并且有默认值 默认值为空字符串
    name varchar(20) default '',
    -- 整型类型(-128 - 127 有符号的条件下) 无符号为 0 - 255 默认值为0
    age tinyint unsigned default 0,
    -- 浮点型 实数为3位 小数为2位
    height decimal(5,2),
    -- 枚举类型 必须要在给定的选项中选择一个
    gender enum('男','女','人妖','保密'),
    -- 无符号的整型类型 默认值为0
    cls_id int unsigned default 0
);

-- 对当前学生表添加一个字段 birthday add: 添加字段
alter table 表名 add 字段名称 字段类型;

alter table students add birthday datetime;

-- 发现当前字段名称不符合要求  需要对字段名重新命名 change: 重命名字段
alter table 表名 change 原名 新名 类型及约束;
alter table students change birthday birth datetime not null;

-- 当前字段名称符合规则, 但是当前字段类型不符合要求
alter table 表名 modify 列名 类型及约束;
alter table students modify birth date not null;

-- 删除字段
alter table 表名 drop 字段名;
alter table students drop birth;


-- 查询表中的数据
select * from 表名;
select * from classes;

-- 查询表中的指定字段
select 字段名 from 表名;
select name from classes;

-- 查询多个指定字段 语句中的字段位置会影响查询出来的字段的显示位置
select name,id from classes;

-- 查询多个字段 字段显示为中文
select name as 班级名称 from classes;


-- 数据插入  数据插入可以使用 navicat 但是现阶段不建议使用

-- 准备工作 添加字段
alter table students add hometown varchar(10);
alter table students add birthday date;
insert into 表名(列1,...) values(值1,...);
insert into students(name,hometown,birthday) values('黄蓉','桃花岛','2016-3-2');

-- 只插入名称数据
insert into students(name) values('杨康'),('杨过'),('小龙女');


-- 修改数据
update 表名 set 列1=值1,列2=值2... where 条件
update students set gender='女',hometown='北京' where id=4;

-- 数据删除
delete from students where id=4; -- 一般情况下在公司开发中是没有权限的

    -- 逻辑删除
    -- 在当前这条数据中添加一个字段 is_delete 根据当前字段的值判断这个字段是否显示
    alter table students add is_delete bit;

    -- 如果现在获取到数据之后通过if判断当前这个字段的值是否为1 如果为1 则显示 如果为0 则隐藏



-- orm
--     数据库的一个框架
--         面向对象的方式对数据库进行增删改查



