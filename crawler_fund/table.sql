use crawler;
create table fundinfo(
 ID varchar(20) not null comment '基金代码',
 NAME varchar(100) not null comment '基金名称',
 DATE timestamp null comment '日期',
 VALUE double null comment '基金净值',
 R_DAY double null comment '最近1日收益率',
 R_WEEK double null comment '最近1周收益率',
 R_MONTH double null comment '最近1月收益率',
 R_3MONTH double null comment '最近3月收益率',
 R_6MONTH double null comment '最近6月收益率',
 R_YEAR double null comment '最近1年收益率',
 R_2YEAR double null comment '最近2年收益率',
 R_3YEAR double null comment '最近3年收益率',
 SINCE_THIS_YEAR double null comment '今年以来收益率',
 SINCE_SET_UP double null comment '成立以来收益率',
 BUY_RATE double null comment '申购费率',
 LOWEST_COST varchar(20) null comment '最低申购额',
 TYPE varchar(10) not null comment '基金类型:pg-偏股型,gp-股票,hh-混合,zq-债券,zs-指数,qdii-QDII基金');

load data infile 'fund_data.csv'
into table crawler.fundinfo
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\n';