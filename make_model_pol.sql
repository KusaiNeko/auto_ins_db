-- Table: public.make_model_pol

DROP TABLE public.make_model_pol;

CREATE TABLE public.make_model_pol
(
    full_vhl_cd character varying(20) COLLATE pg_catalog."default",
    full_vhl_cname character varying(50) COLLATE pg_catalog."default",
    vhl_type character varying(10) COLLATE pg_catalog."default",
    maker_jv character varying(20) COLLATE pg_catalog."default",
    maker_cd character varying(20) COLLATE pg_catalog."default",
    full_maker_cname character varying(50) COLLATE pg_catalog."default",
    brand_cname character varying(20) COLLATE pg_catalog."default",
    brand_cd character varying(20) COLLATE pg_catalog."default",
    model_cd character varying(20) COLLATE pg_catalog."default",
    model_cd_jy character varying(20) COLLATE pg_catalog."default",
    register_year character varying(20) COLLATE pg_catalog."default",
    --vhl_capacity double precision
	vhl_capacity varchar(10)
)

TABLESPACE pg_default;

ALTER TABLE public.make_model_pol
    OWNER to postgres;
	
COMMENT ON TABLE public.make_model_pol
    IS 'make model information from make_model.txt';