-- Table: public.make_model_dz

DROP TABLE public.make_model_dz;

CREATE TABLE public.make_model_dz
(
    auto varchar(20) COLLATE pg_catalog."default" NOT NULL,
    line varchar(20) COLLATE pg_catalog."default" NOT NULL,
    branch_name2 varchar(50) COLLATE pg_catalog."default",
    vhl_code_jy varchar(50) COLLATE pg_catalog."default" NOT NULL,
    make_model varchar(50) COLLATE pg_catalog."default",
    rlt_mm double precision
)

TABLESPACE pg_default;

ALTER TABLE public.make_model_dz
    OWNER to postgres;

COMMENT ON TABLE public.make_model_dz
    IS 'make model information from make_model.csv ';