--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.3

-- Started on 2020-12-05 13:26:20

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 17076)
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name character varying,
    gender character varying,
    birthdate date
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 17074)
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO postgres;

--
-- TOC entry 2836 (class 0 OID 0)
-- Dependencies: 202
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- TOC entry 204 (class 1259 OID 17087)
-- Name: movies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    title character varying,
    release date
);


ALTER TABLE public.movies OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 17093)
-- Name: movies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_id_seq OWNER TO postgres;

--
-- TOC entry 2837 (class 0 OID 0)
-- Dependencies: 205
-- Name: movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;


--
-- TOC entry 2695 (class 2604 OID 17095)
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- TOC entry 2696 (class 2604 OID 17096)
-- Name: movies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);


--
-- TOC entry 2828 (class 0 OID 17076)
-- Dependencies: 203
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (id, name, gender, birthdate) FROM stdin;
2	Harrison Ford	Male	1942-07-13
3	Carrie Fisher	Female	1956-10-21
4	Harrison Ford	Male	1942-07-13
5	Carrie Fisher	Female	1956-10-21
6	Harrison Ford	Male	1942-07-13
7	Carrie Fisher	Female	1956-10-21
8	Harrison Ford	Male	1942-07-13
9	Carrie Fisher	Female	1956-10-21
10	Harrison Ford	Male	1942-07-13
11	Carrie Fisher	Female	1956-10-21
12	Harrison Ford	Male	1942-07-13
13	Carrie Fisher	Female	1956-10-21
14	Harrison Ford	Male	1942-07-13
15	Carrie Fisher	Female	1956-10-21
16	Harrison Ford	Male	1942-07-13
17	Carrie Fisher	Female	1956-10-21
18	Harrison Ford	Male	1942-07-13
\.


--
-- TOC entry 2829 (class 0 OID 17087)
-- Dependencies: 204
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.movies (id, title, release) FROM stdin;
3	Blade Runner	1982-06-25
4	Blade Runner	1982-06-25
5	Blade Runner	1982-06-25
6	Blade Runner	1982-06-25
2	Star Wars	1982-06-25
7	Blade Runner	1982-06-25
8	Blade Runner	1982-06-25
9	Blade Runner	1982-06-25
10	Blade Runner	1982-06-25
11	Blade Runner	1982-06-25
12	Blade Runner	1982-06-25
13	Blade Runner	1982-06-25
14	Blade Runner	1982-06-25
15	Blade Runner	1982-06-25
16	Blade Runner	1982-06-25
17	Blade Runner	1982-06-25
\.


--
-- TOC entry 2838 (class 0 OID 0)
-- Dependencies: 202
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actors_id_seq', 18, true);


--
-- TOC entry 2839 (class 0 OID 0)
-- Dependencies: 205
-- Name: movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.movies_id_seq', 17, true);


--
-- TOC entry 2698 (class 2606 OID 17084)
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- TOC entry 2700 (class 2606 OID 17098)
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);


-- Completed on 2020-12-05 13:26:21

--
-- PostgreSQL database dump complete
--

