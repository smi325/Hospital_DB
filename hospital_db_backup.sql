PGDMP     4                    y            hospital_db_1    14.1    14.1                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16394    hospital_db_1    DATABASE     j   CREATE DATABASE hospital_db_1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE hospital_db_1;
                postgres    false            ?            1259    16467 
   Department    TABLE     ?   CREATE TABLE public."Department" (
    name text NOT NULL,
    manager text NOT NULL,
    phone text NOT NULL,
    hosp_name text NOT NULL
);
     DROP TABLE public."Department";
       public         heap    postgres    false            ?            1259    16509    Doctor    TABLE     ?   CREATE TABLE public."Doctor" (
    name text NOT NULL,
    "position" text NOT NULL,
    phone text NOT NULL,
    hosp_name text NOT NULL,
    dep_name text NOT NULL
);
    DROP TABLE public."Doctor";
       public         heap    postgres    false            ?            1259    16521     Doctors prescription for Patient    TABLE     ?   CREATE TABLE public."Doctors prescription for Patient" (
    hosp_name text NOT NULL,
    dep_name text NOT NULL,
    doc_name text NOT NULL,
    patient_name text NOT NULL,
    prescription text NOT NULL
);
 6   DROP TABLE public."Doctors prescription for Patient";
       public         heap    postgres    false            ?            1259    16405    Hospital    TABLE     o   CREATE TABLE public."Hospital" (
    name text NOT NULL,
    address text NOT NULL,
    phone text NOT NULL
);
    DROP TABLE public."Hospital";
       public         heap    postgres    false            ?            1259    16410    Patient    TABLE     h   CREATE TABLE public."Patient" (
    name text NOT NULL,
    sex text NOT NULL,
    age text NOT NULL
);
    DROP TABLE public."Patient";
       public         heap    postgres    false                      0    16467 
   Department 
   TABLE DATA           G   COPY public."Department" (name, manager, phone, hosp_name) FROM stdin;
    public          postgres    false    211   ?                 0    16509    Doctor 
   TABLE DATA           P   COPY public."Doctor" (name, "position", phone, hosp_name, dep_name) FROM stdin;
    public          postgres    false    212   >                 0    16521     Doctors prescription for Patient 
   TABLE DATA           w   COPY public."Doctors prescription for Patient" (hosp_name, dep_name, doc_name, patient_name, prescription) FROM stdin;
    public          postgres    false    213   ?                 0    16405    Hospital 
   TABLE DATA           :   COPY public."Hospital" (name, address, phone) FROM stdin;
    public          postgres    false    209   ?                 0    16410    Patient 
   TABLE DATA           3   COPY public."Patient" (name, sex, age) FROM stdin;
    public          postgres    false    210   ?       p           2606    16473    Department Department_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public."Department"
    ADD CONSTRAINT "Department_pkey" PRIMARY KEY (name, hosp_name);
 H   ALTER TABLE ONLY public."Department" DROP CONSTRAINT "Department_pkey";
       public            postgres    false    211    211            t           2606    16527 G   Doctors prescription for Patient Doctor's prescription for Patient_pkey 
   CONSTRAINT     ?   ALTER TABLE ONLY public."Doctors prescription for Patient"
    ADD CONSTRAINT "Doctor's prescription for Patient_pkey" PRIMARY KEY (patient_name, doc_name, dep_name, hosp_name);
 u   ALTER TABLE ONLY public."Doctors prescription for Patient" DROP CONSTRAINT "Doctor's prescription for Patient_pkey";
       public            postgres    false    213    213    213    213            r           2606    16515    Doctor Doctor_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public."Doctor"
    ADD CONSTRAINT "Doctor_pkey" PRIMARY KEY (name, hosp_name, dep_name);
 @   ALTER TABLE ONLY public."Doctor" DROP CONSTRAINT "Doctor_pkey";
       public            postgres    false    212    212    212            l           2606    16416    Hospital Hospital_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public."Hospital"
    ADD CONSTRAINT "Hospital_pkey" PRIMARY KEY (name);
 D   ALTER TABLE ONLY public."Hospital" DROP CONSTRAINT "Hospital_pkey";
       public            postgres    false    209            n           2606    16438    Patient Patient_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public."Patient"
    ADD CONSTRAINT "Patient_pkey" PRIMARY KEY (name);
 B   ALTER TABLE ONLY public."Patient" DROP CONSTRAINT "Patient_pkey";
       public            postgres    false    210            x           2606    16533 0   Doctors prescription for Patient fk_hosp_dep_doc    FK CONSTRAINT     ?   ALTER TABLE ONLY public."Doctors prescription for Patient"
    ADD CONSTRAINT fk_hosp_dep_doc FOREIGN KEY (hosp_name, dep_name, doc_name) REFERENCES public."Doctor"(hosp_name, dep_name, name);
 \   ALTER TABLE ONLY public."Doctors prescription for Patient" DROP CONSTRAINT fk_hosp_dep_doc;
       public          postgres    false    212    212    213    213    3186    213    212            v           2606    16516    Doctor fk_hosp_dep_names    FK CONSTRAINT     ?   ALTER TABLE ONLY public."Doctor"
    ADD CONSTRAINT fk_hosp_dep_names FOREIGN KEY (hosp_name, dep_name) REFERENCES public."Department"(hosp_name, name);
 D   ALTER TABLE ONLY public."Doctor" DROP CONSTRAINT fk_hosp_dep_names;
       public          postgres    false    3184    211    212    212    211            u           2606    16474    Department fk_hosp_name    FK CONSTRAINT     ?   ALTER TABLE ONLY public."Department"
    ADD CONSTRAINT fk_hosp_name FOREIGN KEY (hosp_name) REFERENCES public."Hospital"(name);
 C   ALTER TABLE ONLY public."Department" DROP CONSTRAINT fk_hosp_name;
       public          postgres    false    3180    211    209            w           2606    16528 '   Doctors prescription for Patient fk_pat    FK CONSTRAINT     ?   ALTER TABLE ONLY public."Doctors prescription for Patient"
    ADD CONSTRAINT fk_pat FOREIGN KEY (patient_name) REFERENCES public."Patient"(name);
 S   ALTER TABLE ONLY public."Doctors prescription for Patient" DROP CONSTRAINT fk_pat;
       public          postgres    false    210    3182    213               r   x???,*-J?L?t,*N??L-S?Ћⴴ?52?5??L????LNT0?JN,J???t?O.?/?/S?????45?56?55CRW?Z?X 4ϥ4%??*X???D??T???ʈ+F??? I?#?         ?   x?mͻ?0????)?m?\?#	?????Z8	RsZ??	???ϗ???&t?_?MB"c1 ?ԃҙPe?Nh?ah?N??e+????B$:?E???????'~??mcu?G?C?
???\k???b.????˥E??|??D?'-??d???YC?         ?   x?}?1
?@@?z?{????$E?"6AҌ??G???g?% )????Y??^JIMw_a????Qw??x}?.r??u?e+???/? ,,Gn?l??V??w??????\w?"??{??FK????K????!j?/?D????M?         C   x?K????LNT0?,???I????M9??t?LtM,????F ?????#KNs]#]Ss?=... ?U?         A   x??????IL-S?s????45?
?
??%*8?y?q?q?qEe楧)????Yr??qqq UB     