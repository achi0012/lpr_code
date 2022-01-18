drop table if exists public.tcpd_carcheck;

CREATE TABLE public.tcpd_carcheck (
	check_carlicense varchar(20), 
	video_name varchar(20), 
	carcheck_time timestamp, 
	screenshots_path varchar(254), 
	panoramic_path varchar(254), 
	recognition_type int
) order by check_carlicense, carcheck_time
segmented by hash(check_carlicense, carcheck_time) all nodes

drop table if exists public.tcpd_involved;

CREATE TABLE public.tcpd_involved
(
    involved_id int,
    check_carlicense varchar(20),
    involved_time timestamp,
    create_id varchar(20),
    create_time timestamp,
    update_id varchar(20),
    update_time timestamp,
    remark varchar(254),
    group_list varchar(254)
) order by check_carlicense
segmented by hash(check_carlicense) all nodes;

drop table if exists public.tcpd_stolen;

CREATE TABLE public.tcpd_stolen
(
    stolen_id int,
    check_carlicense varchar(20),
    stolen_time timestamp,
    create_id varchar(20),
    create_time timestamp,
    remark varchar(254),
    group_list varchar(254)
) order by check_carlicense
segmented by hash (check_carlicense) all nodes;

