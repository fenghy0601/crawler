create table if not exists movieInfo(
id int comment 'ID',
name varchar(50) comment '影片名',
keywords varchar(100) comment '关键词',
ratingnum double comment '评分',
director varchar(30) comment '导演',
actor varchar(100) comment '主演',
movietype varchar(50) comment '电影类型',
moviedate varchar(50) comment '上映日期',
runtime int comment '电影时长',
summary varchar(2000) comment '剧情简介'
);

use crawler;
insert into movieInfo (id, name, keywords, ratingnum, director, actor, movietype, moviedate, runtime, summary) 
values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
