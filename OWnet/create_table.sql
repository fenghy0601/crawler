use crawler;
create table crawler.stockinfo(
id varchar(100) not null primary key comment'ID',
net_id varchar(50) not null comment  '网页ID',
stock_id int(8) not null comment '股票ID',
stock_name varchar(200) not null comment '名称',
open_price varchar(30) comment '开盘价',
close_price varchar(30) comment '收盘价',
max_price varchar(30) comment '当日最高价',
min_price varchar(30) comment '当日最低价',
limit_up varchar(30) comment '涨停价',
limit_down varchar(30) comment '跌停价',
turnover_rate varchar(30) comment '换手率',
volumn_ratio varchar(30) comment '量比',
volumn varchar(100) comment '成交量',
turnover varchar(100) comment '成交额',
pe_ratio varchar(30) comment '市盈率',
pb_ratio varchar(30) comment '市净率',
market_cap varchar(100) comment '总市值',
famc varchar(100) comment '流通市值',
date varchar(30) not null comment '日期',
createtime datetime comment '创建日期',
updatetime datetime comment '更新日期'
)