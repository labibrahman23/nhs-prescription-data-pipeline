
create table if not exists prescriptions(

    prescription_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    year_month DATE NOT NULL,
    regional_office_name TEXT NOT NULL,
    regional_office_code TEXT NOT NULL,
    icb_name TEXT, 
    icb_code TEXT,
    pco_name TEXT,
    pco_code TEXT,
    practice_name TEXT,
    practice_code TEXT,
    postcode TEXT,
    bnf_chemical_substance_code TEXT,
    bnf_chemical_substance TEXT, 
    bnf_presentation_code TEXT,
    bnf_presentation_name TEXT,
    bnf_chapter_plus_code TEXT,
    quantity INT NOT NULL,
    items INT NOT NULL,
    total_quantity INT NOT NULL,
    adq_usage DECIMAL(10,2),
    nic DECIMAL(10,2),
    actual_cost DECIMAL(10,2) NOT NULL,
    unidentified BOOLEAN,
    snomed_code TEXT
);